Readme
======

## myutil

The myutil now is a package of modules, not a single file.
The default path $HOME/src/ericosur-snippet/python3

python: use ```sys.path.insert()``` to add the default path.
bash: append default path into **PYTHONPATH** environment variable

```python
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

import os
import sys

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import require_python_version
```

If use a bootstrip script to launch the python script, add the following
snippet before running the script.

```bash
base_d=src/ericosur-snippet/python3
export PYTHONPATH=$PYTHONPATH:${HOME}/${base_d}
python3 foobar.py
```

## config / data serialization

* python, refer to ```emoji/_emoji.py``` and ```emoji/test_emoji.py```
  * use ```import _emoji``` to use all python built-in data structures
* json, ```import json```
  * cannot put comment in the json
* toml, ```import toml``` or ```import tomllib```
  * standard library supported from python 3.11+ (need use 3rd module for older version of python)
* pickle, ```import pickle```
* txt, use **re** to parse


## f-string

The minimum python version to support f-strings is python 3.6.

### conda tips

note: here I use 'goto.sh'

```
source $(goto -x conda)/conda.sh
```

```
conda create --name mypy python=3.10
```

```
conda activate # use base conda

conda activate mypy # created by prior command
```

```
conda deactivate
```


## Useful python cheat sheet

- https://github.com/gto76/python-cheatsheet


## featured

* [fisher_yates_shuffle.py](./fisher_yates_shuffle.py) and [shuf.py](./shuf.py)
  * https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

* [mcnugget.py](./mcnugget.py)
  * [McNuggetNumber](http://mathworld.wolfram.com/McNuggetNumber.html)
  * to find the largest mcnugget number
  * a good example to use [itertools](https://docs.python.org/3.5/library/itertools.html)

###### tags: ```python3``` ```pylint``` ```script``` ```python```
