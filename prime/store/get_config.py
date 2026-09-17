'''
get_config.py provides class GetConfig
'''

import os
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
    sizes = ("big", "large", "h119", "h422")
    allkeys = ("txt", "pickle", "compress_pickle", "u32", "max", "num")

    def __init__(self, conf: str = "setting.json") -> None:
        self.home = get_home()
        self.conf = conf
        settings = self.__read_json_conf()
        if settings is None:
            print(f'[FAIL] {__file__}: fail to read settings')
            sys.exit(1)
        self.d: dict[str, Any] = settings
        self.ppath: str = self.d['prime_path']
        self.key: str | None = None

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

        assert os.path.exists(self.get_full_ppath())

        for k in self.sizes:
            cs = self.d[k]
            assert cs is not None
            msg = f'numbers of primes: {cs.get("num"):,}, max prime is {cs.get("max"):,}'
            print(msg)
            for i in ["txt", "pickle", "compress_pickle"]:
                fn = os.path.join(self.get_full_ppath(), cs.get(i))
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
        ''' give item like txt, pickle, compress_pick, num, max '''
        if item not in self.allkeys:
            raise ValueError(f"[FAIL] GetConfig has no such key: {item}")
        if self.key is None:
            raise ValueError(f'[FAIL] no configuration key selected: {self.key}')
        p = os.path.join(get_home(), self.ppath, self.d[self.key][item])
        return p

    def get_full_ppath(self) -> str:
        ''' prime path '''
        return os.path.join(get_home(), self.ppath)

    def get_ppath(self) -> str:
        ''' prime path '''
        return self.ppath

    def get_big_config(self) -> dict[str, Any] | None:
        ''' get prime data file path '''
        return self.get_config("big")

    def get_large_config(self) -> dict[str, Any] | None:
        ''' get prime data file path '''
        return self.get_config("large")

    def get_h119_config(self) -> dict[str, Any] | None:
        ''' get prime data file path '''
        return self.get_config("h119")

    def get_h422_config(self) -> dict[str, Any] | None:
        ''' get prime data file path '''
        return self.get_config("h422")

    def _get_data_path(self, size: str) -> tuple[str, str, str]:
        '''Return text, pickle, and compressed-pickle paths for a data set.'''
        config = self.d[size]
        ppath = self.get_full_ppath()
        txtfn = os.path.join(ppath, config['txt'])
        pfn = os.path.join(ppath, config['pickle'])
        pzfn = os.path.join(ppath, config['compress_pickle'])
        return txtfn, pfn, pzfn

    def get_largedata_path(self) -> tuple[str, str, str]:
        ''' get large prime data file path '''
        return self._get_data_path('large')

    def get_bigdata_path(self) -> tuple[str, str, str]:
        ''' get big prime data file path '''
        return self._get_data_path('big')

if __name__ == "__main__":
    print(f'{__file__}\nversion: {__VERSION__} is a module only')
