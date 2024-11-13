#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions
	get_python_version, get_python_versions, require_python_version
'''

import sys


def get_python_version() -> str:
    ''' return version string of python '''
    minor = sys.version_info.minor
    if minor >= 10:
        print("minor >= 10, wrong value if convert to a float number"
            ", use get_python_versions instead")
        raise RuntimeError
    py_ver = ".".join(map(str, sys.version_info[:2]))
    return py_ver

def get_python_versions() -> tuple:
    ''' return python version in (major, minor) integers '''
    return (sys.version_info[0], sys.version_info[1])

def require_python_version(major, minor, debug=False) -> bool:
    ''' raise exception if not match the minimum version '''
    sys_major = sys.version_info.major
    if sys_major > major:
        return True
    if sys_major == major:
        if debug:
            print(f'{sys.version_info.minor=} vs {minor=}')
        if int(sys.version_info.minor) >= int(minor):
            return True
    return False

def need_python36() -> None:
    ''' if not python version >= 3.6, raise exception '''
    if sys.version_info.major == 3 and sys.version_info.minor >= 6:
        pass
    else:
        raise RuntimeError
