'''
module that helps to load functions in myutil
'''

__VERSION__ = "2023.10.25"
SETTING_FILE = "setting.json"

# pylint: disable=import-error
# pylint: disable=wrong-import-position

import sys
from pathlib import Path

try:
    from loguru import logger
    dbg = logger.debug
except ImportError:
    dbg = print


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    this_dir = Path(__file__).resolve().parent  # store
    prime_dir = this_dir.parent  # prime
    repo_dir = prime_dir.parent  # ericosur-snippets
    py3_dir = repo_dir.joinpath('python3')  # python3
    myutil_dir = py3_dir.joinpath('myutil')
    madlog_dir = py3_dir.joinpath('madlog')
    sys.path.insert(0, str(prime_dir))
    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(myutil_dir))
    sys.path.insert(0, str(madlog_dir))

try:
    setup_local_paths()
    from myutil import (  # type: ignore[reportAttributeAccessIssue]
        MyDebug,  # type: ignore[reportAttributeAccessIssue]
        MyVerbose,  # type: ignore[reportAttributeAccessIssue]
        die,  # type: ignore[reportAttributeAccessIssue]
        do_nothing,  # type: ignore[reportAttributeAccessIssue]
        get_home,  # type: ignore[reportAttributeAccessIssue]
        is_dir,  # type: ignore[reportAttributeAccessIssue]
        is_file,  # type: ignore[reportAttributeAccessIssue]
        prt,  # type: ignore[reportAttributeAccessIssue]
        read_from_stdin,  # type: ignore[reportAttributeAccessIssue]
        read_setting,  # type: ignore[reportAttributeAccessIssue]
    )
except ImportError as e:
    raise RuntimeError(f"Failed to set up local paths: {e}") from e


__all__ = [
    'MyDebug',
    'MyVerbose',
    'dbg',
    'die',
    'do_nothing',
    'get_home',
    'is_dir',
    'is_file',
    'prt',
    'read_from_stdin',
    'read_setting',
]
