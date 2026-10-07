#!/usr/bin/env python3
"""Validate this skill's local structure only; no model or scientific validation.

Usage:
    python scripts/validate_package.py
    python scripts/validate_package.py /path/to/proposal-logic-review

Python standard library only. Reads files without modifying them or making network
requests. It reports missing package files, broken local Markdown links, invalid
entry metadata and stray chat-only citation tokens.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

REQUIRED = (
    'SKILL.md', 'README.md', 'CHANGELOG.md', 'sources.json',
    'references/writing-playbook.md',
    'references/review-protocol.md',
    'references/urban-3dgs-case.md',
    'references/source-ledger.md',
    'templates/argument-workbook.md',
    'templates/two-page-proposal.md',
    'templates/review-report.md',
    'templates/blind-review-brief.md',
    'examples/approved-excerpts.md',
    'evals/behavior-tests.md',
    'scripts/validate_package.py',
)


def validate(root: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    local_links = 0
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f'Missing required file: {relative}')
    entry = root / 'SKILL.md'
    if entry.is_file():
        text = entry.read_text(encoding='utf-8')
        front = re.match(r'\A---\n(.*?)\n---\n', text, re.DOTALL)
        if not front:
            errors.append('SKILL.md has no leading YAML front matter.')
        else:
            data = front.group(1)
            if not re.search(r'^name: proposal-logic-review\s*$', data, re.MULTILINE):
                errors.append('SKILL.md must use name: proposal-logic-review.')
            if not re.search(r'^description:\s*\S+', data, re.MULTILINE):
                errors.append('SKILL.md requires a nonempty description.')
        if len(text.splitlines()) > 500:
            warnings.append('SKILL.md exceeds 500 lines; consider progressive disclosure.')

    md_files = list(root.rglob('*.md'))
    for file in md_files:
        text = file.read_text(encoding='utf-8')
        if any(marker in text for marker in ('filecite', 'cite', 'sandbox:/mnt/data/')):
            errors.append(f'Non-portable chat citation or sandbox link: {file.relative_to(root)}')
        for match in re.finditer(r'\[[^\]\n]+\]\(([^)\n]+)\)', text):
            target = match.group(1).strip().split(' "', 1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith('#'):
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            local_links += 1
            resolved = (file.parent / path).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f'Local link escapes package: {file.relative_to(root)} -> {target}')
                continue
            if not resolved.exists():
                errors.append(f'Broken local link: {file.relative_to(root)} -> {target}')

    source_file = root / 'sources.json'
    if source_file.is_file():
        try:
            data = json.loads(source_file.read_text(encoding='utf-8'))
            for item in data.get('sources', []):
                if not re.fullmatch(r'[0-9a-f]{64}', item.get('sha256', '')):
                    errors.append('Invalid SHA-256 value in sources.json.')
        except (json.JSONDecodeError, AttributeError, TypeError) as exc:
            errors.append(f'Invalid sources.json: {exc}')

    return {
        'scope': 'local_package_structure_only',
        'status': 'PASS' if not errors else 'FAIL',
        'markdown_files_checked': len(md_files),
        'local_links_checked': local_links,
        'errors': errors,
        'warnings': warnings,
        'model_behavior_tests': 'NOT_RUN',
        'scientific_claim_verification': 'NOT_PERFORMED',
        'host_installation': 'NOT_PERFORMED',
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(json.dumps({'status': 'FAIL', 'errors': ['Package directory not found.']}, indent=2))
        return 2
    result = validate(root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
