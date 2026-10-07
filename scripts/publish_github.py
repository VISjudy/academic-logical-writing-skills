#!/usr/bin/env python3
"""Publish this prepared package to a NEW repository; preview only by default.

Requires locally installed Git and authenticated GitHub CLI (gh). Does not read
or print tokens, change global configuration, modify the original repository,
overwrite an existing destination repository, force-push, or delete anything.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OWNER = 'VISjudy'
REPO = 'academic-logical-writing-skills'
TARGET = f'{OWNER}/{REPO}'
DESCRIPTION = 'Academic writing skills: proposal logic, critical review, bilingual drafting and research-writing workflows.'


def command(args: list[str], *, required: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        args, cwd=ROOT, text=True, encoding='utf-8', errors='replace',
        capture_output=True, check=False,
    )
    if required and result.returncode:
        # These commands never request token values. Keep errors visible for recovery.
        raise RuntimeError(f'Command failed ({args[0]} {args[1]}):\n{result.stderr.strip()}')
    return result


def validated_files() -> list[str]:
    manifest = json.loads((ROOT / 'PACKAGE_FILES.json').read_text(encoding='utf-8'))
    if manifest.get('target_repository') != TARGET:
        raise RuntimeError('Unexpected target repository in package manifest.')
    paths: list[str] = []
    for relative, expected in manifest['files_sha256'].items():
        rel = Path(relative)
        if rel.is_absolute() or '..' in rel.parts or '.git' in rel.parts:
            raise RuntimeError(f'Unsafe manifest path: {relative}')
        path = ROOT / rel
        if path.is_symlink() or not path.is_file() or ROOT not in path.resolve().parents:
            raise RuntimeError(f'Missing or unsafe file: {relative}')
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f'Package file changed: {relative}. Review it before publishing.')
        paths.append(relative)
    paths.append('PACKAGE_FILES.json')
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', action='store_true', help='Actually create and push the new repository.')
    parser.add_argument('--visibility', choices=('public', 'private'), help='Required for publication; no default visibility.')
    args = parser.parse_args()
    if args.publish and args.visibility is None:
        parser.error('--publish requires an explicit --visibility public or private')
    try:
        files = validated_files()
        print(f'Target: {TARGET}')
        print(f'Packaged files: {len(files)}; original repository is unchanged.')
        if not args.publish:
            print('PREVIEW ONLY: no network requests or file changes were performed.')
            print('After review, run: python scripts/publish_github.py --publish --visibility public')
            print('The publication run will validate gh identity, refuse existing repositories,')
            print('create a new local main branch, create the remote repository, push and verify its SHA.')
            return 0
        for program in ('git', 'gh'):
            if shutil.which(program) is None:
                raise RuntimeError(f'{program} is not installed/on PATH. No remote operation was performed.')
        if (ROOT / '.git').exists():
            raise RuntimeError('This package already has .git. Refusing to reinitialize or overwrite; inspect previous progress.')
        parent = command(['git', 'rev-parse', '--show-toplevel'], required=False)
        if parent.returncode == 0:
            raise RuntimeError('Package is inside an existing Git worktree. Extract to a separate directory first.')
        identity = command(['gh', 'api', '--hostname', 'github.com', 'user', '--jq', '.login']).stdout.strip()
        if identity.casefold() != OWNER.casefold():
            raise RuntimeError(f'gh is authenticated as {identity!r}, not {OWNER}. Stop and select the correct account locally.')
        exists = command(['gh', 'api', '--hostname', 'github.com', f'repos/{TARGET}', '--jq', '.full_name'], required=False)
        if exists.returncode == 0:
            raise RuntimeError('Target repository already exists. Refusing to overwrite or append; inspect it first.')
        if '404' not in exists.stderr:
            raise RuntimeError(f'Could not safely determine repository availability:\n{exists.stderr.strip()}')
        validation = command([sys.executable, str(ROOT / 'scripts' / 'validate_all.py')])
        print(validation.stdout, end='')
        command(['git', 'init', '-b', 'main'])
        command(['git', '-c', 'core.autocrlf=false', 'add', '--', *files])
        command([
            'git', '-c', f'user.name={OWNER}',
            '-c', f'user.email=86459381+{OWNER}@users.noreply.github.com',
            '-c', 'commit.gpgsign=false', 'commit', '-m',
            'Initialize dedicated academic-logical-writing-skills repository',
        ])
        local_sha = command(['git', 'rev-parse', 'HEAD']).stdout.strip()
        created = command(['gh', 'repo', 'create', TARGET, f'--{args.visibility}', '--description', DESCRIPTION])
        print(created.stdout, end='')
        command(['git', 'remote', 'add', 'origin', f'https://github.com/{TARGET}.git'])
        git_auth = ['git', '-c', 'credential.https://github.com.helper=', '-c', 'credential.https://github.com.helper=!gh auth git-credential']
        command(git_auth + ['push', '--set-upstream', 'origin', 'main'])
        remote_sha = command([
            'gh', 'api', '--hostname', 'github.com', f'repos/{TARGET}/git/ref/heads/main', '--jq', '.object.sha'
        ]).stdout.strip()
        if remote_sha != local_sha:
            raise RuntimeError(f'Pushed, but commit verification disagrees: local={local_sha}, remote={remote_sha}')
        print('PUBLISHED AND VERIFIED')
        print(f'https://github.com/{TARGET}')
        print(f'Commit: {remote_sha}')
        print('Original source repository, PR and branch were not modified.')
        return 0
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as exc:
        print(f'STOPPED: {exc}', file=sys.stderr)
        print('No rollback, deletion or force-push was attempted. Some earlier steps may have completed; inspect before retrying.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
