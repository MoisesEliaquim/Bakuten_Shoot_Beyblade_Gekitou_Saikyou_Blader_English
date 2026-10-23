"""Independently apply an IPS patch and compare it with its built ROM."""
from pathlib import Path
import argparse
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument('stem')
parser.add_argument('--rom', type=Path, required=True)
parser.add_argument('--output-dir', type=Path)
args = parser.parse_args()
root = args.output_dir or Path(__file__).resolve().parents[1] / 'build'
source = args.rom.resolve().read_bytes()
assert hashlib.sha256(source).hexdigest() == '58b7ad86fae87e572e8474eb935ecda165e71c741096cd687f96bed96fbba05c'
result = bytearray(source)
patch = (root / (args.stem+'.ips')).read_bytes()
assert patch[:5] == b'PATCH'
cursor = 5
records = 0
while patch[cursor:cursor+3] != b'EOF':
    assert cursor+5 <= len(patch), 'Truncated record'
    offset = int.from_bytes(patch[cursor:cursor+3], 'big')
    length = int.from_bytes(patch[cursor+3:cursor+5], 'big')
    cursor += 5
    if length:
        chunk = patch[cursor:cursor+length]
        assert len(chunk) == length
        cursor += length
    else:
        assert cursor+3 <= len(patch)
        count = int.from_bytes(patch[cursor:cursor+2], 'big')
        assert count
        chunk = bytes([patch[cursor+2]])*count
        cursor += 3
    if len(result) < offset+len(chunk):
        result.extend(bytes(offset+len(chunk)-len(result)))
    result[offset:offset+len(chunk)] = chunk
    records += 1
assert cursor+3 == len(patch), 'Unexpected data after EOF'
expected = (root / (args.stem+'.gba')).read_bytes()
assert result == expected, 'IPS result differs from built ROM'
print(f'Verified {records} IPS records; {len(result)} bytes; SHA-256 {hashlib.sha256(result).hexdigest()}')
