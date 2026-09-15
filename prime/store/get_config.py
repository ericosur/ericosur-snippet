'''
get_config.py provides class GetConfig
'''

import os
import sys

from .load_myutil import (  # type: ignore[reportAttributeAccessIssue]
    get_home,  # type: ignore[reportAttributeAccessIssue]
    read_setting,  # type: ignore[reportAttributeAccessIssue]
)

__VERSION__ = "2026.09.15"

class GetConfig:
    ''' a wrapper class to load config for primes '''
    sizes = ("small", "big", "large", "h119", "h422")
    allkeys = ("txt", "pickle", "compress_pickle", "max", "num")

    def __init__(self, conf="setting.json"):
        self.home = get_home()
        self.conf = conf
        self.d = read_setting(self.conf)
        if self.d is None:
            print(f'[FAIL] {__file__}: fail to read settings')
            sys.exit(1)
        self.ppath = self.d['prime_path']
        self.key = None

    def do_tests(self):
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

    def set_configkey(self, key):
        ''' set config key '''
        if key not in self.sizes:
            raise ValueError(f"[FAIL] GetConfig has no such key: {key}")
        self.key = key

    def get_config(self, key=None):
        ''' input key, get config group '''
        if key is None:
            key = self.key
        self.set_configkey(key)
        return self.d.get(key)

    def get_full_path(self, item):
        ''' give item like txt, pickle, compress_pick, num, max '''
        if item not in self.allkeys:
            raise ValueError("[FAIL] GetConfig has no such key")
        # print(self.ppath)
        # print(self.d)
        # print(self.d[self.key])
        p = os.path.join(get_home(), self.ppath, self.d[self.key][item])
        # print(p)
        return p

    def get_full_ppath(self):
        ''' prime path '''
        return os.path.join(get_home(), self.ppath)

    def get_ppath(self):
        ''' prime path '''
        return self.ppath

    def get_small_config(self):
        ''' get prime data file path '''
        self.set_configkey("small")
        return self.get_config()

    def get_big_config(self):
        ''' get prime data file path '''
        self.set_configkey("big")
        return self.get_config()

    def get_large_config(self):
        ''' get prime data file path '''
        self.set_configkey("large")
        return self.get_config()

    def get_h119_config(self):
        ''' get prime data file path '''
        self.set_configkey("h119")
        return self.get_config()

    def get_h422_config(self):
        ''' get prime data file path '''
        self.set_configkey("h422")
        return self.get_config()

    def get_largedata_path(self):
        ''' get large prime data file path '''
        pth = self.d['prime_path']
        txtfn = os.path.join(get_home(), pth, self.d['prime_large'])
        pfn = os.path.join(get_home(), pth, self.d['pickle_large'])
        pzfn = os.path.join(get_home(), pth, self.d['pickle_large_compress'])
        return txtfn, pfn, pzfn

    def get_bigdata_path(self):
        ''' get large prime data file path '''
        txtfn = os.path.join(get_home(), self.ppath, self.d['prime_big'])
        pfn = os.path.join(get_home(), self.ppath, self.d['pickle_big'])
        pzfn = os.path.join(get_home(), self.ppath, self.d['pickle_big_compress'])
        return txtfn, pfn, pzfn

if __name__ == "__main__":
    print(f'{__file__}\nversion: {__VERSION__} is a module only')
