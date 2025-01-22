#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
from /etc/os-release to get OS info (usu. ubuntu)
'''

import os
import re
import sys
from typing import Union, Dict
try:
    from rich import print as pprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = pprint if USE_RICH else print

class OSRelease():
    ''' info from /etc/os-release (ubuntu) '''
    FN = '/etc/os-release'
    def __init__(self):
        self.info = self.read_os_release()

    def read_os_release(self) -> Union[Dict[str, str], None]:
        ''' read /etc/os-release '''
        fn = self.FN
        if not os.path.exists(fn):
            prt(f'file not found: {fn}')
            return None
        ret = {}
        with open(fn, 'rt', encoding='utf-8') as f:
            for ln in f.readlines():
                ln = ln.strip()
                m = re.search(r'^(\w+)="?([^"]+)"?$', ln)
                if m:
                    k, v = m.group(1), m.group(2)
                    ret[k] = v
                else:
                    prt(f'OSRelease: no match: {ln}')
        return ret

    def is_ubutnu(self) -> Union[bool, None]:
        ''' true if ubuntu '''
        return None if self.info is None else self.info.get('ID') == 'ubuntu'

    def match_ubuntu_version(self, ver: str) -> Union[bool, None]:
        ''' true if ubuntu version matches '''
        return None if self.info is None else self.info.get("VERSION_ID") == ver

    def is_ubuntu_1804(self) -> Union[bool, None]:
        ''' true if ubuntu 18.04, none if no info retrieved '''
        return None if self.info is None else self.info.get('VERSION_ID') == "18.04"

    def is_ubuntu_2204(self) -> Union[bool, None]:
        ''' true if ubuntu 18.04, none if no info retrieved '''
        return None if self.info is None else self.info.get('VERSION_ID') == "18.04"

    def is_ge_ubuntu(self, ver: float) -> Union[bool, None]:
        ''' true if number >= ver (version taken as float) '''
        if self.info is None:
            return None
        try:
            current_version = float(self.info.get('VERSION_ID', 0))
            return current_version >= ver
        except ValueError:
            prt(f'Invalid version format: {self.info.get("VERSION_ID")}')
            return None

    def get_version_float(self) -> Union[float, None]:
        ''' return version as float '''
        if self.info is None:
            return None
        try:
            return float(self.info.get("VERSION_ID"))
        except ValueError:
            prt(f'Invalid version format: {self.info.get("VERSION_ID")}')
            return None

def is_ubuntu1804() -> Union[bool, None]:
    ''' true if ubuntu 18.04'''
    obj = OSRelease()
    return obj.is_ubuntu_1804()

def test():
    ''' test '''
    obj = OSRelease()
    prt(obj.info)
    prt("is_ubuntu:", obj.is_ubutnu())
    prt("is_ubuntu 18.04:", obj.is_ubuntu_1804())
    prt("match_ubuntu_version 22.04:", obj.match_ubuntu_version("22.04"))
    prt("is_ge_ubuntu 22.04:", obj.is_ge_ubuntu(22.04))
    prt("get_version_float:", obj.get_version_float())

if __name__ == "__main__":
    if len(sys.argv)>1 and sys.argv[1] == "test":
        test()
    else:
        prt(f'{sys.argv[0]} is a module, not a standalone script')
        sys.exit(1)
