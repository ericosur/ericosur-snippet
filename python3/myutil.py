#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions '''

from __future__ import print_function
import os
import sys
import json
import hashlib
import platform

# pylint: disable=no-member
# pylint: disable=import-outside-toplevel

__version__ = '0.0.4'

DEBUG = False

def read_jsonfile(fn:str, debug=False):
    '''
    specify json filename and return whole json object
    '''
    if debug:
        print(f'load json from {fn}')
    if not os.path.exists(fn):
        if debug:
            print(f'file not found: {fn}')
        return None
    # read from json file

    # method #1
    with open(fn, 'r', encoding='utf8') as fstream:
        data = json.load(fstream)

    # kiss method #2
    #data = json.load(open(fn))

    return data

def read_textfile(fn: str, debug=False) -> str:
    ''' read specified file and return file content '''
    if debug:
        print(f'read text file content from: {fn}')
    content = None
    with open(fn, 'rt', encoding='utf8') as fh:
        content = fh.read()
    return content

# in order not to break client scripts
def read_setting(fn):
    '''get json object from file'''
    return read_jsonfile(fn)

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

def need_python36():
    ''' if not python version >= 3.6, raise exception '''
    if sys.version_info.major == 3 and sys.version_info.minor >= 6:
        pass
    else:
        raise RuntimeError

def request_value(data, key, default_value=None):
    '''
    given json object and request key, if key does not exist, return None
    if default_value is specified, will return default value if value not
    found
    '''
    ret = default_value
    try:
        ret = data[key]
    except KeyError:
        print(f'key "{key}" not found, will use default_value')
    return ret

def insert_syspath(p):
    ''' help to insert path into module search path '''
    if is_path_exist(p):
        print(f'insert {p} into sys path')
        sys.path.insert(0, p)

def is_path_exist(p):
    ''' true if specified path exists '''
    return os.path.exists(p)

def isfile(url):
    '''test file exists'''
    return os.path.isfile(url)

def isdir(url):
    '''test dir exists'''
    return os.path.isdir(url)

def mkdir(url) -> bool:
    ''' simulate mkdir -p '''
    try:
        if not os.path.exists(url):
            os.makedirs(url)
            if DEBUG:
                print(f'mkdir: {url}')
            return True
    except FileExistsError as e:
        if DEBUG:
            print(e)
    return False

def get_home():
    ''' return $HOME '''
    return os.getenv('HOME')

def get_hostname():
    ''' get hostname '''
    return platform.node()

def is_cygwin():
    ''' check if cygwin '''
    system_name = platform.system().lower()
    return "cygwin" in system_name

def is_linux():
    ''' check if linux '''
    system_name = platform.system().lower()
    return "linux" in system_name

def is_windows():
    ''' check if windows '''
    system_name = platform.system().lower()
    return "windows" in system_name

def query_url_for_data(url):
    ''' query url and return data
    refer to: https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
    '''
    result = None
    debug = False
    if debug:
        print(url)
    pyver = get_python_versions()
    try:
        if pyver[0] >= 3:
            import urllib.request
            with urllib.request.urlopen(url) as f:
                result = f.read()
        else:
            #print("python < 3.0")
            import urllib
            with urllib.urlopen(url) as f:
                result = f.read()
    except ImportError:
        print('[ERROR] import error!')
    return result


def query_url_for_json(url):
    ''' query url and return json data
    refer to: https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
    '''
    result = query_url_for_data(url)
    data = json.loads(result)
    return data


def write_json(fn, data):
    ''' write json into specified file '''
    with open(fn, 'w', encoding='utf8') as ofile:
        ofile.write(json.dumps(data))
        print(f'output json to {fn}')


def hash_factory(fn, hash_func):
    ''' hash factory '''
    BUFSIZE = 65536
    dgst = hash_func()
    with open(fn, 'rb') as f:
        while True:
            data = f.read(BUFSIZE)
            if not data:
                break
            dgst.update(data)
    return dgst.hexdigest()


# demo at filesum.py
def md5sum(fn):
    ''' get md5sum from a file, return string of md5sum '''
    return hash_factory(fn, hashlib.md5)


# demo at filesum.py
def sha256sum(fn):
    ''' get sha256 from a file, return string of sha256sum '''
    return hash_factory(fn, hashlib.sha256)

def sha1sum(fn):
    ''' get sha1 from a file, return string of sha1sum '''
    return hash_factory(fn, hashlib.sha1)

def print_stderr(*args, **kwargs):
    '''
    from: https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
    '''
    print(*args, file=sys.stderr, **kwargs)

def read_from_stdin(func):
    ''' read from stdin '''
    args = []
    for line in sys.stdin:
        args.append(line.strip())
    func(args)

def get_random_str(lens=15):
    ''' get secret '''
    import secrets
    import re
    #r = secrets.token_hex(LENS)
    r = ''
    while len(r) < lens:
        r = secrets.token_urlsafe(lens*2)   # may contains _ or -
        r = re.sub(r'[-_]+', '', r)     # remove [-_]
        r = re.sub(r'^[0-9]+', '', r)   # remove leading digits 0-9
    return r[:lens]

def main():
    '''main function'''
    fn = 'nosuchfile'
    data = read_jsonfile(fn)
    if data:
        print('skipped...')
        return

def test():
    '''test function'''
    print('test() of myutil.py')
    fn = 'setting.json'
    if isfile(fn):
        jdata = read_jsonfile(fn)
        data = jdata['myutil.py']
        ret = request_value(data, 'name')
        print('ret:', ret)
    else:
        print('file not found: {fn}')

if __name__ == '__main__':
    test()
