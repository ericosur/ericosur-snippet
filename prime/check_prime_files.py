#!/usr/bin/env python3
'''Check that all data files referenced in setting.json actually exist.'''

import argparse
import json
import socket
import sys
from pathlib import Path

DEFAULT_CONFIG = Path(__file__).resolve().parent / 'setting.json'


def resolve_prime_path(config: dict) -> Path:
    ''' Resolve prime data directory with priority:
        1. master_profile (manual override, highest)
        2. hostname_map   (auto-detect by hostname)
        3. default_profile (fallback profile)
        4. $HOME / base_prime_path (last resort)
    '''
    profiles: dict = config.get('profiles', {})
    hostname_map: dict = config.get('hostname_map', {})

    def _try_profile(name: str) -> Path | None:
        p = profiles.get(name, {}).get('full_prime_path', '')
        if p and Path(p).exists():
            return Path(p)
        return None

    # 1. master_profile
    master = config.get('master_profile', '').strip()
    if master:
        result = _try_profile(master)
        if result:
            return result

    # 2. hostname_map
    hostname = socket.gethostname()
    profile_name = hostname_map.get(hostname)
    if profile_name:
        result = _try_profile(profile_name)
        if result:
            return result

    # 3. default_profile
    default = config.get('default_profile', '').strip()
    if default:
        result = _try_profile(default)
        if result:
            return result

    # 4. $HOME / base_prime_path
    return Path.home() / config['base_prime_path']


def resolve_active_profile(config: dict) -> dict:
    ''' Return the active profile dict using the same priority as resolve_prime_path:
        1. master_profile  2. hostname_map  3. default_profile
    '''
    profiles: dict = config.get('profiles', {})
    hostname_map: dict = config.get('hostname_map', {})

    for name in [
        config.get('master_profile', '').strip() or None,
        hostname_map.get(socket.gethostname()),
        config.get('default_profile', '').strip() or None,
    ]:
        if name and name in profiles:
            return profiles[name]
    return {}


def check_files(config_path: Path) -> list[Path]:
    ''' Return the list of files (declared in the active profile) that do not exist. '''
    with config_path.open('r', encoding='utf8') as f:
        config = json.load(f)

    prime_path = resolve_prime_path(config)
    active = resolve_active_profile(config)
    # sizes: {size_name: [available_formats]}
    sizes: dict = active.get('sizes', {})

    missing: list[Path] = []
    for size_name, formats in sizes.items():
        size_def = config.get(size_name)
        if not isinstance(size_def, dict):
            print(f'[WARN] no definition for size {size_name!r} in config', file=sys.stderr)
            continue
        for fmt in formats:
            filename = size_def.get(fmt)
            if not isinstance(filename, str):
                print(f'[WARN] no filename for {size_name}/{fmt} in config', file=sys.stderr)
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
