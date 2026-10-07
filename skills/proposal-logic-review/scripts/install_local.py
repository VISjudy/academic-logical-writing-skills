#!/usr/bin/env python3
"""Install the complete skill locally without overwriting existing files.

Standard library only. No downloads, credentials, registry changes, AGENTS.md
edits, or config.toml edits. Run in the same OS/user environment as Codex.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    source = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--destination', type=Path,
        default=Path.home() / '.agents' / 'skills' / 'proposal-logic-review',
        help='Full destination directory; default: ~/.agents/skills/proposal-logic-review',
    )
    args = parser.parse_args()
    raw_destination = args.destination.expanduser()
    destination = raw_destination.resolve()
    if destination == source or source in destination.parents:
        print('Refusing to install into the source tree.', file=sys.stderr)
        return 2
    if raw_destination.exists() or raw_destination.is_symlink():
        print(f'Destination already exists; no files changed: {raw_destination}', file=sys.stderr)
        print('Compare the existing skill before explicitly choosing a backup or replacement.', file=sys.stderr)
        return 2
    checked = subprocess.run(
        [sys.executable, str(source / 'scripts' / 'validate_package.py'), str(source)],
        check=False,
    )
    if checked.returncode != 0:
        print('Source package validation failed; not installed.', file=sys.stderr)
        return checked.returncode
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git'))
    except OSError as exc:
        print(f'Installation failed: {exc}', file=sys.stderr)
        print('No cleanup or replacement was attempted; inspect any partial destination before retrying.', file=sys.stderr)
        return 1
    print(f'Installed complete skill to: {destination}')
    print('In Codex, invoke $proposal-logic-review. If it is not listed, restart Codex.')
    print('File installation completed; Codex discovery and model behavior have not been tested here.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
