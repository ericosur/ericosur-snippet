'''
provides utility functions for basic
'''

import sys
from pathlib import Path


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    this_dir = Path(__file__).resolve().parent
    py3_dir = this_dir.parent
    myutil_dir = py3_dir.joinpath('myutil')
    madlog_dir = py3_dir.joinpath('madlog')
    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(myutil_dir))
    sys.path.insert(0, str(madlog_dir))

try:
    setup_local_paths()
    from madlog import get_logd, get_prt, import_rich  # noqa: F401
    from myutil import do_nothing  # noqa: F401
except ImportError as e:
    print('failed to load module: ', e)
    sys.exit(1)

prt = get_prt()
logd = get_logd()
