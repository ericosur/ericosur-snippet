'''
get_config.py provides class GetConfig
'''

import os
import socket
import sys
from typing import Any

try:
    from .load_myutil import (  # type: ignore[reportAttributeAccessIssue]
        do_nothing,  # type: ignore[reportAttributeAccessIssue]
        get_home,  # type: ignore[reportAttributeAccessIssue]
        is_file,  # type: ignore[reportAttributeAccessIssue]
        prime_dir,  # type: ignore[reportAttributeAccessIssue]
        read_setting,  # type: ignore[reportAttributeAccessIssue]
    )
except ImportError:
    print(f'[FAIL] MUST not run {__file__} directly')
    sys.exit(1)

__VERSION__ = "2026.09.15"
LOCAL_DEBUG = True
if LOCAL_DEBUG:
    try:
        from madlog import logd  # type: ignore[reportAttributeAccessIssue]
    except ImportError:
        logd = print
else:
    logd = do_nothing


class GetConfig:
    ''' a wrapper class to load config for primes '''
    allkeys = ("txt", "pickle", "u32", "u64", "max", "count")

    def __init__(self, conf: str = "setting.json") -> None:
        self.conf = conf
        settings = self.__read_json_conf()
        if settings is None:
            print(f'[FAIL] {__file__}: fail to read settings')
            sys.exit(1)
        self.d: dict[str, Any] = settings
        self.base_path: str = self.d['base_prime_path']
        self.key: str | None = None
        active = self._resolve_active_profile()
        # sizes is now a dict: {size_name: [available_formats]}
        self._active_sizes: dict[str, list[str]] = active.get('sizes', {})
        self.sizes: tuple[str, ...] = tuple(self._active_sizes.keys())
        # cache resolved prime path once at init
        self._prime_path: str = self._resolve_prime_path()

    def _resolve_active_profile(self) -> dict[str, Any]:
        ''' Return the active profile dict using the same priority as get_full_prime_path:
            1. master_profile  2. hostname_map  3. default_profile
        '''
        profiles: dict = self.d.get('profiles', {})
        hostname_map: dict = self.d.get('hostname_map', {})

        for name in [
            self.d.get('master_profile', '').strip() or None,
            hostname_map.get(socket.gethostname()),
            self.d.get('default_profile', '').strip() or None,
        ]:
            if name and name in profiles:
                logd(f'active profile: {name!r}')
                return profiles[name]
        return {}

    def __read_json_conf(self) -> dict[str, Any] | None:
        ''' read json config '''
        self.conf = os.path.join(prime_dir, self.conf)
        logd(f'reading settings from {self.conf}')
        if not is_file(self.conf):
            print(f'[FAIL] {__file__}: settings file not found: {self.conf}')
            return None
        try:
            sett = read_setting(self.conf)
            return sett
        except FileNotFoundError as e:
            print(f'[FAIL] {__file__}: fail to read settings: {e}')
            return None

    def do_tests(self) -> None:
        ''' test all path and file is available '''
        for k in self.sizes:
            cs = self.d[k]
            assert cs is not None
            msg = f'numbers of primes: {cs.get("count"):,}, max prime is {cs.get("max"):,}'
            print(msg)
            for fmt in self._active_sizes.get(k, []):
                filename = cs.get(fmt)
                if not filename:
                    print(f'[WARN] no filename for {k}/{fmt} in config')
                    continue
                fn = os.path.join(self._prime_path, filename)
                print(fn)
                assert os.path.exists(fn)

    def set_configkey(self, key: str) -> None:
        ''' set config key '''
        if key not in self.sizes:
            raise ValueError(f"[FAIL] GetConfig has no such key: {key}")
        self.key = key

    def get_config(self, key: str | None = None) -> dict[str, Any] | None:
        ''' input key, get config group '''
        if key is None:
            key = self.key
        if key is None:
            raise ValueError('[FAIL] no configuration key selected')
        self.set_configkey(key)
        return self.d.get(key)

    def get_full_path(self, item: str) -> str:
        '''
        item in [txt, pickle, u32, u64, ...]
        Returns the full absolute path to the file.
        Raises KeyError  if item is not a known format key.
        Raises ValueError if item is not declared available for this size in the active profile.
        Raises FileNotFoundError if the file does not exist on disk.
        '''
        if item not in self.allkeys:
            raise KeyError(f"[FAIL] get_full_path: unknown format key: {item!r}")
        assert self.key is not None
        available = self._active_sizes.get(self.key, [])
        if item not in available:
            raise ValueError(
                f"[FAIL] get_full_path: format {item!r} not available "
                f"for size {self.key!r} in active profile"
            )
        full_ppath = self.get_full_prime_path()
        p = os.path.join(full_ppath, self.d[self.key][item])
        if not os.path.exists(p):
            raise FileNotFoundError(f"[FAIL] get_full_path: file not found: {p}")
        return p

    def get_available_formats(self, size: str | None = None) -> list[str]:
        ''' Return the list of available format keys for the given size (or current key). '''
        key = size or self.key
        if key is None:
            raise ValueError('[FAIL] get_available_formats: no size selected')
        return list(self._active_sizes.get(key, []))

    def _resolve_prime_path(self) -> str:
        ''' Resolve prime data directory with priority:
            1. master_profile (manual override, highest)
            2. hostname_map   (auto-detect by hostname)
            3. default_profile (fallback profile)
            4. $HOME / base_prime_path (last resort)
        Called once at init; result is cached in self._prime_path.
        '''
        profiles: dict = self.d.get('profiles', {})
        hostname_map: dict = self.d.get('hostname_map', {})

        def _try_profile(name: str) -> str | None:
            p = profiles.get(name, {}).get('full_prime_path', '')
            if p and os.path.exists(p):
                logd(f'_resolve_prime_path: profile={name!r} -> {p}')
                return p
            return None

        # 1. master_profile
        master = self.d.get('master_profile', '').strip()
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
        default = self.d.get('default_profile', '').strip()
        if default:
            result = _try_profile(default)
            if result:
                return result

        # 4. $HOME / base_prime_path
        the_path = os.path.join(get_home(), self.base_path)
        logd(f'_resolve_prime_path: fallback -> {the_path}')
        if os.path.exists(the_path):
            return the_path
        raise FileNotFoundError(f'[FAIL] GetConfig: path not found: {the_path}')

    def get_full_prime_path(self) -> str:
        ''' Return the resolved prime data directory (cached at init). '''
        return self._prime_path

    def get_base_path(self) -> str:
        ''' Return base_prime_path value from config. '''
        return self.base_path

    def _get_data_path(self, size: str) -> tuple[str, str]:
        '''Return (txt, pickle) paths for a data set.
        Raises ValueError if either format is not declared available in the active profile.
        '''
        available = self._active_sizes.get(size, [])
        for fmt in ('txt', 'pickle'):
            if fmt not in available:
                raise ValueError(
                    f"[FAIL] _get_data_path: format {fmt!r} not available "
                    f"for size {size!r} in active profile"
                )
        config = self.d[size]
        txtfn = os.path.join(self._prime_path, config['txt'])
        pfn = os.path.join(self._prime_path, config['pickle'])
        return txtfn, pfn

if __name__ == "__main__":
    print(f'{__file__}\nversion: {__VERSION__} is a module only')
