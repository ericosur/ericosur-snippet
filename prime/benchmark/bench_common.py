'''
provide common functions for benchmarking
'''

import sys
from pathlib import Path


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    this_dir = Path(__file__).resolve().parent  # benchmark
    prime_dir = this_dir.parent  # prime
    repo_dir = prime_dir.parent  # ericosur-snippets
    py3_dir = repo_dir.joinpath('python3')  # python3
    myutil_dir = py3_dir.joinpath('myutil')
    madlog_dir = py3_dir.joinpath('madlog')
    sys.path.insert(0, str(prime_dir))
    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(myutil_dir))
    sys.path.insert(0, str(madlog_dir))

if __name__ == '__main__':
    print('bench_common is a module')
