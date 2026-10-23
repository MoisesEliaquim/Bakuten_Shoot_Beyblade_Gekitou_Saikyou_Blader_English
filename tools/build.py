"""Build and verify the experimental translation using an external original ROM."""
import argparse
from pathlib import Path
import subprocess
import sys
import json

parser = argparse.ArgumentParser()
parser.add_argument('--rom', type=Path, required=True)
parser.add_argument('--output-dir', type=Path)
args = parser.parse_args()
tools = Path(__file__).resolve().parent
output = (args.output_dir or tools.parent / 'build').resolve()
rom = args.rom.resolve()
stem = json.loads((tools.parent / 'project.json').read_text('utf-8'))['artifact_stem']
common = ['--rom', str(rom), '--output-dir', str(output)]
for script, extra in [('build_dialogue.py', ['--narrow']),
                       ('build_ui.py', ['--output-stem', stem]),
                       ('verify_patch.py', [stem])]:
    subprocess.run([sys.executable, str(tools / script), *common, *extra], check=True)
print(f'Built and verified: {output / (stem+".ips")}')
