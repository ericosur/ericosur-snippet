# README

This directory is a collection of Python 3 scripts, small experiments, and reusable helpers.
Most files are standalone and can be run directly. Some areas are grouped by topic and have
their own local `README.md` or `Makefile`.

## Layout

Common areas in this folder:

| Path | Purpose |
| --- | --- |
| `basic/` | Small Python language demos and utility snippets |
| `datetime/` | Date, calendar, and workday-related scripts |
| `random/` | Random strings, names, and word generators |
| `myutil/` | Reusable helper package for local imports |
| `numpy/`, `pandas/` | Numeric and data-processing experiments |
| `crypto/`, `qr/`, `rpc/` | Topic-specific utilities and demos |
| `kana/`, `unicode/`, `unihan/`, `emoji/` | Text, Unicode, and language-related scripts |
| `omc/` | Math and puzzle scripts |
| `data/` | Local data files used by some scripts |

There are also many one-file scripts at the top level for quick tests or small tasks.

## Running scripts

From this directory:

```bash
python3 basic/hello_world.py
python3 basic/count-by-letter.py
python3 datetime/list_possible_workday.py
```

In most case you should run

## Ruff: check one file

To lint only your currently edited script, pass the file path to `ruff check`.

From this directory:

```bash
/home/user/venv/py314/bin/python -m ruff check datetime/TianGanDiZhi/gngan_yaljux.py
```

From anywhere (absolute path):

```bash
/home/user/venv/py314/bin/python -m ruff check /home/user/src/ericosur-snippet/python3/datetime/TianGanDiZhi/gngan_yaljux.py
```

Useful variants:

```bash
# auto-fix this file only
/home/user/venv/py314/bin/python -m ruff check datetime/TianGanDiZhi/gngan_yaljux.py --fix

# check specific rules only
/home/user/venv/py314/bin/python -m ruff check datetime/TianGanDiZhi/gngan_yaljux.py --select I001,UP039

# show summary statistics for this file
/home/user/venv/py314/bin/python -m ruff check datetime/TianGanDiZhi/gngan_yaljux.py --statistics
```

### VS Code shortcut: run Ruff on active file

You can add a workspace task that always uses the currently opened file.

1. Create `.vscode/tasks.json` in this workspace with:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Ruff: check active file",
      "type": "shell",
      "command": "/home/user/venv/py314/bin/python",
      "args": [
        "-m",
        "ruff",
        "check",
        "${file}"
      ],
      "problemMatcher": []
    }
  ]
}
```

2. Run it from Command Palette:
   - `Tasks: Run Task` -> `Ruff: check active file`

3. Optional keybinding (User keybindings JSON):

```json
{
  "key": "ctrl+alt+r",
  "command": "workbench.action.tasks.runTask",
  "args": "Ruff: check active file"
}
```

Some subdirectories include a `Makefile` to run a default action.

## Local package: `myutil`

`myutil` is a package of reusable modules, not a single file.

Default local path:

```text
$HOME/src/ericosur-snippet/python3
```

If you want another script outside this tree to import `myutil`, add this directory to
`sys.path` or `PYTHONPATH`.

Example with `sys.path.insert()`:

```python
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

import os
import sys

HOME = os.getenv("HOME")
UTILPATH = os.path.join(HOME, "src/ericosur-snippet/python3")
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import require_python_version
```

Example with `PYTHONPATH`:

```bash
base_d=src/ericosur-snippet/python3
export PYTHONPATH="${PYTHONPATH}:${HOME}/${base_d}"
python3 foobar.py
```

## Data and serialization notes

- `json`: use `import json`
  - JSON does not support comments
- `toml`: use `import tomllib` on Python 3.11+, or `import toml` for older environments
- `pickle`: use `import pickle`
- plain text: parse with `re` or custom logic as needed

Examples in this repo are spread across topic folders rather than one dedicated serialization area.

## Python version notes

- f-strings require Python 3.6+
- `tomllib` is available in the standard library from Python 3.11+

## Tooling

- `pyproject.toml` currently contains local `ruff` settings
- some folders have their own `requirements.txt`
- notebooks exist in a few areas such as `numpy/`

This repo does not appear to be managed as one installable Python package. It is primarily a
working collection of scripts.

## Selected examples

- [basic/count-by-letter.py](./basic/count-by-letter.py): count labels from `A` upward
- [datetime/list_possible_workday.py](./datetime/list_possible_workday.py): list candidate workdays
- [random/five_char_verbs.py](./random/five_char_verbs.py): generate or inspect five-character verbs
- [random/fisher_yates_shuffle.py](./random/fisher_yates_shuffle.py) and [random/shuf.py](./random/shuf.py): shuffle examples
- [periodic/brief.py](./periodic/brief.py): periodic table lookup helper

## Reference

- Python cheat sheet: <https://github.com/gto76/python-cheatsheet>

Tags: `python3` `scripts` `utilities`
