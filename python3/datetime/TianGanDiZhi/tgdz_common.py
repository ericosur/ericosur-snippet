'''
provides utility functions for tgdz
'''

import sys
from pathlib import Path


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    this_dir = Path(__file__).resolve().parent
    datetime_dir = this_dir.parent
    py3_dir = datetime_dir.parent
    myutil_dir = py3_dir.joinpath('myutil')
    madlog_dir = py3_dir.joinpath('madlog')
    sys.path.insert(0, str(datetime_dir))
    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(myutil_dir))
    sys.path.insert(0, str(madlog_dir))

try:
    setup_local_paths()
    from madlog import get_logd, get_prt  # type: ignore[import]
    from myutil import do_nothing  # noqa: F401
except ImportError as e:
    print('[INFO] no madlog, exit...', e)
    sys.exit(1)

prt = get_prt()
logd = get_logd()
