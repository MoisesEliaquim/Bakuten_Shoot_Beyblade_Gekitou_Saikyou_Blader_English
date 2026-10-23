"""Read-only text analysis for Beyblade AHEJ. Does not modify the ROM."""
from pathlib import Path
import hashlib
import json
import re
import struct

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--rom', type=Path, required=True)
parser.add_argument('--output-dir', type=Path)
args = parser.parse_args()
ROOT = args.output_dir or Path(__file__).resolve().parents[1] / 'build' / 'extracted'
ROOT.mkdir(parents=True, exist_ok=True)
ROM = args.rom.resolve()
data = ROM.read_bytes()
assert data[0xAC:0xB0] == b'AHEJ', 'Unexpected game'
assert hashlib.sha256(data).hexdigest() == '58b7ad86fae87e572e8474eb935ecda165e71c741096cd687f96bed96fbba05c'

# These are observed byte pairs, not yet confirmed engine semantics.
commands = {b'KK', b'PP', b'WW', b'EE', b'FF'}
entries = []
for match in re.finditer(rb'FF([\x00-\x3f])\x00', data):
    start = match.end()
    pos = start
    tokens = []
    japanese = 0
    ended = False
    while pos + 2 <= len(data) and pos - start < 8192:
        pair = data[pos:pos+2]
        if pair in commands:
            tokens.append({'offset': f'0x{pos:08X}', 'command': pair.decode('ascii')})
            pos += 2
            if pair in {b'FF', b'EE'}:
                ended = True
                break
            continue
        try:
            char = pair.decode('cp932', errors='strict')
        except UnicodeDecodeError:
            break
        if len(char) != 1 or not (0x81 <= pair[0] <= 0x9F or 0xE0 <= pair[0] <= 0xEF):
            break
        japanese += bool(re.search('[\u3040-\u30ff\u4e00-\u9fff]', char))
        if tokens and 'text' in tokens[-1]:
            tokens[-1]['text'] += char
        else:
            tokens.append({'offset': f'0x{pos:08X}', 'text': char})
        pos += 2
    if not ended or japanese < 2:
        continue
    entries.append({
        'offset': f'0x{start:08X}',
        'header_offset': f'0x{match.start():08X}',
        'speaker_id_candidate': match.group(1)[0],
        'byte_length': pos-start,
        'original_hex': data[start:pos].hex(),
        'original': ''.join(t.get('text', '<'+t.get('command', '')+'>') for t in tokens),
        'tokens': tokens,
        'translation': '',
        'status': 'extracted_engine_semantics_unverified',
    })

targets = {int(e['header_offset'], 16): e for e in entries}
references = {offset: [] for offset in targets}
for pos in range(0, len(data)-3, 4):
    target = struct.unpack_from('<I', data, pos)[0] - 0x08000000
    if target in references:
        references[target].append(f'0x{pos:08X}')
for offset, entry in targets.items():
    entry['aligned_pointer_candidates'] = references[offset]

result = {'rom': ROM.name, 'sha256': hashlib.sha256(data).hexdigest(),
          'notes': 'Heuristic extraction. Command meanings and pointer roles require engine verification.',
          'entries': entries}
(ROOT / 'dialogue-extracted.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
(ROOT / 'dialogue-readable.txt').write_text('\n\n'.join(
    f"{e['offset']} speaker?={e['speaker_id_candidate']}\n{e['original']}" for e in entries), encoding='utf-8')
print(json.dumps({'entries': len(entries), 'with_pointer_candidates': sum(bool(e['aligned_pointer_candidates']) for e in entries)}, indent=2))
