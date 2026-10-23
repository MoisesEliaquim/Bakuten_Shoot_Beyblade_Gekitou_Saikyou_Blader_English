"""Apply this project's IPS patch to an exact-match original ROM copy."""
import argparse
import hashlib
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--rom', type=Path, required=True)
parser.add_argument('--patch', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
if args.output.exists() or args.output.resolve() == args.rom.resolve():
    parser.error('Choose a new output file; existing files will not be overwritten.')
original = args.rom.read_bytes()
if hashlib.sha256(original).hexdigest() != '58b7ad86fae87e572e8474eb935ecda165e71c741096cd687f96bed96fbba05c':
    parser.error('Original ROM hash does not match the supported Japanese AHEJ release.')
patch = args.patch.read_bytes()
if not patch.startswith(b'PATCH'):
    parser.error('Not an IPS patch.')
result = bytearray(original)
cursor = 5
while patch[cursor:cursor+3] != b'EOF':
    if cursor+5 > len(patch):
        parser.error('Truncated patch record.')
    offset = int.from_bytes(patch[cursor:cursor+3], 'big')
    count = int.from_bytes(patch[cursor+3:cursor+5], 'big')
    cursor += 5
    if count:
        chunk = patch[cursor:cursor+count]
        if len(chunk) != count:
            parser.error('Truncated patch data.')
        cursor += count
    else:
        if cursor+3 > len(patch):
            parser.error('Truncated run-length record.')
        count = int.from_bytes(patch[cursor:cursor+2], 'big')
        if count == 0:
            parser.error('Empty run-length record.')
        chunk = bytes([patch[cursor+2]])*count
        cursor += 3
    if len(result) < offset+len(chunk):
        result.extend(bytes(offset+len(chunk)-len(result)))
    result[offset:offset+len(chunk)] = chunk
if cursor+3 != len(patch):
    parser.error('Unexpected trailing patch data.')
args.output.parent.mkdir(parents=True, exist_ok=True)
with args.output.open('xb') as target:
    target.write(result)
print(f'Wrote {args.output}; SHA-256 {hashlib.sha256(result).hexdigest()}')
