#
# pylint: disable=import-error
# pylint: disable=wrong-import-position
#

'''
provide import and config functions
'''

import argparse
import os
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    this_dir = Path(__file__).resolve().parent  # opencv_python
    opencv_dir = this_dir.parent  # opencv
    top_dir = opencv_dir.parent  # ericosur-snippet top directory
    py3_dir = top_dir.joinpath('python3')
    myutil_dir = py3_dir.joinpath('myutil')
    madlog_dir = py3_dir.joinpath('madlog')
    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(myutil_dir))
    sys.path.insert(0, str(madlog_dir))

try:
    setup_local_paths()
    from madlog import get_console, get_logd, get_prt  # type: ignore[import]
    from myutil import (
        do_nothing,  # noqa: F401
        read_setting,  # type: ignore[import]
    )
except ImportError:
    print('[INFO] no madlog, exit...')
    sys.exit(1)

prt: Callable[..., None] = get_prt()
logd: Callable[..., None] = get_logd()
console = get_console()


CONFIG = 'setting.json'

def read_image_config() -> Any:
    ''' read image common config '''
    if not os.path.exists(CONFIG):
        print('[ERROR] cannot load config:', CONFIG)
        sys.exit(1)
    data = read_setting(CONFIG)
    return data

def main() -> None:
    '''Parse command-line options and optionally print the config.'''
    parser = argparse.ArgumentParser(description='Read the image configuration.')
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='print the loaded config',
    )
    args = parser.parse_args()

    config = read_image_config()
    if args.verbose:
        prt(config)
    else:
        prt(f'{__file__} provides functions')


if __name__ == '__main__':
    main()
