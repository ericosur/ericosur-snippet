# README

`myutil` is a local utility package used by scripts in this repository. It collects small helpers
for filesystem checks, JSON handling, hashing, Python version checks, shell commands, date
utilities, and simple debugging helpers.

## Usage

When the repo root is on `PYTHONPATH`, import from `myutil` directly:

```python
from myutil import get_home, read_jsonfile, require_python_version
```

## Exported API

The package exports the following public names from `myutil/__init__.py`.

### Functions

- `clamp`
- `die`
- `do_nothing`
- `get_dow`
- `get_doom_num`
- `get_epoch`
- `get_home`
- `get_offset_from_year`
- `get_platform`
- `get_python_version`
- `get_python_versions`
- `is_cygwin`
- `is_dir`
- `is_file`
- `is_leapyear`
- `is_linux`
- `is_path_exist`
- `is_windows`
- `isdir`
- `isfile`
- `md5sum`
- `mkdir`
- `print_stderr`
- `prt`
- `query_url_for_data`
- `query_url_for_json`
- `read_from_stdin`
- `read_jsonfile`
- `read_setting`
- `read_textfile`
- `require_python_version`
- `run_command`
- `run_command2`
- `sha1sum`
- `sha256sum`
- `sha384sum`
- `sha3_256sum`
- `sha3_512sum`
- `sha512sum`
- `show_platform`
- `write_jsonfile`

### Classes

- `DefaultConfig`
- `MyDebug`
- `MyVerbose`
- `WhatNow`

### Notes

- `is_file` is an alias of `isfile`
- `is_dir` is an alias of `isdir`
- `sep()` exists in `myutil/__init__.py`, but it is not part of `__all__`

## Source modules

- `commonutil.py`: common helpers such as `clamp`, path checks, stdin helpers
- `jsonutil.py`: JSON and text file read/write helpers
- `hashutil.py`: file hashing helpers
- `versionutil.py`: Python version checks
- `run_cmd.py`: shell command helpers
- `mydateutil.py`: date and doomsday-related helpers
- `debug_verbose.py`: lightweight debug and verbose helpers
- `pathutil.py`: path-based config helper class
- `thedatetime.py`: current-epoch and time helper class
- `queryutil.py`: fetch URL data or JSON
- `__myutil.py`: platform detection helpers

## External dependencies

`myutil` mostly uses the Python standard library.

Optional third-party module:

- `rich`
  - used in `debug_verbose.py` and `run_cmd.py`
  - only for nicer console output via `rich.print`
  - not required for basic use; the code falls back to built-in `print` if `rich` is not installed
