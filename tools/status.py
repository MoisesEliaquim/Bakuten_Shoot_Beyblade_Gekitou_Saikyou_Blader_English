"""Report counts directly from the editable project sources; no ROM required."""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
project = json.loads((root / 'project.json').read_text('utf-8'))
dialogue = json.loads((root / 'translations/dialogue-en.json').read_text('utf-8'))
menus = json.loads((root / 'translations/menus-en.json').read_text('utf-8'))
battle = json.loads((root / 'translations/battle-en.json').read_text('utf-8'))
print(json.dumps({
    'version': project['version'],
    'translated_speeches': sum(map(len, dialogue.values())),
    'translated_scenes': len(dialogue),
    'translated_ui_strings': len(menus),
    'translated_battle_resources': len(battle),
    'translated_battle_pages': sum(len(e['english_pages']) for e in battle),
    'scene_ids': list(map(int, dialogue)),
    'runtime_name_placeholders': sum(message['text'].count('{N1}') for messages in dialogue.values() for message in messages)
}, indent=2))
