#!/usr/bin/env python3
"""Read-only validation of skill package structures; not model behavior tests."""
from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
entries = sorted((root / 'skills').glob('*/SKILL.md'))
if not entries:
    raise SystemExit('No skill entries found.')
failed = False
for entry in entries:
    text = entry.read_text(encoding='utf-8')
    print('Checking:', entry.parent.name, flush=True)
    if not re.match(r'\A---\n.*?^name:\s*\S+.*?^description:\s*\S+.*?^---\s*$', text, re.M | re.S):
        print('Invalid SKILL.md front matter:', entry)
        failed = True
    validator = entry.parent / 'scripts' / 'validate_package.py'
    if validator.is_file():
        result = subprocess.run([sys.executable, str(validator), str(entry.parent)], check=False)
        failed |= result.returncode != 0
print('Structure validation:', 'FAIL' if failed else 'PASS')
print('Model behavior and user-machine loading: NOT TESTED')
raise SystemExit(1 if failed else 0)
