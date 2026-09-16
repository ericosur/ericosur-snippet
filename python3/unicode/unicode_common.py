'''
provides utility functions for unicode scripts
'''

import sys
from pathlib import Path


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    this_dir = Path(__file__).resolve().parent # unicdoe
    py3_dir = this_dir.parent # python3
    myutil_dir = py3_dir.joinpath('myutil')
    madlog_dir = py3_dir.joinpath('madlog')
    emoji_dir = py3_dir.joinpath('emoji')
    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(myutil_dir))
    sys.path.insert(0, str(madlog_dir))
    sys.path.insert(0, str(emoji_dir))

try:
    setup_local_paths()
    from madlog import get_console, get_logd, get_prt  # type: ignore[import]
    from myutil import do_nothing  # noqa: F401
except ImportError:
    print('[INFO] no madlog, exit...')
    sys.exit(1)

prt = get_prt()
logd = get_logd()
console = get_console()
