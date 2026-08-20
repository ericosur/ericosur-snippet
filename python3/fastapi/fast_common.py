'''
provides utility functions for fastapi scripts
'''

import sys
from pathlib import Path


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    def check_path_exists(path: Path) -> None:
        if not path.exists():
            raise FileNotFoundError(f"Required path does not exist: {path}")
    this_dir = Path(__file__).resolve().parent
    py3_dir = this_dir.parent
    myutil_dir = py3_dir.joinpath('myutil')
    madlog_dir = py3_dir.joinpath('madlog')
    datetime_dir = py3_dir.joinpath('datetime')
    doom_dir = datetime_dir.joinpath('dooms')

    check_path_exists(py3_dir)
    check_path_exists(myutil_dir)
    check_path_exists(madlog_dir)
    check_path_exists(datetime_dir)
    check_path_exists(doom_dir)

    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(myutil_dir))
    sys.path.insert(0, str(madlog_dir))
    sys.path.insert(0, str(datetime_dir))
    sys.path.insert(0, str(doom_dir))

try:
    setup_local_paths()
    from be_prepared import prepare_values  # type: ignore[import]
    from dooms_day import DoomsDay  # type: ignore[import]
    from madlog import get_console, get_logd, get_prt  # type: ignore[import]
    from myutil import do_nothing
except ImportError as e:
    print(f'failed to import module: {e}, exit...')
    sys.exit(1)

prt = get_prt()
logd = get_logd()
console = get_console()


def prepare_ints(v: int, after: int=0, before: int=0, radius: int=0) -> list[int]:
    ''' prepare ints '''
    if radius!=0:
        after, before = radius, radius
    upper = v + after
    lower = v - before
    if lower>upper:
        lower,upper = upper,lower
    vals = list(range(lower,upper+1))
    return vals
