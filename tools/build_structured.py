"""Relocate translated group-1 menu/event records without changing their opcodes."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import struct

parser = argparse.ArgumentParser()
parser.add_argument('--rom', type=Path, required=True)
parser.add_argument('--output-dir', type=Path)
args = parser.parse_args()

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = args.output_dir or ROOT / 'build'
SOURCE_HASH = '58b7ad86fae87e572e8474eb935ecda165e71c741096cd687f96bed96fbba05c'
BASE = 0x31CD4C
POOL_START = 0x4F0000
POOL_END = 0x500000
OUTPUT.mkdir(parents=True, exist_ok=True)

rom_path = args.rom.resolve()
original = rom_path.read_bytes()
assert hashlib.sha256(original).hexdigest() == SOURCE_HASH, 'Unexpected Japanese ROM'
out_path = OUTPUT / 'Beyblade-AHEJ-English-opening-NARROW-EXPERIMENTAL.gba'
out = bytearray(out_path.read_bytes())
source_path = ROOT / 'translations' / 'structured-menus-en.json'
if not source_path.exists():
    source_path = ROOT / 'structured-menus-en.json'
source = json.loads(source_path.read_text('utf-8'))
expected_resources = {0, 3, 9, 12, 17, 20, 29, *range(35, 96, 3)}
assert {entry['resource'] for entry in source['entries']} == expected_resources

def encode_english(text):
    converted = ''.join('　' if char == ' ' else
                        chr(ord(char) + 0xFEE0) if '!' <= char <= '~' else char
                        for char in text)
    return converted.encode('cp932', errors='strict')

cursor = POOL_START
manifest = []
seen = set()
for entry in source['entries']:
    resource = entry['resource']
    assert resource not in seen, f'Duplicate structured resource {resource}'
    seen.add(resource)
    assert len(entry['japanese']) == len(entry['english'])
    table_entry = BASE + resource * 4
    old_start = BASE + struct.unpack_from('<I', original, table_entry)[0]
    old_end = BASE + struct.unpack_from('<I', original, table_entry + 4)[0]
    original_payload = original[old_start:old_end]
    payload = bytearray(original_payload)
    replacements = []
    for japanese, english in zip(entry['japanese'], entry['english']):
        assert english.strip(), (resource, japanese, 'empty translation')
        assert not re.search(r'[\u3040-\u30ff\u3400-\u9fff]', english), (resource, japanese, english)
        old = japanese.encode('cp932', errors='strict')
        new = encode_english(english)
        assert original_payload.count(old) == 1, (resource, japanese, original_payload.count(old))
        assert payload.count(old) == 1, (resource, japanese)
        position = payload.index(old)
        payload[position:position + len(old)] = new
        replacements.append({'japanese': japanese, 'english': english,
                             'old_bytes': len(old), 'new_bytes': len(new)})
    while cursor % 4:
        cursor += 1
    new_start = cursor
    new_end = new_start + len(payload)
    assert new_end <= POOL_END, 'Structured menu pool exceeds reserved range'
    assert all(value == 0xFF for value in out[new_start:new_end]), 'Structured pool overlaps existing data'
    out[new_start:new_end] = payload
    struct.pack_into('<I', out, table_entry, new_start - BASE)
    manifest.append({'resource': resource, 'table_offset': hex(table_entry),
                     'old_offset': hex(old_start), 'new_offset': hex(new_start),
                     'old_bytes': len(original_payload), 'new_bytes': len(payload),
                     'replacements': replacements})
    cursor = new_end

out_path.write_bytes(out)
(OUTPUT / 'structured-manifest.json').write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Relocated {len(manifest)} structured resources; {sum(len(x["replacements"]) for x in manifest)} strings; pool ends at {cursor:#x}')
