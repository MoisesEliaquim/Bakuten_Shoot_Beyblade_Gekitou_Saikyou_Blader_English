"""Add pointer-relocated UI translations to the narrow-font sample."""
from pathlib import Path
import hashlib
import json
import struct
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--output-stem', default='Beyblade-AHEJ-English-UI-EXPERIMENTAL')
parser.add_argument('--rom', type=Path, required=True)
parser.add_argument('--output-dir', type=Path)
args = parser.parse_args()

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = args.output_dir or ROOT / 'build'
OUTPUT.mkdir(parents=True, exist_ok=True)
original = args.rom.resolve().read_bytes()
assert hashlib.sha256(original).hexdigest() == '58b7ad86fae87e572e8474eb935ecda165e71c741096cd687f96bed96fbba05c'
out = bytearray((OUTPUT / 'Beyblade-AHEJ-English-opening-NARROW-EXPERIMENTAL.gba').read_bytes())
cursor = 0x7F0000
entries = json.loads((ROOT / 'translations' / 'menus-en.json').read_text('utf-8'))
for entry in entries:
    old = int(entry['offset'], 16)
    jp = bytes.fromhex(entry['japanese_hex']) if 'japanese_hex' in entry else entry['japanese'].encode('cp932')
    assert original[old:old+len(jp)+1] == jp+b'\0', entry
    assert len(entry['english']) <= entry.get('max_chars',len(entry['japanese'])), 'UI label exceeds its validated display capacity'
    english = (bytes.fromhex(entry['english_hex'])+b'\0\0' if 'english_hex' in entry else
               ''.join('　' if c == ' ' else chr(ord(c)+0xFEE0) if '!' <= c <= '~' else c
                       for c in entry['english']).encode('cp932')+b'\0\0')
    assert cursor+len(english) <= len(out), 'UI allocation exceeds ROM capacity'
    assert all(v == 255 for v in out[cursor:cursor+len(english)])
    for pointer in entry['pointers']:
        location = int(pointer, 16)
        assert struct.unpack_from('<I', original, location)[0] == old+0x08000000
        struct.pack_into('<I', out, location, cursor+0x08000000)
    entry['new_offset'] = hex(cursor)
    out[cursor:cursor+len(english)] = english
    cursor = (cursor+len(english)+3) & ~3
stem = args.output_stem
from battle_patch import apply_battle
battle_manifest = apply_battle(original, out, ROOT / 'translations' / 'battle-en.json')
(OUTPUT / 'battle-manifest.json').write_text(json.dumps(battle_manifest, indent=2), encoding='utf-8')
(OUTPUT / (stem+'.gba')).write_bytes(out)
patch = bytearray(b'PATCH')
position = 0
# Emit all changes, including code hooks and expansion, independently of earlier patches.
while position < len(out):
    if position < len(original) and out[position] == original[position]:
        position += 1
        continue
    start = position
    while position < len(out) and position-start < 65535:
        if position < len(original) and out[position] == original[position]:
            break
        position += 1
    chunk = out[start:position]
    if chunk and all(value == chunk[0] for value in chunk):
        patch += start.to_bytes(3, 'big')+b'\0\0'+len(chunk).to_bytes(2, 'big')+chunk[:1]
    else:
        patch += start.to_bytes(3, 'big')+len(chunk).to_bytes(2, 'big')+chunk
patch += b'EOF'
(OUTPUT / (stem+'.ips')).write_bytes(patch)
(OUTPUT / 'menus-manifest.json').write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Built {len(entries)} UI entries; translation data ends at {cursor:#x}')
