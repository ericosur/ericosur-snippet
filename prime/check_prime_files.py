#!/usr/bin/env python3
'''Check that all data files referenced in setting.json actually exist.'''

import argparse
import json
import sys
from pathlib import Path

DEFAULT_CONFIG = Path(__file__).resolve().parent / 'setting.json'


def resolve_prime_path(config: dict) -> Path:
    ''' full_prime_path overrides base_prime_path, matching store/get_config.py '''
    full_prime_path = config.get('full_prime_path')
    if full_prime_path and Path(full_prime_path).exists():
        return Path(full_prime_path)
    return Path.home() / config['base_prime_path']


def check_files(config_path: Path) -> list[Path]:
    ''' return the list of files referenced in the config that do not exist '''
    with config_path.open('r', encoding='utf8') as f:
        config = json.load(f)

    prime_path = resolve_prime_path(config)
    missing: list[Path] = []
    for value in config.values():
        if not isinstance(value, dict):
            continue
        for filename in value.values():
            if not isinstance(filename, str):
                continue
            full_path = prime_path / filename
            if not full_path.exists():
                missing.append(full_path)
    return missing


def main() -> None:
    ''' parse command-line arguments and check the referenced files '''
    parser = argparse.ArgumentParser(
        description='Check that all data files referenced in setting.json exist.'
    )
    parser.add_argument('config', nargs='?', type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()

    missing = check_files(args.config)
    if not missing:
        print('all files exist')
        return

    print(f'missing {len(missing)} file(s):')
    for path in missing:
        print(f'  {path}')
    sys.exit(1)


if __name__ == '__main__':
    main()
