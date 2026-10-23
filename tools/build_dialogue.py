"""Build a relocated English opening sample, preserving the original ROM file."""
from pathlib import Path
import hashlib
import json
import struct
import textwrap
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--narrow', action='store_true', help='Build the experimental 8-pixel dialogue-font variant')
parser.add_argument('--rom', type=Path, required=True)
parser.add_argument('--output-dir', type=Path)
args = parser.parse_args()

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = args.output_dir or ROOT / 'build'
OUTPUT.mkdir(parents=True, exist_ok=True)
source = args.rom.resolve()
original = source.read_bytes()
assert hashlib.sha256(original).hexdigest() == '58b7ad86fae87e572e8474eb935ecda165e71c741096cd687f96bed96fbba05c'
out = bytearray(original)
if args.narrow:
    # Keep the near-branch font hook separate from the growing dialogue pool.
    out += b'\xFF' * (0x410000-len(out))
base = 0x31CD4C
translations = json.loads((ROOT / 'translations' / 'dialogue-en.json').read_text('utf-8'))
manifest = []

def encode(text):
    # The original name-entry keyboard contains fullwidth Latin letters.
    assert not any(c in re.sub(r'\{N1\}', '', text) for c in '{}'), 'Unknown placeholder'
    output = bytearray()
    for fragment in re.split(r'(\{N1\})', text):
        if fragment == '{N1}':
            output += b'N1'
        else:
            converted = ''.join('　' if c == ' ' else '’' if c == "'" else
                                chr(ord(c)+0xFEE0) if '!' <= c <= '~' else c for c in fragment)
            output += converted.encode('cp932', errors='strict')
    return bytes(output)

for scene, messages in translations.items():
    index = int(scene)
    table_offset = base + index * 4
    previous = struct.unpack_from('<I', original, table_offset)[0] + base
    headerless = original[previous:previous+2] != b'FF'
    next_scene = struct.unpack_from('<I', original, table_offset+4)[0] + base
    original_scene = original[previous:next_scene].rstrip(b'\0')
    if original_scene.endswith(b'WWEE'):
        scene_ending = b'WWEE'
    elif original_scene.endswith(b'EE'):
        scene_ending = b'EE'
    else:
        raise AssertionError('Unsupported scene ending')
    expected_speakers = [match.group(1)[0] for match in re.finditer(rb'FF([\x00-\x3f])\x00', original_scene)]
    translated_speakers = [message['speaker'] for message in messages if message['speaker'] is not None]
    if expected_speakers:
        # A null speaker preserves the inherited portrait until an inline FF command.
        assert expected_speakers == translated_speakers, f'Speaker mismatch in scene {scene}'
    else:
        assert all(message['speaker'] is None for message in messages), f'Unexpected speaker in headerless scene {scene}'
    # Refuse to replace scenes containing commands not supported by this builder.
    position = 0
    name_commands = 0
    while position < len(original_scene):
        pair = original_scene[position:position+2]
        if pair == b'FF':
            position += 4
        elif pair in (b'KK', b'PP', b'WW', b'EE'):
            position += 2
        elif pair == b'N1':
            name_commands += 1
            position += 2
        else:
            assert 0x81 <= pair[0] <= 0x9F or 0xE0 <= pair[0] <= 0xEF, f'Unknown command in scene {scene}'
            assert len(pair.decode('cp932', errors='strict')) == 1
            position += 2
    assert sum(message['text'].count('{N1}') for message in messages) == name_commands, 'Name command count changed'
    while len(out) % 4:
        out.append(0xFF)
    start = len(out)
    payload = bytearray()
    for number, message in enumerate(messages):
        if message['speaker'] is not None:
            payload += b'FF' + struct.pack('<H', message['speaker'])
        line_width = 24 if args.narrow else 12
        paragraphs = message['text'].split('\n\n')
        for paragraph_number, paragraph in enumerate(paragraphs):
            lines = []
            for hard_line in paragraph.splitlines():
                lines.extend(textwrap.wrap(hard_line, width=line_width, break_long_words=False, break_on_hyphens=False))
            # Reserve 12 character cells for the runtime name. Keep it on its own line.
            assert all(len(line.replace('{N1}', 'X'*12)) <= line_width for line in lines)
            assert all('{N1}' not in line or line.strip() in ('{N1}', '{N1}.', '{N1}!') for line in lines)
            for i, line in enumerate(lines):
                payload += encode(line)
                if i < len(lines)-1:
                    payload += b'KK' if i % 2 == 0 else b'PP'
            if paragraph_number < len(paragraphs)-1:
                payload += b'PP'
        payload += scene_ending if number == len(messages)-1 else b'PP'
    out += payload
    struct.pack_into('<I', out, table_offset, start-base)
    manifest.append({'scene': index, 'table_offset': hex(table_offset), 'old_offset': hex(previous),
                     'new_offset': hex(start), 'bytes': len(payload), 'messages': len(messages)})

code_offsets = set()
if args.narrow:
    # Expand the scene renderer's 28-byte temporary string area to 60 bytes.
    # Shift every following stack local by 32 bytes; outgoing arguments stay put.
    stack_locals = [0xFAA8, 0xFAAE, 0xFAB6, 0xFAC2, 0xFC20, 0xFC22,
                    0xFC24, 0xFC26, 0xFC2A, 0xFC2E, 0xFC3A, 0xFC3C,
                    0xFC4C, 0xFC4E, 0xFC92, 0xFC96, 0xFCA2, 0xFCA6]
    for p in stack_locals + [0xFAA2, 0xFCB4]:
        instruction = struct.unpack_from('<H', original, p)[0]
        assert (instruction & 0xF000) in (0x9000, 0xA000, 0xB000)
        struct.pack_into('<H', out, p, instruction + 8)
        code_offsets.update((p, p+1))
    # Select the built-in narrow font only for appended translated scenes.
    # Original scenes below 0x08400000 keep the original font mode.
    hook = 0x400000
    assert len(out) <= 0x7F0000, 'Dialogue allocation overlaps UI pool'
    instructions = [0x68EA, 0x0D92, 0x2A21, 0xD101, 0x2201, 0xE000, 0x2200, 0x2301, 0x4770]
    hook_bytes = struct.pack('<'+'H'*len(instructions), *instructions)
    assert all(value == 255 for value in out[hook:hook+len(hook_bytes)])
    out[hook:hook+len(hook_bytes)] = hook_bytes
    call = 0xFCAA
    assert original[call:call+4] == bytes.fromhex('00220123')
    relative = hook-(call+4)
    assert relative % 2 == 0 and -(1<<22) <= relative < (1<<22)
    struct.pack_into('<HH', out, call, 0xF000 | ((relative >> 12) & 0x7FF),
                     0xF800 | ((relative >> 1) & 0x7FF))
    code_offsets.update(range(call, call+4))
    # HH (highlighted item names) originally branched to FCAC, the second
    # instruction of the pair replaced by the font-selector BL at FCAA.
    # Keep HH's narrow mode and resume at FCAE, past the entire selector.
    hh_hook = 0x400100
    hh_instructions = [0x4672,0x3210,0x4696,0x2201,0x2301,0x4770]
    hh_bytes = struct.pack('<'+'H'*len(hh_instructions),*hh_instructions)
    assert all(value == 255 for value in out[hh_hook:hh_hook+len(hh_bytes)])
    out[hh_hook:hh_hook+len(hh_bytes)] = hh_bytes
    hh_call = 0xFC9A
    assert original[hh_call:hh_call+4] == bytes.fromhex('012206e0')
    hh_relative = hh_hook-(hh_call+4)
    struct.pack_into('<HH',out,hh_call,0xF000|((hh_relative>>12)&0x7FF),
                     0xF800|((hh_relative>>1)&0x7FF))
    code_offsets.update(range(hh_call,hh_call+4))

# Round to the next standard cartridge size.
out += b'\xFF' * ((8*1024*1024) - len(out))
allowed = {base+int(scene)*4+j for scene in translations for j in range(4)}
allowed |= code_offsets
assert all(a == b or i in allowed for i, (a, b) in enumerate(zip(original, out)))
assert source.read_bytes() == original
stem = 'Beyblade-AHEJ-English-opening-' + ('NARROW-' if args.narrow else '') + 'EXPERIMENTAL'
output = OUTPUT / (stem+'.gba')
output.write_bytes(out)

# IPS includes only changed bytes and the appended scenes, not the full ROM.
patch = bytearray(b'PATCH')
for record in manifest:
    p = int(record['table_offset'], 16)
    patch += p.to_bytes(3, 'big') + (4).to_bytes(2, 'big') + out[p:p+4]
for p in sorted(code_offsets):
    patch += p.to_bytes(3, 'big') + (1).to_bytes(2, 'big') + out[p:p+1]
for p in range(len(original), len(out), 65535):
    chunk = out[p:min(p+65535, len(out))]
    if all(v == 255 for v in chunk):
        patch += p.to_bytes(3, 'big') + b'\0\0' + len(chunk).to_bytes(2, 'big') + b'\xFF'
    else:
        patch += p.to_bytes(3, 'big') + len(chunk).to_bytes(2, 'big') + chunk
patch += b'EOF'
(OUTPUT / (stem+'.ips')).write_bytes(patch)
(OUTPUT / ('narrow-manifest.json' if args.narrow else 'sample-manifest.json')).write_text(json.dumps({'status': 'experimental_requires_emulator_validation',
    'rom_sha256': hashlib.sha256(out).hexdigest(), 'scenes': manifest}, indent=2), encoding='utf-8')
print(json.dumps(manifest, indent=2))
