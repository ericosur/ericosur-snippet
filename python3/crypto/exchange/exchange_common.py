'''
provides utility functions for crypto/exchange scripts
'''

import sys
from pathlib import Path


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    this_dir = Path(__file__).resolve().parent  # cwd
    crypto_dir = this_dir.parent  # crypto
    py3_dir = crypto_dir.parent  # python3
    myutil_dir = py3_dir.joinpath('myutil')
    madlog_dir = py3_dir.joinpath('madlog')
    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(myutil_dir))
    sys.path.insert(0, str(madlog_dir))

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return

try:
    setup_local_paths()
    from madlog import get_logd, get_prt
except ImportError:
    print('[INFO] no madlog, exit...')
    sys.exit(1)

prt = get_prt()
logd = get_logd()
