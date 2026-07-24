# Ruff Linting Report

This file lists all the linting issues found by `ruff check` in this workspace.

## Summary Statistics

```text
216	I001   	[*] unsorted-imports
 18	RUF012 	[ ] mutable-class-default
 18	UP007  	[*] non-pep604-annotation-union
 16	RET501 	[*] unnecessary-return-none
 16	RUF100 	[*] unused-noqa
 16	SIM103 	[ ] needless-bool
 15	DTZ011 	[ ] call-date-today
 13	DTZ005 	[ ] call-datetime-now-without-tzinfo
 13	UP035  	[-] deprecated-import
 12	UP006  	[*] non-pep585-annotation
 11	SIM102 	[ ] collapsible-if
  8	DTZ001 	[ ] call-datetime-without-tzinfo
  8	SIM113 	[ ] enumerate-for-loop
  8	UP045  	[*] non-pep604-annotation-optional
  7	DTZ002 	[ ] call-datetime-today
  7	TRY004 	[ ] type-check-without-type-error
  6	UP024  	[*] os-error-alias
  5	PERF402	[ ] manual-list-copy
  4	DTZ006 	[ ] call-datetime-fromtimestamp
  3	RUF013 	[ ] implicit-optional
  3	RUF059 	[ ] unused-unpacked-variable
  2	BLE001 	[ ] blind-except
  2	FURB122	[*] for-loop-writes
  2	PERF102	[ ] incorrect-dict-iterator
  2	PIE808 	[*] unnecessary-range-start
  2	SIM115 	[ ] open-file-with-context-handler
  2	SIM118 	[ ] in-dict-keys
  2	UP018  	[*] native-literals
  2	UP025  	[*] unicode-kind-prefix
  1	C408   	[ ] unnecessary-collection-call
  1	C414   	[ ] unnecessary-double-cast-or-process
  1	DTZ007 	[ ] call-datetime-strptime-without-zone
  1	FURB157	[*] verbose-decimal-constructor
  1	FURB167	[*] regex-flag-alias
  1	PLR1711	[*] useless-return
  1	PLR2044	[*] empty-comment
  1	RUF022 	[*] unsorted-dunder-all
  1	RUF046 	[ ] unnecessary-cast-to-int
  1	SIM117 	[ ] multiple-with-statements
  1	UP012  	[*] unnecessary-encode-utf8
  1	YTT204 	[ ] sys-version-info-minor-cmp-int
Found 451 errors.
[*] 310 fixable with the `--fix` option (36 hidden fixes can be enabled with the `--unsafe-fixes` option).
```

## Detailed Issues

```text
I001 [*] Import block is un-sorted or un-formatted
  --> abc101.py:16:1
   |
14 |   #import numpy as np
15 |   #import pandas as pd
16 | / import matplotlib.pyplot as plt
17 | | # pylint: disable=import-error
18 | | import seaborn as sns  # type: ignore[import]
   | |_____________________^
19 |
20 |   sns.set_theme(style="darkgrid")
   |
help: Organize imports
   |
16 | import matplotlib.pyplot as plt
17 +
18 | # pylint: disable=import-error
   |

SIM115 Use a context manager for opening files
  --> access_file.py:21:14
   |
19 |     '''
20 |     try:
21 |         fp = open(fn, encoding='utf8')
   |              ^^^^
22 |     except IOError as e:
23 |         if e.errno == errno.EACCES:
   |

UP024 [*] Replace aliased errors with `OSError`
  --> access_file.py:22:12
   |
20 |     try:
21 |         fp = open(fn, encoding='utf8')
22 |     except IOError as e:
   |            ^^^^^^^
23 |         if e.errno == errno.EACCES:
24 |             print('errno: EACCES')
   |
help: Replace `IOError` with builtin `OSError`
   |
21 |         fp = open(fn, encoding='utf8')
   -     except IOError as e:
22 +     except OSError as e:
23 |         if e.errno == errno.EACCES:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> alpha/alphabravo.py:15:1
   |
13 | sys.path.insert(0, "../")
14 | sys.path.insert(0, "../../")
15 | from myutil import read_from_stdin  # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
16 |
17 | class AlphaBravoCharlie:
   |
help: Organize imports
   |
16 |
17 +
18 | class AlphaBravoCharlie:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> alpha/the_typer.py:9:1
   |
 7 |   '''
 8 |
 9 | / import sys
10 | | from typing import Annotated
   | |____________________________^
11 |   try:
12 |       import typer
   |
help: Organize imports
   |
10 | from typing import Annotated
11 +
12 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> alpha/the_typer.py:16:1
   |
14 |     print('Failed to import:', e)
15 |     sys.exit(1)
16 | from alphabravo import AlphaBravoCharlie
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
17 |
18 | def main(name: Annotated[str,
   |
help: Organize imports
   |
17 |
18 +
19 | def main(name: Annotated[str,
   |

I001 [*] Import block is un-sorted or un-formatted
  --> b64/ai64.py:22:1
   |
20 |   sys.path.insert(0, "../")
21 |   sys.path.insert(0, "python3/")
22 | / from myutil import is_linux, do_nothing  # type: ignore[import]
23 | |
24 | | import typer
   | |____________^
25 |   # if 57, one line 76 characters
26 |   # use 3n to avoid padding issues (4 char from 3 bytes)
   |
help: Organize imports
   |
21 | sys.path.insert(0, "python3/")
   - from myutil import is_linux, do_nothing  # type: ignore[import]
   -
22 | import typer
23 +
24 + from myutil import do_nothing, is_linux  # type: ignore[import]
25 +
26 | # if 57, one line 76 characters
   |

SIM103 Return the condition directly
  --> b64/ai64.py:40:5
   |
38 |       mode = os.stat(filepath).st_mode  # Get the file's mode
39 |       logd(f'{mode=}')
40 | /     if stat.S_ISCHR(mode):
41 | |         return True
42 | |     # if stat.S_ISREG(mode): return "Regular file"
43 | |     # elif stat.S_ISDIR(mode): return "Directory"
44 | |     # elif stat.S_ISBLK(mode): return "Block device"
45 | |     # elif stat.S_ISFIFO(mode): return "FIFO (named pipe)"
46 | |     # elif stat.S_ISSOCK(mode): return "Socket"
47 | |     # elif stat.S_ISLNK(mode): return "Symbolic link"
48 | |     # else: return "Unknown type"
49 | |     # except FileNotFoundError: return "File not found"
50 | |     # except PermissionError: return "Permission denied"
51 | |     return False
   | |________________^
52 |
53 |   def encode_file_to_base64_chunked(file_path, chunk_size=CHUNK_SIZE, log=do_nothing):
   |
help: Inline condition

I001 [*] Import block is un-sorted or un-formatted
  --> b64/b6485.py:14:1
   |
12 |   '''
13 |
14 | / from typing import Any
15 | | import base64
16 | | import sys
   | |__________^
17 |
18 |   try:
   |
help: Organize imports
   |
13 |
   - from typing import Any
14 | import base64
15 | import sys
16 + from typing import Any
17 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> b64/b6485.py:31:1
   |
29 |     print('INFO: no rich.console available')
30 |
31 | from butil import fill_bytearray, sep, int_to_bytes
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
32 |
33 | def is_py310plus() -> bool:
   |
help: Organize imports
   |
30 |
   - from butil import fill_bytearray, sep, int_to_bytes
31 + from butil import fill_bytearray, int_to_bytes, sep
32 +
33 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> b64/butil.py:8:1
   |
 6 | '''
 7 |
 8 | import numpy as np
   | ^^^^^^^^^^^^^^^^^^
 9 |
10 | def fill_bytearray(size: int = 24) -> bytes:
   |
help: Organize imports
   |
9  |
10 +
11 | def fill_bytearray(size: int = 24) -> bytes:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> b64/demo_baseconv.py:16:1
   |
14 |     USE_RICH = False
15 |
16 | from butil import fill_bytearray, sep, int_from_bytes
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
17 |
18 | prt = rprint if USE_RICH else print
   |
help: Organize imports
   |
15 |
   - from butil import fill_bytearray, sep, int_from_bytes
16 + from butil import fill_bytearray, int_from_bytes, sep
17 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> b64/do_digest.py:10:1
   |
 8 |   '''
 9 |
10 | / from hashlib import file_digest
11 | | import sys
   | |__________^
12 |
13 |   try:
   |
help: Organize imports
   |
9  |
10 + import sys
11 | from hashlib import file_digest
   - import sys
12 |
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> b64/do_digest.py:25:1
   |
23 |     USE_LOGGER = False
24 |
25 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
26 | sys.path.insert(0, "./")
27 | sys.path.insert(0, "../")
   |
help: Remove unused `noqa` directive
   |
24 |
   - # ruff: noqa: E402
25 | sys.path.insert(0, "./")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> b64/do_digest.py:32:1
   |
30 |   # if python 3.11+, we may use file_digest, instaed sha512sum() ...
31 |   #from myutil import md5sum, sha512sum, sha3_256sum, sha3_512sum  # type: ignore[import]
32 | / from myutil import get_python_versions, run_command  # type: ignore[import]
33 | | # setup CLI cmd and function name in the dgst.py
34 | | from dgst import digests  # type: ignore[import]
   | |________________________^
35 |
36 |   prt = rprint if USE_RICH else print
   |
help: Organize imports
   |
31 | #from myutil import md5sum, sha512sum, sha3_256sum, sha3_512sum  # type: ignore[import]
   - from myutil import get_python_versions, run_command  # type: ignore[import]
32 | # setup CLI cmd and function name in the dgst.py
33 | from dgst import digests  # type: ignore[import]
34 |
35 + from myutil import get_python_versions, run_command  # type: ignore[import]
36 +
37 | prt = rprint if USE_RICH else print
   |

I001 [*] Import block is un-sorted or un-formatted
  --> b64/mknn64.py:7:1
   |
 5 |   '''
 6 |
 7 | / import argparse
 8 | | import base64
 9 | | import hashlib
10 | | import re
11 | | import os
12 | | import sys
   | |__________^
13 |
14 |   try:
   |
help: Organize imports
   |
9  | import hashlib
10 + import os
11 | import re
   - import os
12 | import sys
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> b64/mknn64.py:23:5
   |
21 | def do_nothing(*_args, **_wargs) -> None:
22 |     ''' do nothing '''
23 |     return None
   |     ^^^^^^^^^^^
24 |
25 | DEF_FN = 'a.txt'
   |
help: Remove explicit `return None`
   |
22 |     ''' do nothing '''
   -     return None
23 +     return
24 |
   |

SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  --> b64/mknn64.py:75:17
   |
73 |             for ln in fobj:
74 |                 ln = ln.strip()
75 |                 cnt += 1
   |                 ^^^^^^^^
76 |                 m = re.match(r'^#(.+)$', ln)
77 |                 if m:
   |

I001 [*] Import block is un-sorted or un-formatted
 --> b64/topt.py:7:1
  |
5 | '''
6 |
7 | import base64
  | ^^^^^^^^^^^^^
8 |
9 | def main() -> None:
  |
help: Organize imports
   |
8  |
9  +
10 | def main() -> None:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/aio.py:7:1
   |
 5 |   '''
 6 |
 7 | / import asyncio
 8 | | import concurrent
 9 | | import threading
10 | | from timeit import default_timer
11 | | from random import randint
12 | | import numpy as np
   | |__________________^
13 |
14 |   try:
   |
help: Organize imports
   |
9  | import threading
10 + from random import randint
11 | from timeit import default_timer
   - from random import randint
12 +
13 | import numpy as np
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> basic/aio.py:89:5
   |
87 |     print_during(during, f'easy-{idx}')
88 |     logd(f'task{idx}: do_easy_job done!')
89 |     return None
   |     ^^^^^^^^^^^
90 |
91 | def print_during(during: float, msg: str|None) -> None:
   |
help: Remove explicit `return None`
   |
88 |     logd(f'task{idx}: do_easy_job done!')
   -     return None
89 +     return
90 |
   |

PLR1711 [*] Useless `return` statement at end of function
  --> basic/aio.py:89:5
   |
87 |     print_during(during, f'easy-{idx}')
88 |     logd(f'task{idx}: do_easy_job done!')
89 |     return None
   |     ^^^^^^^^^^^
90 |
91 | def print_during(during: float, msg: str|None) -> None:
   |
help: Remove useless `return` statement
   |
88 |     logd(f'task{idx}: do_easy_job done!')
   -     return None
89 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/bsc.py:13:1
   |
11 |   # pylint: disable=wrong-import-order
12 |
13 | / import matplotlib.pyplot as plt
14 | | import pymc as pm  # type: ignore[import]
15 | | import numpy as np
   | |__________________^
16 |
17 |   # 生成一些虛構的數據
   |
help: Organize imports
   |
14 | import pymc as pm  # type: ignore[import]
15 +
16 | import numpy as np
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> basic/byte_to_str.py:31:5
   |
29 | def nothing(*_args, **_kwargs) -> None:
30 |     ''' do donothing'''
31 |     return None
   |     ^^^^^^^^^^^
32 |
33 | logd = logger.debug if USE_LOGG else nothing
   |
help: Remove explicit `return None`
   |
30 |     ''' do donothing'''
   -     return None
31 +     return
32 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/check_path_with_space.py:7:1
   |
 5 |   '''
 6 |
 7 | / import os
 8 | | import re
 9 | | from sysconfig import get_platform
   | |__________________________________^
10 |   try:
11 |       from rich import print as pprint
   |
help: Organize imports
   |
9  | from sysconfig import get_platform
10 +
11 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/const.py:13:1
   |
11 | '''
12 |
13 | import sys
   | ^^^^^^^^^^
   |
help: Organize imports
   |
14 |
   -
15 | # pylint: disable=import-outside-toplevel
   |

I001 [*] Import block is un-sorted or un-formatted
 --> basic/dataclass.py:6:1
  |
4 | '''
5 |
6 | from dataclasses import dataclass
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
7 |
8 | @dataclass
  |
help: Organize imports
  |
7 |
8 +
9 | @dataclass
  |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/dict_test.py:11:5
   |
 9 |   '''
10 |   try:
11 | /     from rich import print as rprint
12 | |     from rich.pretty import pprint
   | |__________________________________^
13 |       USE_RICH = True
14 |   except ImportError:
   |
help: Organize imports
   |
10 | try:
   -     from rich import print as rprint
11 |     from rich.pretty import pprint
12 +
13 +     from rich import print as rprint
14 |     USE_RICH = True
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/getmac.py:7:1
   |
 5 |   '''
 6 |
 7 | / import os
 8 | | import re
 9 | | import sys
   | |__________^
10 |   try:
11 |       #from rich import print as pprint
   |
help: Organize imports
   |
9  | import sys
10 +
11 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/getmac.py:12:5
   |
10 |   try:
11 |       #from rich import print as pprint
12 | /     from rich.pretty import pprint
13 | |     from rich.console import Console
   | |____________________________________^
14 |       RICH_ENABLED = True
15 |       prt = pprint
   |
help: Organize imports
   |
11 |     #from rich import print as pprint
12 +     from rich.console import Console
13 |     from rich.pretty import pprint
   -     from rich.console import Console
14 |     RICH_ENABLED = True
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/getmac.py:30:5
   |
28 |       abs_path = os.path.join(home, 'src/ericosur-snippet/python3')
29 |       sys.path.insert(0, abs_path)
30 | /     from myutil import is_linux, show_platform  # type: ignore[import]
31 | |     from myutil import run_command  # type: ignore[import]
   | |__________________________________^
32 |   except ImportError:
33 |       print("cannot import local modules")
   |
help: Organize imports
   |
29 |     sys.path.insert(0, abs_path)
   -     from myutil import is_linux, show_platform  # type: ignore[import]
   -     from myutil import run_command  # type: ignore[import]
30 +     from myutil import (  # type: ignore[import]
31 +         is_linux,
32 +         run_command,  # type: ignore[import]
33 +         show_platform,
34 +     )
35 | except ImportError:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/ifc.py:7:1
   |
 5 |   '''
 6 |
 7 | / import os
 8 | | import re
 9 | | import sys
   | |__________^
10 |   try:
11 |       #from rich import print as pprint
   |
help: Organize imports
   |
9  | import sys
10 +
11 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/ifc.py:12:5
   |
10 |   try:
11 |       #from rich import print as pprint
12 | /     from rich.pretty import pprint
13 | |     from rich.console import Console
14 | |     from rich.table import Table
   | |________________________________^
15 |       RICH_ENABLED = True
16 |       prt = pprint
   |
help: Organize imports
   |
11 |     #from rich import print as pprint
12 +     from rich.console import Console
13 |     from rich.pretty import pprint
   -     from rich.console import Console
14 |     from rich.table import Table
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/ifc.py:32:5
   |
30 |       abs_path = os.path.join(home, 'src/ericosur-snippet/python3')
31 |       sys.path.insert(0, abs_path)
32 | /     from myutil import is_linux, is_windows, show_platform  # type: ignore[import]
33 | |     from myutil import run_command, run_command2  # type: ignore[import]
   | |________________________________________________^
34 |   except ImportError:
35 |       print("cannot import local modules")
   |
help: Organize imports
   |
31 |     sys.path.insert(0, abs_path)
   -     from myutil import is_linux, is_windows, show_platform  # type: ignore[import]
   -     from myutil import run_command, run_command2  # type: ignore[import]
32 +     from myutil import (  # type: ignore[import]  # type: ignore[import]
33 +         is_linux,
34 +         is_windows,
35 +         run_command,
36 +         run_command2,
37 +         show_platform,
38 +     )
39 | except ImportError:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/ipaddr.py:7:1
   |
 5 |   '''
 6 |
 7 | / import os
 8 | | import re
 9 | | import sys
   | |__________^
10 |   try:
11 |       #from rich import print as pprint
   |
help: Organize imports
   |
9  | import sys
10 +
11 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/list2bytes.py:9:1
   |
 7 |   '''
 8 |
 9 | / from hexdump import hexdump # type: ignore[import]
10 | | import numpy as np
   | |__________________^
   |
help: Organize imports
   |
8  |
   - from hexdump import hexdump # type: ignore[import]
9  + from hexdump import hexdump  # type: ignore[import]
10 +
11 | import numpy as np
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/load_toml.py:11:1
   |
 9 | '''
10 |
11 | import sys
   | ^^^^^^^^^^
12 | try:
13 |     from rich import print as pprint
   |
help: Organize imports
   |
11 | import sys
12 +
13 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
 --> basic/lvwords.py:6:1
  |
4 | levenshtein distance
5 | '''
6 | import sys
  | ^^^^^^^^^^
7 | try:
8 |     import Levenshtein as lt  # type: ignore[import]
  |
help: Organize imports
  |
6 | import sys
7 +
8 | try:
  |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/match.py:8:1
   |
 6 | '''
 7 |
 8 | import sys
   | ^^^^^^^^^^
 9 | try:
10 |     sys.path.insert(0, "../")
   |
help: Organize imports
   |
8  | import sys
9  +
10 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/mcsample.py:9:1
   |
 7 |   # pylint: disable=import-error
 8 |
 9 | / import arviz as az  # type: ignore[import]
10 | | import matplotlib.pyplot as plt
11 | | import numpy as np
   | |__________________^
   |
help: Organize imports
   |
10 | import matplotlib.pyplot as plt
11 +
12 | import numpy as np
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/read_os_release.py:7:1
   |
 5 |   '''
 6 |
 7 | / import os
 8 | | import re
 9 | | import sys
10 | | from typing import Union, Dict
   | |______________________________^
11 |   try:
12 |       from rich import print as pprint
   |
help: Organize imports
   |
9  | import sys
   - from typing import Union, Dict
10 + from typing import Dict, Union
11 +
12 | try:
   |

UP035 `typing.Dict` is deprecated, use `dict` instead
  --> basic/read_os_release.py:10:1
   |
 8 | import re
 9 | import sys
10 | from typing import Union, Dict
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
11 | try:
12 |     from rich import print as pprint
   |

UP007 [*] Use `X | Y` for type annotations
  --> basic/read_os_release.py:24:34
   |
22 |         self.info = self.read_os_release()
23 |
24 |     def read_os_release(self) -> Union[Dict[str, str], None]:
   |                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 |         ''' read /etc/os-release '''
26 |         fn = self.FN
   |
help: Convert to `X | Y`
   |
23 |
   -     def read_os_release(self) -> Union[Dict[str, str], None]:
24 +     def read_os_release(self) -> Dict[str, str] | None:
25 |         ''' read /etc/os-release '''
   |

UP006 [*] Use `dict` instead of `Dict` for type annotation
  --> basic/read_os_release.py:24:40
   |
22 |         self.info = self.read_os_release()
23 |
24 |     def read_os_release(self) -> Union[Dict[str, str], None]:
   |                                        ^^^^
25 |         ''' read /etc/os-release '''
26 |         fn = self.FN
   |
help: Replace with `dict`
   |
23 |
   -     def read_os_release(self) -> Union[Dict[str, str], None]:
24 +     def read_os_release(self) -> Union[dict[str, str], None]:
25 |         ''' read /etc/os-release '''
   |

UP007 [*] Use `X | Y` for type annotations
  --> basic/read_os_release.py:42:28
   |
40 |         return ret
41 |
42 |     def is_ubutnu(self) -> Union[bool, None]:
   |                            ^^^^^^^^^^^^^^^^^
43 |         ''' true if ubuntu '''
44 |         return None if self.info is None else self.info.get('ID') == 'ubuntu'
   |
help: Convert to `X | Y`
   |
41 |
   -     def is_ubutnu(self) -> Union[bool, None]:
42 +     def is_ubutnu(self) -> bool | None:
43 |         ''' true if ubuntu '''
   |

UP007 [*] Use `X | Y` for type annotations
  --> basic/read_os_release.py:46:49
   |
44 |         return None if self.info is None else self.info.get('ID') == 'ubuntu'
45 |
46 |     def match_ubuntu_version(self, ver: str) -> Union[bool, None]:
   |                                                 ^^^^^^^^^^^^^^^^^
47 |         ''' true if ubuntu version matches '''
48 |         return None if self.info is None else self.info.get("VERSION_ID") == ver
   |
help: Convert to `X | Y`
   |
45 |
   -     def match_ubuntu_version(self, ver: str) -> Union[bool, None]:
46 +     def match_ubuntu_version(self, ver: str) -> bool | None:
47 |         ''' true if ubuntu version matches '''
   |

UP007 [*] Use `X | Y` for type annotations
  --> basic/read_os_release.py:50:33
   |
48 |         return None if self.info is None else self.info.get("VERSION_ID") == ver
49 |
50 |     def is_ubuntu_1804(self) -> Union[bool, None]:
   |                                 ^^^^^^^^^^^^^^^^^
51 |         ''' true if ubuntu 18.04, none if no info retrieved '''
52 |         return None if self.info is None else self.info.get('VERSION_ID') == "18.04"
   |
help: Convert to `X | Y`
   |
49 |
   -     def is_ubuntu_1804(self) -> Union[bool, None]:
50 +     def is_ubuntu_1804(self) -> bool | None:
51 |         ''' true if ubuntu 18.04, none if no info retrieved '''
   |

UP007 [*] Use `X | Y` for type annotations
  --> basic/read_os_release.py:54:33
   |
52 |         return None if self.info is None else self.info.get('VERSION_ID') == "18.04"
53 |
54 |     def is_ubuntu_2204(self) -> Union[bool, None]:
   |                                 ^^^^^^^^^^^^^^^^^
55 |         ''' true if ubuntu 18.04, none if no info retrieved '''
56 |         return None if self.info is None else self.info.get('VERSION_ID') == "18.04"
   |
help: Convert to `X | Y`
   |
53 |
   -     def is_ubuntu_2204(self) -> Union[bool, None]:
54 +     def is_ubuntu_2204(self) -> bool | None:
55 |         ''' true if ubuntu 18.04, none if no info retrieved '''
   |

UP007 [*] Use `X | Y` for type annotations
  --> basic/read_os_release.py:58:43
   |
56 |         return None if self.info is None else self.info.get('VERSION_ID') == "18.04"
57 |
58 |     def is_ge_ubuntu(self, ver: float) -> Union[bool, None]:
   |                                           ^^^^^^^^^^^^^^^^^
59 |         ''' true if number >= ver (version taken as float) '''
60 |         if self.info is None:
   |
help: Convert to `X | Y`
   |
57 |
   -     def is_ge_ubuntu(self, ver: float) -> Union[bool, None]:
58 +     def is_ge_ubuntu(self, ver: float) -> bool | None:
59 |         ''' true if number >= ver (version taken as float) '''
   |

UP007 [*] Use `X | Y` for type annotations
  --> basic/read_os_release.py:69:36
   |
67 |             return None
68 |
69 |     def get_version_float(self) -> Union[float, None]:
   |                                    ^^^^^^^^^^^^^^^^^^
70 |         ''' return version as float '''
71 |         if self.info is None:
   |
help: Convert to `X | Y`
   |
68 |
   -     def get_version_float(self) -> Union[float, None]:
69 +     def get_version_float(self) -> float | None:
70 |         ''' return version as float '''
   |

UP007 [*] Use `X | Y` for type annotations
  --> basic/read_os_release.py:79:24
   |
77 |             return None
78 |
79 | def is_ubuntu1804() -> Union[bool, None]:
   |                        ^^^^^^^^^^^^^^^^^
80 |     ''' true if ubuntu 18.04'''
81 |     obj = OSRelease()
   |
help: Convert to `X | Y`
   |
78 |
   - def is_ubuntu1804() -> Union[bool, None]:
79 + def is_ubuntu1804() -> bool | None:
80 |     ''' true if ubuntu 18.04'''
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/readtoml.py:8:1
   |
 6 |   '''
 7 |
 8 | / import numpy as np
 9 | | from load_toml import LoadToml
   | |______________________________^
10 |   try:
11 |       from rich import print as pprint
   |
help: Organize imports
   |
7  |
8  + from load_toml import LoadToml
9  +
10 | import numpy as np
   - from load_toml import LoadToml
11 +
12 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/sum.py:9:1
   |
 7 |   '''
 8 |
 9 | / from time import perf_counter as pc
10 | | from time import sleep
11 | | from functools import reduce
12 | | from typing import Any,Union
13 | | import numpy as np
   | |__________________^
14 |
15 |   class Solution:
   |
help: Organize imports
   |
8  |
9  + from functools import reduce
10 | from time import perf_counter as pc
11 | from time import sleep
   - from functools import reduce
   - from typing import Any,Union
12 + from typing import Any, Union
13 +
14 | import numpy as np
15 |
16 +
17 | class Solution:
   |

UP007 [*] Use `X | Y` for type annotations
  --> basic/sum.py:34:33
   |
32 |         return 0
33 |
34 |     def do_something(self, func:Union[Any,None]) -> None:
   |                                 ^^^^^^^^^^^^^^^
35 |         ''' do '''
36 |         start = pc()
   |
help: Convert to `X | Y`
   |
33 |
   -     def do_something(self, func:Union[Any,None]) -> None:
34 +     def do_something(self, func:Any | None) -> None:
35 |         ''' do '''
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/the9801.py:6:1
   |
 4 |   '''
 5 |
 6 | / from math import gcd
 7 | | from decimal import Decimal, getcontext
 8 | | from sympy import factorint
   | |___________________________^
 9 |   try:
10 |       from rich.console import Console
   |
help: Organize imports
   |
5  |
6  + from decimal import Decimal, getcontext
7  | from math import gcd
   - from decimal import Decimal, getcontext
8  +
9  | from sympy import factorint
10 +
11 | try:
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> basic/the9801.py:18:5
   |
16 | def do_nothing(*_args, **_wargs) -> None:
17 |     ''' do nothing'''
18 |     return None
   |     ^^^^^^^^^^^
19 |
20 | logd = do_nothing
   |
help: Remove explicit `return None`
   |
17 |     ''' do nothing'''
   -     return None
18 +     return
19 |
   |

SIM118 Use `key in dict` instead of `key in dict.keys()`
  --> basic/the9801.py:68:13
   |
66 |         print(f"{n} 的質因數分解: {thed}")
67 |         nums = []
68 |         for key in thed.keys():
   |             ^^^^^^^^^^^^^^^^^^
69 |             #print(key, thed[key])
70 |             nums.append(pow(key, thed[key]))
   |
help: Remove `.keys()`

I001 [*] Import block is un-sorted or un-formatted
  --> basic/wmic.py:16:1
   |
14 |   '''
15 |
16 | / import datetime
17 | | import os
18 | | import re
19 | | import shutil
20 | | import subprocess
21 | | import sys
22 | | import tempfile
23 | | import time
24 | | from sysconfig import get_platform
   | |__________________________________^
25 |   try:
26 |       #from rich import print as pprint
   |
help: Organize imports
   |
24 | from sysconfig import get_platform
25 +
26 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> basic/wmic.py:27:5
   |
25 |   try:
26 |       #from rich import print as pprint
27 | /     from rich.pretty import pprint
28 | |     from rich.console import Console
   | |____________________________________^
29 |       prt = pprint
30 |       console = Console()
   |
help: Organize imports
   |
26 |     #from rich import print as pprint
27 +     from rich.console import Console
28 |     from rich.pretty import pprint
   -     from rich.console import Console
29 |     prt = pprint
   |

I001 [*] Import block is un-sorted or un-formatted
  --> change_subject.py:14:1
   |
12 |   '''
13 |
14 | / import json
15 | | import sys
16 | |
17 | | from myutil import read_jsonfile, DefaultConfig
   | |_______________________________________________^
18 |
19 |   try:
   |
help: Organize imports
   |
16 |
   - from myutil import read_jsonfile, DefaultConfig
17 + from myutil import DefaultConfig, read_jsonfile
18 |
   |

C414 Unnecessary `list()` call within `sorted()`
  --> cntchr.py:12:10
   |
10 | def get_freq(s: str) -> None:
11 |     ''' get frequency, got a dict with key and frequency '''
12 |     cc = sorted(list(s))
   |          ^^^^^^^^^^^^^^^
13 |     d : dict[str,int] = {}
14 |     for c in cc:
   |
help: Remove the inner `list()` call

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/aes-siv.py:34:1
   |
32 |     USE_RICH = False
33 |
34 | from run_vector import ScryptVector, genkey_vector
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
35 |
36 | def do_nothing(*_args, **_wargs) -> None:
   |
help: Organize imports
   |
35 |
36 +
37 | def do_nothing(*_args, **_wargs) -> None:
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> crypto/aes-siv.py:38:5
   |
36 | def do_nothing(*_args, **_wargs) -> None:
37 |     ''' do nothing '''
38 |     return None
   |     ^^^^^^^^^^^
39 |
40 | prt = rprint if USE_RICH else print
   |
help: Remove explicit `return None`
   |
37 |     ''' do nothing '''
   -     return None
38 +     return
39 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/chataes.py:12:1
   |
10 |   '''
11 |
12 | / import argparse
13 | | import sys
14 | | from typing import Any
   | |______________________^
15 |   try:
16 |       from Crypto.Cipher import AES
   |
help: Organize imports
   |
14 | from typing import Any
15 +
16 | try:
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> crypto/chataes.py:35:5
   |
33 | def do_nothing(*_args, **_wargs) -> None:
34 |     ''' do nothing '''
35 |     return None
   |     ^^^^^^^^^^^
36 |
37 | prt = rprint if USE_RICH else print
   |
help: Remove explicit `return None`
   |
34 |     ''' do nothing '''
   -     return None
35 +     return
36 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/decpu.py:11:1
   |
 9 |   '''
10 |
11 | / import os
12 | | import sys
13 | | from typing import Annotated
14 | | from passutil import PassUtil
15 | | import typer
   | |____________^
16 |
17 |   class Demo:
   |
help: Organize imports
   |
13 | from typing import Annotated
14 +
15 + import typer
16 | from passutil import PassUtil
   - import typer
17 |
18 +
19 | class Demo:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/exchange/keyiv.py:7:1
   |
 5 |   '''
 6 |
 7 | / import binascii
 8 | | import os
 9 | | import re
   | |_________^
10 |   try:
11 |       from Crypto.Random import get_random_bytes
   |
help: Organize imports
   |
9  | import re
10 +
11 | try:
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> crypto/exchange/keyiv.py:26:5
   |
24 | def _do_nothing(*_args, **_wargs) -> None:
25 |     ''' do nothing '''
26 |     return None
   |     ^^^^^^^^^^^
27 |
28 | def from_file(fn: str) -> bytes:
   |
help: Remove explicit `return None`
   |
25 |     ''' do nothing '''
   -     return None
26 +     return
27 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/exchange/t0.py:7:1
   |
 5 |   '''
 6 |
 7 | / import os
 8 | | import re
 9 | | import sys
10 | | # use bytes.hex() instead of binascii.hexlify
11 | | #from binascii import hexlify
12 | | import base64
   | |_____________^
13 |   try:
14 |       from Crypto.Cipher import AES
   |
help: Organize imports
   |
6  |
   - import os
   - import re
   - import sys
7  | # use bytes.hex() instead of binascii.hexlify
8  | #from binascii import hexlify
9  | import base64
10 + import os
11 + import re
12 + import sys
13 +
14 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/exchange/t0.py:25:1
   |
23 |     USE_LOGGER = False
24 |
25 | from keyiv import from_file, from_env, save_bin
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
26 |
27 | sys.path.insert(0, '../../')
   |
help: Organize imports
   |
24 |
   - from keyiv import from_file, from_env, save_bin
25 + from keyiv import from_env, from_file, save_bin
26 |
   |

FURB122 [*] Use of `f.write` in a for loop
   --> crypto/exchange/t0.py:147:13
    |
145 |           encoded_data = base64.b64encode(data)
146 |           with open(ofile, 'wb') as f:
147 | /             for i in range(0, len(encoded_data), LINE_LENGTH):
148 | |                 f.write(encoded_data[i:i+LINE_LENGTH] + b'\n')
    | |______________________________________________________________^
149 |
150 |       def encrypt_file(self):
    |
help: Replace with `f.writelines`
    |
146 |         with open(ofile, 'wb') as f:
    -             for i in range(0, len(encoded_data), LINE_LENGTH):
    -                 f.write(encoded_data[i:i+LINE_LENGTH] + b'\n')
147 +             f.writelines(encoded_data[i:i+LINE_LENGTH] + b'\n' for i in range(0, len(encoded_data), LINE_LENGTH))
148 |
    |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/kid_rsa/decrypt_sta.py:8:1
   |
 6 |   '''
 7 |
 8 | / from sta_prompt import has_console, prompt_alert, prompt_input
 9 | |
10 | | from kid_rsa import decrypt
   | |___________________________^
   |
help: Organize imports
   |
7  |
   - from sta_prompt import has_console, prompt_alert, prompt_input
   -
8  | from kid_rsa import decrypt
9  + from sta_prompt import has_console, prompt_alert, prompt_input
10 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/kid_rsa/encrypt_sta.py:8:1
   |
 6 |   '''
 7 |
 8 | / from sta_prompt import has_console, prompt_alert, prompt_input
 9 | |
10 | | from kid_rsa import encrypt
   | |___________________________^
   |
help: Organize imports
   |
7  |
   - from sta_prompt import has_console, prompt_alert, prompt_input
   -
8  | from kid_rsa import encrypt
9  + from sta_prompt import has_console, prompt_alert, prompt_input
10 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/kid_rsa/fulltest.py:8:1
   |
 6 |   '''
 7 |
 8 | / from random import randint
 9 | |
10 | | from sta_prompt import has_console, prompt_alert, prompt_input
11 | |
12 | | from kid_rsa import decrypt, encrypt, make_pair
   | |_______________________________________________^
   |
help: Organize imports
   |
9  |
   - from sta_prompt import has_console, prompt_alert, prompt_input
   -
10 | from kid_rsa import decrypt, encrypt, make_pair
11 + from sta_prompt import has_console, prompt_alert, prompt_input
12 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/kid_rsa/genkey_sta.py:8:1
   |
 6 |   '''
 7 |
 8 | / from sta_prompt import has_console, prompt_alert, prompt_input
 9 | |
10 | | from kid_rsa import make_pair
   | |_____________________________^
   |
help: Organize imports
   |
7  |
   - from sta_prompt import has_console, prompt_alert, prompt_input
   -
8  | from kid_rsa import make_pair
9  + from sta_prompt import has_console, prompt_alert, prompt_input
10 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/passutil.py:12:1
   |
10 |   '''
11 |
12 | / import argparse
13 | | import base64
14 | | import hashlib
15 | | import sys
16 | | import json
17 | | from typing import Any, Dict, Tuple
18 | | from loguru import logger
   | |_________________________^
19 |   try:
20 |       from Crypto.Cipher import AES
   |
help: Organize imports
   |
14 | import hashlib
15 + import json
16 | import sys
   - import json
17 | from typing import Any, Dict, Tuple
18 +
19 | from loguru import logger
20 +
21 | try:
   |

UP035 `typing.Dict` is deprecated, use `dict` instead
  --> crypto/passutil.py:17:1
   |
15 | import sys
16 | import json
17 | from typing import Any, Dict, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
18 | from loguru import logger
19 | try:
   |

UP035 `typing.Tuple` is deprecated, use `tuple` instead
  --> crypto/passutil.py:17:1
   |
15 | import sys
16 | import json
17 | from typing import Any, Dict, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
18 | from loguru import logger
19 | try:
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> crypto/passutil.py:30:5
   |
28 | def do_nothing(*_args, **_wargs) -> None:
29 |     ''' do nothing'''
30 |     return None
   |     ^^^^^^^^^^^
31 |
32 | class PassUtil:
   |
help: Remove explicit `return None`
   |
29 |     ''' do nothing'''
   -     return None
30 +     return
31 |
   |

UP006 [*] Use `dict` instead of `Dict` for type annotation
  --> crypto/passutil.py:79:23
   |
77 |                 print(json.dumps(d, indent=4), file=fobj)
78 |
79 |     def load(self) -> Dict | None:
   |                       ^^^^
80 |         ''' load from json '''
81 |         fn = self.jsf
   |
help: Replace with `dict`
   |
78 |
   -     def load(self) -> Dict | None:
79 +     def load(self) -> dict | None:
80 |         ''' load from json '''
   |

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
   --> crypto/passutil.py:109:32
    |
107 |         self.a_dict['ciphertext'] = self.b64enc(ciphertext)
108 |
109 |     def __decodeb64__(self) -> Tuple[bytes, bytes, bytes, bytes]:
    |                                ^^^^^
110 |         ''' load data '''
111 |         cn = self.b64dec(self.a_dict['cn'])
    |
help: Replace with `tuple`
    |
108 |
    -     def __decodeb64__(self) -> Tuple[bytes, bytes, bytes, bytes]:
109 +     def __decodeb64__(self) -> tuple[bytes, bytes, bytes, bytes]:
110 |         ''' load data '''
    |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/run_vector.py:30:1
   |
28 |   '''
29 |
30 | / from hashlib import scrypt
31 | | from pydantic import BaseModel
   | |______________________________^
32 |
33 |   def show_hex(dk: bytes) -> None:
   |
help: Organize imports
   |
30 | from hashlib import scrypt
31 +
32 | from pydantic import BaseModel
33 |
34 +
35 | def show_hex(dk: bytes) -> None:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/scrypt_demo.py:14:1
   |
12 |   '''
13 |
14 | / import argparse
15 | | from typing import Any
16 | | import base64
17 | | import json
18 | | import os
19 | | import sys
   | |__________^
20 |   try:
21 |       from rich import print as rprint
   |
help: Organize imports
   |
14 | import argparse
   - from typing import Any
15 | import base64
16 | import json
17 | import os
18 | import sys
19 + from typing import Any
20 +
21 | try:
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> crypto/scrypt_demo.py:36:5
   |
34 | def do_nothing(*_args, **_wargs) -> None:
35 |     ''' do nothing '''
36 |     return None
   |     ^^^^^^^^^^^
   |
help: Remove explicit `return None`
   |
35 |     ''' do nothing '''
   -     return None
36 +     return
37 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> crypto/scrypt_demo.py:40:5
   |
39 | try:
40 |     from run_vector import do_scrypt, ScryptVector, run_test_vector
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
41 | except ImportError:
42 |     logger.error("The module 'run_vector' could not be found")
   |
help: Organize imports
   |
39 | try:
   -     from run_vector import do_scrypt, ScryptVector, run_test_vector
40 +     from run_vector import ScryptVector, do_scrypt, run_test_vector
41 | except ImportError:
   |

I001 [*] Import block is un-sorted or un-formatted
 --> cython/t/setup.py:1:1
  |
1 | / from distutils.core import setup
2 | | from Cython.Build import cythonize
  | |__________________________________^
3 |
4 |   setup(ext_modules = cythonize('fibo.pyx', language_level = "3"))
  |
help: Organize imports
  |
1 | from distutils.core import setup
2 +
3 | from Cython.Build import cythonize
  |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/TianGanDiZhi/cli_tester.py:10:1
   |
 8 |   '''
 9 |
10 | / import sys
11 | | from random import randint
12 | | from typing import Annotated
   | |____________________________^
13 |   try:
14 |       import typer
   |
help: Organize imports
   |
12 | from typing import Annotated
13 +
14 | try:
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> datetime/TianGanDiZhi/cli_tester.py:27:1
   |
25 |     USE_CONSOLE = False
26 |
27 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
28 | sys.path.insert(0, "..")
29 | sys.path.insert(0, "TaiGanDiZhi/")
   |
help: Remove unused `noqa` directive
   |
26 |
   - # ruff: noqa: E402
27 | sys.path.insert(0, "..")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/TianGanDiZhi/cli_tester.py:32:1
   |
30 |   sys.path.insert(0, "../datetime/")
31 |   sys.path.insert(0, "../../python3/datetime/")
32 | / from nothing import do_nothing  # type: ignore[import]
33 | | from gngan_yaljux import do_tests, do_values, do_verbose, GanChi
   | |________________________________________________________________^
34 |
35 |   logd = console.log if USE_CONSOLE else print
   |
help: Organize imports
   |
31 | sys.path.insert(0, "../../python3/datetime/")
32 + from gngan_yaljux import GanChi, do_tests, do_values, do_verbose
33 | from nothing import do_nothing  # type: ignore[import]
   - from gngan_yaljux import do_tests, do_values, do_verbose, GanChi
34 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/TianGanDiZhi/gngan_yaljux.py:18:1
   |
16 |   '''
17 |
18 | / import sys
19 | | from datetime import datetime
20 | | from typing import Callable, Any
   | |________________________________^
21 |
22 |   sys.path.insert(0, "..")
   |
help: Organize imports
   |
19 | from datetime import datetime
   - from typing import Callable, Any
20 + from typing import Any, Callable
21 |
   |

UP035 [*] Import from `collections.abc` instead: `Callable`
  --> datetime/TianGanDiZhi/gngan_yaljux.py:20:1
   |
18 | import sys
19 | from datetime import datetime
20 | from typing import Callable, Any
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
21 |
22 | sys.path.insert(0, "..")
   |
help: Import from `collections.abc`
   |
19 | from datetime import datetime
   - from typing import Callable, Any
20 + from typing import Any
21 + from collections.abc import Callable
22 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/TianGanDiZhi/gngan_yaljux.py:25:1
   |
23 | sys.path.insert(0, "../datetime/")
24 | sys.path.insert(0, "../../python3/datetime/")
25 | from nothing import do_nothing # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
26 |
27 | try:
   |
help: Organize imports
   |
24 | sys.path.insert(0, "../../python3/datetime/")
   - from nothing import do_nothing # type: ignore[import]
25 + from nothing import do_nothing  # type: ignore[import]
26 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/TianGanDiZhi/gngan_yaljux.py:28:5
   |
27 |   try:
28 | /     from rich.console import Console
29 | |     from rich import print as rprint
   | |____________________________________^
30 |       USE_RICH = True
31 |       prt = rprint
   |
help: Organize imports
   |
28 |     from rich.console import Console
29 +
30 |     from rich import print as rprint
   |

DTZ002 `datetime.datetime.today()` used
  --> datetime/TianGanDiZhi/gngan_yaljux.py:43:12
   |
41 | def get_thisyear() -> int:
42 |     ''' get this year '''
43 |     return datetime.today().year
   |            ^^^^^^^^^^^^^^^^
44 |
45 | class GanChi:
   |
help: Use `datetime.datetime.now(tz=...)` instead

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/TianGanDiZhi/typer_gng.py:12:1
   |
10 |   '''
11 |
12 | / import sys
13 | | from typing import Union
14 | | from typing_extensions import Annotated
   | |_______________________________________^
15 |   try:
16 |       import typer
   |
help: Organize imports
   |
13 | from typing import Union
14 +
15 | from typing_extensions import Annotated
16 +
17 | try:
   |

UP035 [*] Import from `typing` instead: `Annotated`
  --> datetime/TianGanDiZhi/typer_gng.py:14:1
   |
12 | import sys
13 | from typing import Union
14 | from typing_extensions import Annotated
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
15 | try:
16 |     import typer
   |
help: Import from `typing`
   |
13 | from typing import Union
   - from typing_extensions import Annotated
14 + from typing import Annotated
15 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/TianGanDiZhi/typer_gng.py:21:1
   |
19 |     sys.exit(1)
20 |
21 | from rich.console import Console
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
22 | console = Console()
   |
help: Organize imports
   |
21 | from rich.console import Console
22 +
23 | console = Console()
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/TianGanDiZhi/typer_gng.py:24:1
   |
22 | console = Console()
23 |
24 | from gngan_yaljux import do_ab, do_tests, do_values, do_verbose
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 | # ruff: noqa: E402
26 | sys.path.insert(0, "..")
   |
help: Organize imports
   |
24 | from gngan_yaljux import do_ab, do_tests, do_values, do_verbose
25 +
26 | # ruff: noqa: E402
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> datetime/TianGanDiZhi/typer_gng.py:25:1
   |
24 | from gngan_yaljux import do_ab, do_tests, do_values, do_verbose
25 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
26 | sys.path.insert(0, "..")
27 | sys.path.insert(0, "TaiGanDiZhi/")
   |
help: Remove unused `noqa` directive
   |
24 | from gngan_yaljux import do_ab, do_tests, do_values, do_verbose
   - # ruff: noqa: E402
25 | sys.path.insert(0, "..")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/TianGanDiZhi/typer_gng.py:30:1
   |
28 |   sys.path.insert(0, "../datetime/")
29 |   sys.path.insert(0, "../../python3/datetime/")
30 | / from nothing import do_nothing  # type: ignore[import]
31 | | from be_prepared import get_thisyear, prepare_values  # type: ignore[import]
   | |____________________________________________________^
32 |
33 |   class Main:
   |
help: Organize imports
   |
29 | sys.path.insert(0, "../../python3/datetime/")
30 + from be_prepared import get_thisyear, prepare_values  # type: ignore[import]
31 | from nothing import do_nothing  # type: ignore[import]
   - from be_prepared import get_thisyear, prepare_values  # type: ignore[import]
32 |
33 +
34 | class Main:
   |

UP007 [*] Use `X | Y` for type annotations
  --> datetime/TianGanDiZhi/typer_gng.py:38:38
   |
36 |         self.logd = console.log
37 |
38 |     def main(self, values: Annotated[Union[list[int], None],
   |                                      ^^^^^^^^^^^^^^^^^^^^^^
39 |                                      typer.Argument(help="specify year")] = None,
40 |             after: Annotated[int,
   |
help: Convert to `X | Y`
   |
37 |
   -     def main(self, values: Annotated[Union[list[int], None],
38 +     def main(self, values: Annotated[list[int] | None,
39 |                                      typer.Argument(help="specify year")] = None,
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/be_prepared.py:9:1
   |
 7 | '''
 8 |
 9 | from datetime import date
   | ^^^^^^^^^^^^^^^^^^^^^^^^^
10 |
11 | def get_thisyear() -> int:
   |
help: Organize imports
   |
10 |
11 +
12 | def get_thisyear() -> int:
   |

DTZ011 `datetime.date.today()` used
  --> datetime/be_prepared.py:13:12
   |
11 | def get_thisyear() -> int:
12 |     ''' get this year '''
13 |     return date.today().year
   |            ^^^^^^^^^^^^
14 |
15 | def get_year_color(yy: int, target_year: int) -> str:
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

PERF402 Use `list` or `list.copy` to create a copy of a list
  --> datetime/be_prepared.py:47:9
   |
45 |     vals = []
46 |     for y in range(lower,upper+1):
47 |         vals.append(y)
   |         ^^^^^^^^^^^^^^
48 |     return vals
   |

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> datetime/between.py:16:17
   |
14 |     ww = [9, 21]
15 |     # here is time I enter workspace
16 |     from_time = datetime.now().replace(hour=ww[0], minute=ww[1], second=0, microsecond=0)
   |                 ^^^^^^^^^^^^^^
17 |     print('from_time:', from_time)
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> datetime/between.py:20:16
   |
19 |     # current time
20 |     now_time = datetime.now().replace(microsecond=0)
   |                ^^^^^^^^^^^^^^
21 |     print('now_time: ', now_time)
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> datetime/between.py:23:23
   |
21 |     print('now_time: ', now_time)
22 |
23 |     most_early_time = datetime.now().replace(hour=17, minute=30, second=0, microsecond=0)
   |                       ^^^^^^^^^^^^^^
24 |     #print most_early_time
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/black_friday.py:9:1
   |
 7 |   '''
 8 |
 9 | / from datetime import date
10 | | import sys
11 | | from typing import Optional, Annotated, Callable, Any
   | |_____________________________________________________^
12 |   try:
13 |       import typer
   |
help: Organize imports
   |
8  |
   - from datetime import date
9  | import sys
   - from typing import Optional, Annotated, Callable, Any
10 + from datetime import date
11 + from typing import Annotated, Any, Callable, Optional
12 +
13 | try:
   |

UP035 [*] Import from `collections.abc` instead: `Callable`
  --> datetime/black_friday.py:11:1
   |
 9 | from datetime import date
10 | import sys
11 | from typing import Optional, Annotated, Callable, Any
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
12 | try:
13 |     import typer
   |
help: Import from `collections.abc`
   |
10 | import sys
   - from typing import Optional, Annotated, Callable, Any
11 + from typing import Optional, Annotated, Any
12 + from collections.abc import Callable
13 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/black_friday.py:19:5
   |
17 |       USE_TYPER = False
18 |   try:
19 | /     from rich import print as rprint
20 | |     from rich.console import Console
21 | |     from rich.table import Table
   | |________________________________^
22 |       USE_RICH = True
23 |       console = Console()
   |
help: Organize imports
   |
18 | try:
   -     from rich import print as rprint
19 |     from rich.console import Console
20 |     from rich.table import Table
21 +
22 +     from rich import print as rprint
23 |     USE_RICH = True
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/black_friday.py:29:5
   |
27 |       print('import error of module rich', e)
28 |   try:
29 | /     from be_prepared import get_thisyear, prepare_values, get_year_color
30 | |     from nothing import do_nothing
   | |__________________________________^
31 |   except ImportError:
32 |       print('import error of be_prepared, please check the module')
   |
help: Organize imports
   |
28 | try:
   -     from be_prepared import get_thisyear, prepare_values, get_year_color
29 +     from be_prepared import get_thisyear, get_year_color, prepare_values
30 |     from nothing import do_nothing
   |

UP045 [*] Use `X | None` for type annotations
   --> datetime/black_friday.py:154:27
    |
152 |     # pylint: disable=too-many-positional-arguments
153 |     def main(
154 |         values: Annotated[Optional[list[int]],
    |                           ^^^^^^^^^^^^^^^^^^^
155 |             typer.Argument(help="specify year")] = None,
156 |         after: Annotated[int,
    |
help: Convert to `X | None`
    |
153 |     def main(
    -         values: Annotated[Optional[list[int]],
154 +         values: Annotated[list[int] | None,
155 |             typer.Argument(help="specify year")] = None,
    |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/calc-workdays.py:13:5
   |
12 |   try:
13 | /     from rich import print as rprint
14 | |     from rich.console import Console
   | |____________________________________^
15 |       console = Console()
16 |       logd = console.log
   |
help: Organize imports
   |
12 | try:
   -     from rich import print as rprint
13 |     from rich.console import Console
14 +
15 +     from rich import print as rprint
16 |     console = Console()
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/calc-workdays.py:23:5
   |
21 |   try:
22 |       sys.path.insert(0, "..")
23 | /     from myutil import read_jsonfile, DefaultConfig  # type: ignore[import]
24 | |     from myutil import is_leapyear, WhatNow, MyDebug, die  # type: ignore[import]
   | |_________________________________________________________^
25 |   except ImportError:
26 |       print("[FAIL] need myutil module from myutil package")
   |
help: Organize imports
   |
22 |     sys.path.insert(0, "..")
   -     from myutil import read_jsonfile, DefaultConfig  # type: ignore[import]
   -     from myutil import is_leapyear, WhatNow, MyDebug, die  # type: ignore[import]
23 +     from myutil import (  # type: ignore[import]  # type: ignore[import]
24 +         DefaultConfig,
25 +         MyDebug,
26 +         WhatNow,
27 +         die,
28 +         is_leapyear,
29 +         read_jsonfile,
30 +     )
31 | except ImportError:
   |

DTZ011 `datetime.date.today()` used
  --> datetime/calendar_demo.py:13:10
   |
11 |     print calendar of 3 months including current month
12 |     '''
13 |     td = date.today()
   |          ^^^^^^^^^^^^
14 |     #this_month = td.month
15 |     #print('this_month:', this_month)
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/clockemoji.py:7:1
   |
 5 |   '''
 6 |
 7 | / import sys
 8 | | import argparse
 9 | | from datetime import datetime
   | |_____________________________^
10 |   sys.path.insert(0, "..")
11 |   sys.path.insert(0, "python3")
   |
help: Organize imports
   |
6  |
7  + import argparse
8  | import sys
   - import argparse
9  | from datetime import datetime
10 +
11 | sys.path.insert(0, "..")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/clockemoji.py:12:1
   |
10 | sys.path.insert(0, "..")
11 | sys.path.insert(0, "python3")
12 | from myutil import prt  # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^
13 |
14 | class ShowClock:
   |
help: Organize imports
   |
13 |
14 +
15 | class ShowClock:
   |

RUF012 Mutable default value for class attribute
  --> datetime/clockemoji.py:16:14
   |
14 |   class ShowClock:
15 |       ''' class to show clock '''
16 |       clocks = {
   |  ______________^
17 | |         "0100": "🕐",
18 | |         "0200": "🕑",
19 | |         "0300": "🕒",
20 | |         "0400": "🕓",
21 | |         "0500": "🕔",
22 | |         "0600": "🕕",
23 | |         "0700": "🕖",
24 | |         "0800": "🕗",
25 | |         "0900": "🕘",
26 | |         "1000": "🕙",
27 | |         "1100": "🕚",
28 | |         "1200": "🕛",
29 | |         "0130": "🕜",
30 | |         "0230": "🕝",
31 | |         "0330": "🕞",
32 | |         "0430": "🕟",
33 | |         "0530": "🕠",
34 | |         "0630": "🕡",
35 | |         "0730": "🕢",
36 | |         "0830": "🕣",
37 | |         "0930": "🕤",
38 | |         "1030": "🕥",
39 | |         "1130": "🕦",
40 | |         "1230": "🕧",
41 | |     }
   | |_____^
42 |
43 |       def __init__(self, verbose=False):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> datetime/clockemoji.py:74:15
   |
72 |             mm (0 to 59)
73 |         '''
74 |         now = datetime.now()
   |               ^^^^^^^^^^^^^^
75 |         # Extract hour and minute
76 |         self.sethh(now.hour)
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

DTZ001 `datetime.datetime()` called without a `tzinfo` argument
  --> datetime/count_month.py:25:13
   |
23 | def main():
24 |     ''' main '''
25 |     start = datetime.datetime(2020, 12, 21)
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
26 |     i = 31
27 |     upper = 4*12
   |
help: Pass a `datetime.timezone` object to the `tzinfo` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/date_palidrome.py:7:1
   |
 5 |   '''
 6 |
 7 | / from datetime import date, timedelta
 8 | | import sys
   | |__________^
 9 |   sys.path.insert(0, "..")
10 |   sys.path.insert(0, "python3")
   |
help: Organize imports
   |
6  |
7  + import sys
8  | from datetime import date, timedelta
   - import sys
9  +
10 | sys.path.insert(0, "..")
   |

TRY004 Prefer `TypeError` exception for invalid type
  --> datetime/date_palidrome.py:17:9
   |
15 |     ''' the shortest way to test if palindrome '''
16 |     if not isinstance(the_str, str):
17 |         raise ValueError
   |         ^^^^^^^^^^^^^^^^
18 |     return the_str==the_str[::-1]
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/date_typer.py:10:1
   |
 8 |   '''
 9 |
10 | / from datetime import datetime
11 | | import sys
12 | | from typing import Union, Annotated
   | |___________________________________^
13 |   try:
14 |       import typer
   |
help: Organize imports
   |
9  |
   - from datetime import datetime
10 | import sys
   - from typing import Union, Annotated
11 + from datetime import datetime
12 + from typing import Annotated, Union
13 +
14 | try:
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> datetime/date_typer.py:22:1
   |
20 |                   help="epoch / timestamp utility",
21 |                   no_args_is_help=True)
22 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
23 | sys.path.insert(0, "..")
24 | sys.path.insert(0, "datetime")
   |
help: Remove unused `noqa` directive
   |
21 |                   no_args_is_help=True)
   - # ruff: noqa: E402
22 | sys.path.insert(0, "..")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/date_typer.py:27:1
   |
25 |   sys.path.insert(0, "myutil")
26 |   sys.path.insert(0, "python3/datetime")
27 | / from ep import epoch2timestr, datetime2epoch
28 | | from nothing import do_nothing
   | |______________________________^
29 |
30 |   def run_demo() -> None:
   |
help: Organize imports
   |
26 | sys.path.insert(0, "python3/datetime")
   - from ep import epoch2timestr, datetime2epoch
27 + from ep import datetime2epoch, epoch2timestr
28 | from nothing import do_nothing
29 |
30 +
31 | def run_demo() -> None:
   |

UP007 [*] Use `X | Y` for type annotations
  --> datetime/date_typer.py:55:9
   |
53 | def main(
54 |     dateval: Annotated[
55 |         Union[datetime, None],
   |         ^^^^^^^^^^^^^^^^^^^^^
56 |         typer.Option("--datetime", "--date", "-D",
57 |             formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
   |
help: Convert to `X | Y`
   |
54 |     dateval: Annotated[
   -         Union[datetime, None],
55 +         datetime | None,
56 |         typer.Option("--datetime", "--date", "-D",
   |

UP007 [*] Use `X | Y` for type annotations
  --> datetime/date_typer.py:59:23
   |
57 |             formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
58 |     ] = None, #"1970-01-01T00:00:00",
59 |     numval: Annotated[Union[int, None], typer.Option("--epoch", "--number", "-e", "-n",
   |                       ^^^^^^^^^^^^^^^^
60 |         help="epoch value in number")] = None, # 1234567890
61 |     debug: Annotated[bool, typer.Option("--debug", help="turn on debug")] = False,
   |
help: Convert to `X | Y`
   |
58 |     ] = None, #"1970-01-01T00:00:00",
   -     numval: Annotated[Union[int, None], typer.Option("--epoch", "--number", "-e", "-n",
59 +     numval: Annotated[int | None, typer.Option("--epoch", "--number", "-e", "-n",
60 |         help="epoch value in number")] = None, # 1234567890
   |

DTZ001 `datetime.datetime()` called without a `tzinfo` argument
  --> datetime/datedelta.py:14:13
   |
12 | def main():
13 |     ''' main '''
14 |     start = datetime(1975, 6, 17, 12, 0, 0)
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
15 |     print("start date:", start)
16 |     today = datetime.today()
   |
help: Pass a `datetime.timezone` object to the `tzinfo` parameter

DTZ002 `datetime.datetime.today()` used
  --> datetime/datedelta.py:16:13
   |
14 |     start = datetime(1975, 6, 17, 12, 0, 0)
15 |     print("start date:", start)
16 |     today = datetime.today()
   |             ^^^^^^^^^^^^^^^^
17 |     print('diff since start:', today - start)
   |
help: Use `datetime.datetime.now(tz=...)` instead

I001 [*] Import block is un-sorted or un-formatted
 --> datetime/dbetw.py:5:1
  |
3 |   ''' to calculate days between two dates '''
4 |
5 | / from datetime import date
6 | | import sys
  | |__________^
7 |   sys.path.insert(0, "../")
8 |   sys.path.insert(0, "python3/")
  |
help: Organize imports
  |
4 |
5 + import sys
6 | from datetime import date
  - import sys
7 +
8 | sys.path.insert(0, "../")
  |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/dbetw.py:9:1
   |
 7 | sys.path.insert(0, "../")
 8 | sys.path.insert(0, "python3/")
 9 | from myutil import prt  # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^
10 |
11 | class Solution:
   |
help: Organize imports
   |
10 |
11 +
12 | class Solution:
   |

DTZ011 `datetime.date.today()` used
  --> datetime/dbetw.py:47:34
   |
45 |     def get_today_str():
46 |         ''' get string of today '''
47 |         return Solution.date2str(date.today())
   |                                  ^^^^^^^^^^^^
48 |
49 |     @staticmethod
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

DTZ011 `datetime.date.today()` used
  --> datetime/dbetw.py:54:13
   |
52 |             eg: 2021-12-31
53 |         '''
54 |         t = date.today()
   |             ^^^^^^^^^^^^
55 |         nd = date(t.year, 12, 31)
56 |         return str(nd)
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

DTZ011 `datetime.date.today()` used
  --> datetime/dbetw.py:63:13
   |
61 |             eg: 2021-01-01
62 |         '''
63 |         t = date.today()
   |             ^^^^^^^^^^^^
64 |         nd = date(t.year, 1, 1)
65 |         return str(nd)
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/delta_seconds.py:7:1
   |
 5 |   '''
 6 |
 7 | / import argparse
 8 | | import datetime
   | |_______________^
 9 |   try:
10 |       from rich.console import Console
   |
help: Organize imports
   |
8  | import datetime
9  +
10 | try:
   |

DTZ001 `datetime.datetime()` called without a `tzinfo` argument
  --> datetime/delta_seconds.py:19:16
   |
17 |     ''' a class to calculate delta seconds '''
18 |     base = 2
19 |     birthday = datetime.datetime(1989, 6, 4, hour=12, minute=34)
   |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
20 |     base_start = 27
21 |     base_end = 31
   |
help: Pass a `datetime.timezone` object to the `tzinfo` parameter

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> datetime/delta_seconds.py:41:40
   |
39 |         for i in range(Solution.base_start, Solution.base_end + 1):
40 |             delta_time = Solution.get_delta(i)
41 |             delta_days = (delta_time - datetime.datetime.now()).days
   |                                        ^^^^^^^^^^^^^^^^^^^^^^^
42 |             table.add_row(str(i), str(delta_time), str(delta_days))
43 |         console.print(table)
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> datetime/delta_seconds.py:51:36
   |
49 |             result = Solution.get_delta(i)
50 |             # to get the delta days between today
51 |             delta_days = (result - datetime.datetime.now()).days
   |                                    ^^^^^^^^^^^^^^^^^^^^^^^
52 |             print('2 ^', i, ": ", result, "\t", delta_days)
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/dooms/doomsday.py:7:1
   |
 5 |   '''
 6 |
 7 | / import argparse
 8 | | import sys
 9 | | from datetime import date
   | |_________________________^
10 |   try:
11 |       # try to add my code snippet into python path
   |
help: Organize imports
   |
9  | from datetime import date
10 +
11 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/dooms/doomsday.py:15:5
   |
13 |     # sys.path.insert(0, '../../')
14 |     # sys.path.insert(0, 'python3/')
15 |     from be_prepared import prepare_values, get_year_color
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
16 | except ImportError:
17 |     print('cannot import be_prepared, exit')
   |
help: Organize imports
   |
14 |     # sys.path.insert(0, 'python3/')
   -     from be_prepared import prepare_values, get_year_color
15 +     from be_prepared import get_year_color, prepare_values
16 | except ImportError:
   |

DTZ011 `datetime.date.today()` used
  --> datetime/dooms/doomsday.py:43:14
   |
41 |     # else:
42 |     #     tdyear = year
43 |     tdyear = date.today().year if year <=0 else year
   |              ^^^^^^^^^^^^
44 |     ret = DoomsDay.get_month_modifier(tdyear)
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

DTZ011 `datetime.date.today()` used
  --> datetime/dooms/doomsday.py:72:18
   |
70 |         raise ValueError("year_range MUST NOT smaller than 0")
71 |
72 |     start_year = date.today().year if base_year <= 0 else base_year
   |                  ^^^^^^^^^^^^
73 |
74 |     answer = []
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/dooms/dow_caller.py:9:1
   |
 7 |   '''
 8 |
 9 | / import sys
10 | | from datetime import date
   | |_________________________^
11 |   try:
12 |       from dooms_day import DoomsDay
   |
help: Organize imports
   |
10 | from datetime import date
11 +
12 | try:
   |

DTZ011 `datetime.date.today()` used
  --> datetime/dooms/dow_caller.py:33:10
   |
31 |     ''' demo '''
32 |     prt('demo: Use date.today().weekday()...')
33 |     td = date.today()
   |          ^^^^^^^^^^^^
34 |     tdow = int(td.weekday() + 1) % 7  # calibrate to 0 is Sun, 6 is Sat
35 |     prt(f'today: {td}, dow: {tdow} ({TWS[tdow]})')
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/dooms/easydoom.py:43:1
   |
41 |   '''
42 |
43 | / import sys
44 | | from datetime import date
   | |_________________________^
45 |   try:
46 |       from rich import print as pprint
   |
help: Organize imports
   |
44 | from datetime import date
45 +
46 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/dooms/easydoom.py:46:5
   |
44 |   from datetime import date
45 |   try:
46 | /     from rich import print as pprint
47 | |     from rich.console import Console
48 | |     from rich.table import Table
   | |________________________________^
49 |       USE_RICH = True
50 |       console = Console()
   |
help: Organize imports
   |
45 | try:
   -     from rich import print as pprint
46 |     from rich.console import Console
47 |     from rich.table import Table
48 +
49 +     from rich import print as pprint
50 |     USE_RICH = True
   |

RUF012 Mutable default value for class attribute
  --> datetime/dooms/easydoom.py:64:14
   |
62 |   class EasyDoomsDay:
63 |       ''' utility functions to provide doomsday number '''
64 |       months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
   |  ______________^
65 | |               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
   | |_______________________________________________________^
66 |
67 |       def __init__(self):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

DTZ011 `datetime.date.today()` used
  --> datetime/dooms/easydoom.py:69:22
   |
67 |     def __init__(self):
68 |         ''' init '''
69 |         self.today = date.today()
   |                      ^^^^^^^^^^^^
70 |         self.this_year = self.today.year
71 |         self.modifer_year = 0
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/easter_date.py:11:1
   |
10 |   # datetime.datetime, datetime.date
11 | / from datetime import date
12 | | import sys
13 | | from typing import Optional, Annotated
   | |______________________________________^
14 |   try:
15 |       import typer
   |
help: Organize imports
   |
10 | # datetime.datetime, datetime.date
   - from datetime import date
11 | import sys
   - from typing import Optional, Annotated
12 + from datetime import date
13 + from typing import Annotated, Optional
14 +
15 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/easter_date.py:21:5
   |
19 |       print('warn: failed to import typer, only demo, no CLI...')
20 |   try:
21 | /     from rich import print as rprint
22 | |     from rich.console import Console
23 | |     from rich.table import Table
   | |________________________________^
24 |       USE_RICH = True
25 |       console = Console()
   |
help: Organize imports
   |
20 | try:
   -     from rich import print as rprint
21 |     from rich.console import Console
22 |     from rich.table import Table
23 +
24 +     from rich import print as rprint
25 |     USE_RICH = True
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/easter_date.py:31:5
   |
29 |     logd = print
30 | try:
31 |     from be_prepared import get_thisyear, prepare_values, get_year_color
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
32 |     #from nothing import do_nothing
33 | except ImportError:
   |
help: Organize imports
   |
30 | try:
   -     from be_prepared import get_thisyear, prepare_values, get_year_color
31 +     from be_prepared import get_thisyear, get_year_color, prepare_values
32 |     #from nothing import do_nothing
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E741`)
  --> datetime/easter_date.py:37:1
   |
35 |     sys.exit(1)
36 |
37 | # ruff: noqa: E741
   | ^^^^^^^^^^^^^^^^^^
38 | def calculate_easter(year: int) -> date:
39 |     ''' Calculate the date of Easter Sunday for the given year '''
   |
help: Remove unused `noqa` directive
   |
36 |
   - # ruff: noqa: E741
37 | def calculate_easter(year: int) -> date:
   |

UP045 [*] Use `X | None` for type annotations
   --> datetime/easter_date.py:123:32
    |
122 | if USE_TYPER:
123 |     def main(values: Annotated[Optional[list[int]],
    |                                ^^^^^^^^^^^^^^^^^^^
124 |                 typer.Argument(help="specify year")] = None,
125 |             after: Annotated[int,
    |
help: Convert to `X | None`
    |
122 | if USE_TYPER:
    -     def main(values: Annotated[Optional[list[int]],
123 +     def main(values: Annotated[list[int] | None,
124 |                 typer.Argument(help="specify year")] = None,
    |

UP035 `typing.Tuple` is deprecated, use `tuple` instead
  --> datetime/ep.py:44:1
   |
42 | import time
43 | from random import randint
44 | from typing import Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^
45 |
46 | sys.path.insert(0, '..')
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/ep.py:48:1
   |
46 | sys.path.insert(0, '..')
47 | sys.path.insert(0, 'python3')
48 | from myutil import read_from_stdin  # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
49 |
50 | def datetime2epoch(date_str: str) -> int:
   |
help: Organize imports
   |
49 |
50 +
51 | def datetime2epoch(date_str: str) -> int:
   |

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
  --> datetime/ep.py:56:53
   |
54 |     return calendar.timegm(time.strptime(date_str, '%Y-%m-%d %H:%M:%S'))
55 |
56 | def epoch2timestr(epoch: int, human: bool=False) -> Tuple[int, str]:
   |                                                     ^^^^^
57 |     ''' Replace time.localtime with time.gmtime for GMT time '''
58 |     if epoch == -1:
   |
help: Replace with `tuple`
   |
55 |
   - def epoch2timestr(epoch: int, human: bool=False) -> Tuple[int, str]:
56 + def epoch2timestr(epoch: int, human: bool=False) -> tuple[int, str]:
57 |     ''' Replace time.localtime with time.gmtime for GMT time '''
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/list_old_folder.py:8:1
   |
 8 | / from datetime import datetime
 9 | | from glob import glob
10 | | import os
11 | | import sys
12 | | import time
   | |___________^
13 |   sys.path.insert(0, '.')
14 |   sys.path.insert(0, '..')
   |
help: Organize imports
   |
7  |
   - from datetime import datetime
   - from glob import glob
8  | import os
9  | import sys
10 | import time
11 + from datetime import datetime
12 + from glob import glob
13 +
14 | sys.path.insert(0, '.')
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/list_old_folder.py:15:1
   |
13 | sys.path.insert(0, '.')
14 | sys.path.insert(0, '..')
15 | from myutil import prt  # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^
16 |
17 | class ShowDirList:
   |
help: Organize imports
   |
16 |
17 +
18 | class ShowDirList:
   |

DTZ006 `datetime.datetime.fromtimestamp()` called without a `tz` argument
  --> datetime/list_old_folder.py:64:62
   |
62 |         ''' show the older folders '''
63 |         ago = ShowDirList.get_older_epoch(days)
64 |         prt(f'> The folders are older than {days} days ago: {datetime.fromtimestamp(ago)}')
   |                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
65 |         ShowDirList.sep()
66 |         for d in self.dirs:
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

DTZ006 `datetime.datetime.fromtimestamp()` called without a `tz` argument
  --> datetime/list_old_folder.py:75:61
   |
73 |         ''' show the newer folders '''
74 |         ago = ShowDirList.get_older_epoch(days)
75 |         prt(f'> The folders are newer, within {days} days: {datetime.fromtimestamp(ago)}')
   |                                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
76 |         ShowDirList.sep()
77 |         for d in self.dirs:
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/list_possible_workday.py:29:1
   |
27 |   '''
28 |
29 | / import json
30 | | import os
31 | | import sys
32 | | from datetime import date, datetime, timedelta
33 | | from typing import Union, Annotated, Any, Callable, Optional
   | |____________________________________________________________^
34 |
35 |   typer: Any = None
   |
help: Organize imports
   |
32 | from datetime import date, datetime, timedelta
   - from typing import Union, Annotated, Any, Callable, Optional
33 + from typing import Annotated, Any, Callable, Optional, Union
34 |
   |

UP035 [*] Import from `collections.abc` instead: `Callable`
  --> datetime/list_possible_workday.py:33:1
   |
31 | import sys
32 | from datetime import date, datetime, timedelta
33 | from typing import Union, Annotated, Any, Callable, Optional
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
34 |
35 | typer: Any = None
   |
help: Import from `collections.abc`
   |
32 | from datetime import date, datetime, timedelta
   - from typing import Union, Annotated, Any, Callable, Optional
33 + from typing import Union, Annotated, Any, Optional
34 + from collections.abc import Callable
35 |
   |

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> datetime/list_possible_workday.py:65:12
   |
63 | def get_thisyear() -> int:
64 |     ''' return current year '''
65 |     return datetime.now().year
   |            ^^^^^^^^^^^^^^
66 |
67 | def print_stderr(*_args: Any, **_kwargs: Any) -> None:
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

DTZ007 Naive datetime constructed using `datetime.datetime.strptime()` without %z
   --> datetime/list_possible_workday.py:125:25
    |
123 |                 # transaform string to date object
124 |                 if d:
125 |                     d = datetime.strptime(d, "%Y-%m-%d").date()
    |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
126 |                 res.append(d)
127 |         return res
    |
help: Call `.replace(tzinfo=<timezone>)` or `.astimezone()` to convert to an aware datetime

DTZ005 `datetime.datetime.now()` called without a `tz` argument
   --> datetime/list_possible_workday.py:155:15
    |
153 |     def warn_if_olddate(self, the_d: datetime) -> None:
154 |         ''' warn if the input datetime is more than 3 months ago '''
155 |         now = datetime.now()
    |               ^^^^^^^^^^^^^^
156 |         three_months_ago = now - timedelta(days=90)
157 |         if the_d.date() < three_months_ago.date():
    |
help: Pass a `datetime.timezone` object to the `tz` parameter

DTZ002 `datetime.datetime.today()` used
   --> datetime/list_possible_workday.py:197:14
    |
195 |     def run_default(self) -> None:
196 |         ''' run default, without CLI options '''
197 |         td = datetime.today()
    |              ^^^^^^^^^^^^^^^^
198 |         default_yymm = td.strftime("%Y-%m")
199 |         print(f'[INFO] use default value: {default_yymm}')
    |
help: Use `datetime.datetime.now(tz=...)` instead

UP045 [*] Use `X | None` for type annotations
   --> datetime/list_possible_workday.py:209:31
    |
207 |         def main(self,
208 |             # input like: "1970-01"
209 |             yyyymm: Annotated[Optional[datetime],
    |                               ^^^^^^^^^^^^^^^^^^
210 |                 typer.Argument(help="specify a YYYY-mm date, the dd will be ignored",
211 |                         formats=["%Y-%m", "%Y-%m-%d"]),] = None,
    |
help: Convert to `X | None`
    |
208 |             # input like: "1970-01"
    -             yyyymm: Annotated[Optional[datetime],
209 +             yyyymm: Annotated[datetime | None,
210 |                 typer.Argument(help="specify a YYYY-mm date, the dd will be ignored",
    |

UP007 [*] Use `X | Y` for type annotations
   --> datetime/list_possible_workday.py:217:29
    |
215 |                 typer.Option("--next", "-n", help="Use next month", is_flag=True)] = False,
216 |             # output file name
217 |             outf: Annotated[Union[str, None],
    |                             ^^^^^^^^^^^^^^^^
218 |                 typer.Option("--out", "-o", help="output file name")] = None,
219 |             # show holidays for a specific year, default current year
    |
help: Convert to `X | Y`
    |
216 |             # output file name
    -             outf: Annotated[Union[str, None],
217 +             outf: Annotated[str | None,
218 |                 typer.Option("--out", "-o", help="output file name")] = None,
    |

UP045 [*] Use `X | None` for type annotations
   --> datetime/list_possible_workday.py:221:38
    |
219 |             # show holidays for a specific year, default current year
220 |             vacation: Annotated[bool, typer.Option("-v", "--vacation", help="Show vacation info, default is current year")] = False,
221 |             vacation_year: Annotated[Optional[int], typer.Option("--vacation-year", help="Must specify the year")] = None,
    |                                      ^^^^^^^^^^^^^
222 |             # debug mode
223 |             debug: Annotated[bool,
    |
help: Convert to `X | None`
    |
220 |             vacation: Annotated[bool, typer.Option("-v", "--vacation", help="Show vacation info, default is current year")] = False,
    -             vacation_year: Annotated[Optional[int], typer.Option("--vacation-year", help="Must specify the year")] = None,
221 +             vacation_year: Annotated[int | None, typer.Option("--vacation-year", help="Must specify the year")] = None,
222 |             # debug mode
    |

DTZ011 `datetime.date.today()` used
   --> datetime/list_possible_workday.py:255:25
    |
253 |             target_date = yyyymm
254 |             if target_date is None:
255 |                 today = date.today()
    |                         ^^^^^^^^^^^^
256 |                 if current_month:
257 |                     target_date = datetime(today.year, today.month, 1)
    |
help: Use `datetime.datetime.now(tz=...).date()` instead

DTZ001 `datetime.datetime()` called without a `tzinfo` argument
   --> datetime/list_possible_workday.py:257:35
    |
255 |                 today = date.today()
256 |                 if current_month:
257 |                     target_date = datetime(today.year, today.month, 1)
    |                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
258 |                 elif next_month:
259 |                     year = today.year + (1 if today.month == 12 else 0)
    |
help: Pass a `datetime.timezone` object to the `tzinfo` parameter

DTZ001 `datetime.datetime()` called without a `tzinfo` argument
   --> datetime/list_possible_workday.py:261:35
    |
259 |                     year = today.year + (1 if today.month == 12 else 0)
260 |                     month = 1 if today.month == 12 else today.month + 1
261 |                     target_date = datetime(year, month, 1)
    |                                   ^^^^^^^^^^^^^^^^^^^^^^^^
262 |
263 |             if target_date is None:
    |
help: Pass a `datetime.timezone` object to the `tzinfo` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/lunar_date.py:15:1
   |
14 |   #import datetime
15 | / import itertools as it
16 | | import sys
   | |__________^
17 |   try:
18 |       from rich import print as rprint
   |
help: Organize imports
   |
16 | import sys
17 +
18 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/lunar_date.py:29:5
   |
28 |   try:
29 | /     from lunarcalendar import Converter, DateNotExist, Lunar, Solar  # type: ignore[import]
30 | |     from lunarcalendar.festival import festivals  # type: ignore[import]
   | |________________________________________________^
31 |   except ImportError:
32 |       print('failed to import module lunarcalendar')
   |
help: Organize imports
   |
28 | try:
   -     from lunarcalendar import Converter, DateNotExist, Lunar, Solar  # type: ignore[import]
29 +     from lunarcalendar import (  # type: ignore[import]
30 +         Converter,
31 +         DateNotExist,
32 +         Lunar,
33 +         Solar,
34 +     )
35 |     from lunarcalendar.festival import festivals  # type: ignore[import]
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/new_date.py:7:1
   |
 5 |   '''
 6 |
 7 | / from datetime import datetime, timedelta
 8 | | from typing import Union, Annotated
   | |___________________________________^
 9 |   try:
10 |       import typer
   |
help: Organize imports
   |
7  | from datetime import datetime, timedelta
   - from typing import Union, Annotated
8  + from typing import Annotated, Union
9  +
10 | try:
   |

DTZ002 `datetime.datetime.today()` used
  --> datetime/new_date.py:37:13
   |
35 |     '''demo function'''
36 |     print("demo...")
37 |     start = datetime.today()
   |             ^^^^^^^^^^^^^^^^
38 |     delta = 60
39 |     get_result(start, delta)
   |
help: Use `datetime.datetime.now(tz=...)` instead

UP007 [*] Use `X | Y` for type annotations
  --> datetime/new_date.py:55:13
   |
53 |     def main(
54 |         dateval: Annotated[
55 |             Union[datetime, None],
   |             ^^^^^^^^^^^^^^^^^^^^^
56 |             typer.Option("--datetime", "--date", "-D",
57 |                 formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
   |
help: Convert to `X | Y`
   |
54 |         dateval: Annotated[
   -             Union[datetime, None],
55 +             datetime | None,
56 |             typer.Option("--datetime", "--date", "-D",
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/ngorgo.py:14:1
   |
12 |   '''
13 |
14 | / import argparse
15 | | import re
16 | | import os
17 | | import sys
18 | | from datetime import date, timedelta
   | |____________________________________^
19 |
20 |   SUCCESS = 0
   |
help: Organize imports
   |
14 | import argparse
15 + import os
16 | import re
   - import os
17 | import sys
   |

RUF012 Mutable default value for class attribute
  --> datetime/ngorgo.py:29:14
   |
27 |       TS = 'latest.txt'
28 |       MINDIFF = 5
29 |       months = ['Nul', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
   |  ______________^
30 | |         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
   | |_________________________________________________^
31 |       patterns = [
32 |           # 西元2023年12月15日 (週五) 13時57分07秒 CST
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

RUF012 Mutable default value for class attribute
  --> datetime/ngorgo.py:31:16
   |
29 |       months = ['Nul', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
30 |           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
31 |       patterns = [
   |  ________________^
32 | |         # 西元2023年12月15日 (週五) 13時57分07秒 CST
33 | |         r'^西元(\d{4})年(\d+)月(\d+)日.*$',
34 | |         # Tue, 12 Dec 2023 14:47:55 +0800
35 | |         r'^\w+,\s+(\d+)\s+(\w+)\s+(\d+) \d+:\d+:\d+ \+\d+$',
36 | |         # Tue Dec 12 15:10:30 CST 2023
37 | |         r'^\w+\s+(\w+)\s+(\d+)\s+\d+:\d+:\d+ \w+ (\d+)$',
38 | |     ]
   | |_____^
39 |
40 |       def __init__(self):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

DTZ011 `datetime.date.today()` used
   --> datetime/ngorgo.py:138:33
    |
136 |         self.parse_stampfile()
137 |         if self.lastdate:
138 |             if self.lastdate >= date.today() - self.offset:
    |                                 ^^^^^^^^^^^^
139 |                 self.show_msg(f'[INFO] {self.lastdate} rather new, no need to bother')
140 |                 sys.exit(NOTOLDENOUGH)
    |
help: Use `datetime.datetime.now(tz=...).date()` instead

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> datetime/nothing.py:9:5
   |
 7 | def do_nothing(*_args, **_wargs) -> None:
 8 |     ''' do nothing'''
 9 |     return None
   |     ^^^^^^^^^^^
10 |
11 | if __name__ == '__main__':
   |
help: Remove explicit `return None`
   |
8  |     ''' do nothing'''
   -     return None
9  +     return
10 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/perfect_square_date.py:12:1
   |
10 |   '''
11 |
12 | / from math import sqrt
13 | | import sys
   | |__________^
14 |   sys.path.insert(0, "..")
15 |   from myutil import is_leapyear  # type: ignore[import]
   |
help: Organize imports
   |
11 |
12 + import sys
13 | from math import sqrt
   - import sys
14 +
15 | sys.path.insert(0, "..")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/perfect_square_date.py:15:1
   |
13 | import sys
14 | sys.path.insert(0, "..")
15 | from myutil import is_leapyear  # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
16 |
17 | def logd(*args, **wargs):
   |
help: Organize imports
   |
16 |
17 +
18 | def logd(*args, **wargs):
   |

DTZ011 `datetime.date.today()` used
  --> datetime/ratio_month.py:55:26
   |
53 |             self.today = td
54 |         else:
55 |             self.today = date.today()
   |                          ^^^^^^^^^^^^
56 |         td = self.today
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/sickutil.py:11:1
   |
 9 |   '''
10 |
11 | / import math
12 | | import struct
13 | | import time
14 | | import logging
15 | | from datetime import datetime
16 | | from sysconfig import get_platform
   | |__________________________________^
17 |   #from nothing import do_nothing
   |
help: Organize imports
   |
10 |
11 + import logging
12 | import math
13 | import struct
14 | import time
   - import logging
15 | from datetime import datetime
16 | from sysconfig import get_platform
17 +
18 | #from nothing import do_nothing
   |

TRY004 Prefer `TypeError` exception for invalid type
  --> datetime/sickutil.py:45:9
   |
43 |     ''' sick to datetime '''
44 |     if not isinstance(sick, int):
45 |         raise ValueError('sick should be an int')
   |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
46 |     logd(f'----- sick_to_ns({sick}) -----')
47 |     hex_string = normalize_hex_str(hex(sick))
   |

TRY004 Prefer `TypeError` exception for invalid type
  --> datetime/sickutil.py:74:9
   |
72 |     ''' sick to datetime '''
73 |     if not isinstance(val, int):
74 |         raise ValueError
   |         ^^^^^^^^^^^^^^^^
75 |     logd(f'----- sick_to_datetime({val}) -----')
76 |     hex_string = normalize_hex_str(hex(val))
   |

DTZ006 `datetime.datetime.fromtimestamp()` called without a `tz` argument
   --> datetime/sickutil.py:99:10
    |
 97 |     str_val = str_val[:keep_len]
 98 |     logd(f'  {str_val=}')
 99 |     dt = datetime.fromtimestamp(int(str_val))
    |          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
100 |     return dt
    |
help: Pass a `datetime.timezone` object to the `tz` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/wtfstamp.py:21:1
   |
19 |   '''
20 |
21 | / from datetime import datetime
22 | | import time
23 | | import logging
   | |______________^
24 |   try:
25 |       from rich import print as rprint
   |
help: Organize imports
   |
20 |
   - from datetime import datetime
   - import time
21 | import logging
22 + import time
23 + from datetime import datetime
24 +
25 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/wtfstamp.py:25:5
   |
23 |   import logging
24 |   try:
25 | /     from rich import print as rprint
26 | |     from rich.console import Console
   | |____________________________________^
27 |       USE_RICH = True
28 |   except ImportError:
   |
help: Organize imports
   |
24 | try:
   -     from rich import print as rprint
25 |     from rich.console import Console
26 +
27 +     from rich import print as rprint
28 |     USE_RICH = True
   |

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/wtfstamp.py:30:1
   |
28 |   except ImportError:
29 |       USE_RICH = False
30 | / from sickutil import get_sick_from_ns
31 | | from sickutil import sick_to_ns, sick_to_datetime, datetime_to_sick
   | |___________________________________________________________________^
32 |
33 |   prt = rprint if USE_RICH else print
   |
help: Organize imports
   |
29 |     USE_RICH = False
   - from sickutil import get_sick_from_ns
   - from sickutil import sick_to_ns, sick_to_datetime, datetime_to_sick
30 + from sickutil import datetime_to_sick, get_sick_from_ns, sick_to_datetime, sick_to_ns
31 |
   |

DTZ001 `datetime.datetime()` called without a `tzinfo` argument
  --> datetime/wtfstamp.py:45:15
   |
43 |     def get_range(self):
44 |         ''' get range '''
45 |         dt1 = datetime(2024,8,21,0,0,0)
   |               ^^^^^^^^^^^^^^^^^^^^^^^^^
46 |         self.min_epoch = dt1.timestamp()
47 |         dt2 = datetime(2024,8,29,23,59,59)
   |
help: Pass a `datetime.timezone` object to the `tzinfo` parameter

DTZ001 `datetime.datetime()` called without a `tzinfo` argument
  --> datetime/wtfstamp.py:47:15
   |
45 |         dt1 = datetime(2024,8,21,0,0,0)
46 |         self.min_epoch = dt1.timestamp()
47 |         dt2 = datetime(2024,8,29,23,59,59)
   |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
48 |         self.max_epoch = dt2.timestamp()
   |
help: Pass a `datetime.timezone` object to the `tzinfo` parameter

DTZ001 `datetime.datetime()` called without a `tzinfo` argument
   --> datetime/wtfstamp.py:142:27
    |
140 |     ''' 1e9 loop '''
141 |     obj = Solution()
142 |     d1 = datetime_to_sick(datetime(2024, 8, 21, 20, 36))
    |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
143 |     #d2 = datetime_to_sick(datetime(2024, 8, 27, 13, 22))
144 |     for i in range(1, 1_000_000_000):
    |
help: Pass a `datetime.timezone` object to the `tzinfo` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> datetime/yesterday.py:11:1
   |
11 | / import time
12 | | from datetime import datetime, timedelta
   | |________________________________________^
13 |   try:
14 |       from rich import print as pprint
   |
help: Organize imports
   |
12 | from datetime import datetime, timedelta
13 +
14 | try:
   |

DTZ006 `datetime.datetime.fromtimestamp()` called without a `tz` argument
  --> datetime/yesterday.py:22:13
   |
20 |     '''main function'''
21 |     # get current time
22 |     today = datetime.fromtimestamp(time.time())
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
23 |     today = today.replace(microsecond=0)  # remove microsecond part
24 |     prt(f"current time from time stamp: {today}")
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> demo_pushover/base_pushover.py:17:1
   |
16 | sys.path.insert(0, "..")
17 | from myutil import read_jsonfile, MyDebug, DefaultConfig
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
help: Organize imports
   |
16 | sys.path.insert(0, "..")
   - from myutil import read_jsonfile, MyDebug, DefaultConfig
17 + from myutil import DefaultConfig, MyDebug, read_jsonfile
18 |
   |

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> demo_pushover/base_pushover.py:34:37
   |
32 |         # default data fields
33 |         self._title = 'pushover.py'
34 |         self._message = f'{msg} at {datetime.now()}'
   |                                     ^^^^^^^^^^^^^^
35 |         self.resp_str = None
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> demo_pushover/p2over.py:10:1
   |
 8 |   '''
 9 |
10 | / import json
11 | | import sys
12 | | from random import choice
13 | | from time import time
14 | | import requests
15 | | from base_pushover import PushOverBase
   | |______________________________________^
16 |   sys.path.insert(0, "..")
17 |   from myutil import read_jsonfile
   |
help: Organize imports
   |
13 | from time import time
14 +
15 | import requests
16 | from base_pushover import PushOverBase
17 +
18 | sys.path.insert(0, "..")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> demo_pushover/p3over.py:10:1
   |
 8 |   '''
 9 |
10 | / import http.client
11 | | import urllib
12 | | from datetime import datetime
13 | | from base_pushover import PushOverBase
   | |______________________________________^
   |
help: Organize imports
   |
12 | from datetime import datetime
13 +
14 | from base_pushover import PushOverBase
   -
15 |
   |

DTZ002 `datetime.datetime.today()` used
  --> demo_pushover/p3over.py:60:14
   |
58 |     def run(cls):
59 |         ''' run '''
60 |         ts = datetime.today().strftime('%a %d %b %Y, %H:%M') # Wed 24 May 2023, 14:49
   |              ^^^^^^^^^^^^^^^^
61 |         # strftime('%Y-%m-%d %H:%M:%S')  '2023-05-24 14:50:25'
62 |         msg = f'notification on {ts} via urllib'
   |
help: Use `datetime.datetime.now(tz=...)` instead

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> demo_pushover/pushover.py:22:1
   |
20 | from datetime import datetime
21 |
22 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
23 | sys.path.insert(0, "./")
24 | sys.path.insert(0, "../")
   |
help: Remove unused `noqa` directive
   |
21 |
   - # ruff: noqa: E402
22 | sys.path.insert(0, "./")
   |

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> demo_pushover/pushover.py:44:50
   |
42 |         (self.userkey, self.apitoken) = self.get_apikey()
43 |         self.title = 'pushover.py'
44 |         self.message = f'{get_host()}: {msg} at {datetime.now()}'
   |                                                  ^^^^^^^^^^^^^^
45 |
46 |     def __str__(self):
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> demo_pushover/request-soundlist.py:12:1
   |
10 |   '''
11 |
12 | / import argparse
13 | | import json
14 | | import os
15 | | import sys
16 | | import requests
   | |_______________^
17 |
18 |   # ruff: noqa: E402
   |
help: Organize imports
   |
15 | import sys
16 +
17 | import requests
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> demo_pushover/request-soundlist.py:18:1
   |
16 | import requests
17 |
18 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
19 | sys.path.insert(0, "./")
20 | sys.path.insert(0, "../")
   |
help: Remove unused `noqa` directive
   |
17 |
   - # ruff: noqa: E402
18 | sys.path.insert(0, "./")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> demo_pushover/request-soundlist.py:22:1
   |
20 |   sys.path.insert(0, "../")
21 |   sys.path.insert(0, "python3/")
22 | / from base_pushover import PushOverBase
23 | | from myutil import read_jsonfile
   | |________________________________^
   |
help: Organize imports
   |
22 | from base_pushover import PushOverBase
23 +
24 | from myutil import read_jsonfile
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> demo_pushover/yagmail_send_pushover.py:33:1
   |
31 |     return path
32 |
33 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
34 | sys.path.insert(0, "./")
35 | sys.path.insert(0, "../")
   |
help: Remove unused `noqa` directive
   |
32 |
   - # ruff: noqa: E402
33 | sys.path.insert(0, "./")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> demo_pushover/yagmail_send_pushover.py:37:1
   |
35 | sys.path.insert(0, "../")
36 | sys.path.insert(0, "python3/")
37 | from myutil import isfile, read_jsonfile
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
38 |
39 | def main():
   |
help: Organize imports
   |
38 |
39 +
40 | def main():
   |

I001 [*] Import block is un-sorted or un-formatted
  --> dice.py:11:1
   |
 9 |   '''
10 |
11 | / import time
12 | | from random import randint
13 | | import matplotlib.pyplot as plt
14 | | import numpy as np
   | |__________________^
15 |   #import seaborn as sns
16 |   try:
   |
help: Organize imports
   |
12 | from random import randint
13 +
14 | import matplotlib.pyplot as plt
15 +
16 | import numpy as np
17 +
18 | #import seaborn as sns
   |

I001 [*] Import block is un-sorted or un-formatted
 --> emoji/food/clean_from.py:7:1
  |
5 | '''
6 |
7 | import re
  | ^^^^^^^^^
8 |
9 | class Cleanup:
  |
help: Organize imports
   |
8  |
9  +
10 | class Cleanup:
   |

SIM117 Use a single `with` statement with multiple contexts instead of nested `with` statements
  --> emoji/food/clean_from.py:19:9
   |
17 |       def action(self):
18 |           ''' action '''
19 | /         with open(self.fn, 'rt', encoding='UTF-8') as fobj:
20 | |             with open(self.ofn, 'wt', encoding='UTF-8') as fout:
   | |________________________________________________________________^
21 |                   for ln in fobj:
22 |                       ln = ln.strip()
   |
help: Combine `with` statements

I001 [*] Import block is un-sorted or un-formatted
  --> emoji/food/lookup.py:14:1
   |
12 |   sys.path.insert(0, "..")
13 |   sys.path.insert(0, "../..")
14 | / from myutil import is_file, read_textfile, die
15 | | from en_emoji import EMOJI
   | |__________________________^
   |
help: Organize imports
   |
13 | sys.path.insert(0, "../..")
   - from myutil import is_file, read_textfile, die
14 | from en_emoji import EMOJI
15 |
16 + from myutil import die, is_file, read_textfile
17 +
18 |
   |

RUF012 Mutable default value for class attribute
  --> emoji/food/lookup.py:31:13
   |
29 |     '''
30 |     foods_file = "foods.txt"
31 |     files = ["foods.txt", "sorted.txt"]
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
32 |
33 |     def __init__(self):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

I001 [*] Import block is un-sorted or un-formatted
 --> emoji/logd.py:6:1
  |
4 |   '''
5 |
6 | / import sys
7 | | from rich.console import Console
  | |________________________________^
8 |   error_console = Console(stderr=True, style="bold red")
  |
help: Organize imports
   |
6  | import sys
7  +
8  | from rich.console import Console
9  +
10 | error_console = Console(stderr=True, style="bold red")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> emoji/mytofrom.py:7:1
   |
 5 |   '''
 6 |
 7 | / import binascii as bi
 8 | | import json
 9 | | from logd import logd
   | |_____________________^
10 |
11 |   __version__ = '0.1'
   |
help: Organize imports
   |
8  | import json
9  +
10 | from logd import logd
   |

TRY004 Prefer `TypeError` exception for invalid type
  --> emoji/mytofrom.py:49:9
   |
47 |         ret = cc.decode('utf-8')
48 |     else:
49 |         raise ValueError("need input bytes")
   |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
50 |     return ret
   |

I001 [*] Import block is un-sorted or un-formatted
  --> emoji/parse_enxml.py:10:1
   |
 8 |   '''
 9 |
10 | / import re
11 | | import sys
12 | | from datetime import datetime
   | |_____________________________^
13 |   try:
14 |       from bs4 import BeautifulSoup
   |
help: Organize imports
   |
12 | from datetime import datetime
13 +
14 | try:
   |

DTZ002 `datetime.datetime.today()` used
  --> emoji/parse_enxml.py:24:13
   |
23 | # header for generated python file
24 | timestamp = datetime.today()
   |             ^^^^^^^^^^^^^^^^
25 | HEADER='''
26 | # coding: utf-8
   |
help: Use `datetime.datetime.now(tz=...)` instead

SIM103 Return the condition `"skin_tone" in k` directly
  --> emoji/parse_enxml.py:65:9
   |
63 |           if k in black_set:
64 |               return True
65 | /         if "skin_tone" in k:
66 | |             return True
67 | |         return False
   | |____________________^
68 |
69 |       def make_soup(self, the_dict: dict) -> None:
   |
help: Replace with `return "skin_tone" in k`

UP018 [*] Unnecessary `str` call (rewrite as a literal)
   --> emoji/parse_enxml.py:119:13
    |
117 |     def value_to_string(v: list) -> list:
118 |         ''' value to string '''
119 |         s = str()
    |             ^^^^^
120 |         for i in v:
121 |             s += '"' + i + '"' + ','
    |
help: Replace with string literal
    |
118 |         ''' value to string '''
    -         s = str()
119 +         s = ''
120 |         for i in v:
    |

I001 [*] Import block is un-sorted or un-formatted
  --> emoji/pickup.py:10:1
   |
 8 | '''
 9 |
10 | import sys
   | ^^^^^^^^^^
11 | sys.path.insert(0, "..")
12 | from myutil import is_file, read_textfile, die
   |
help: Organize imports
   |
10 | import sys
11 +
12 | sys.path.insert(0, "..")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> emoji/pickup.py:12:1
   |
10 |   import sys
11 |   sys.path.insert(0, "..")
12 | / from myutil import is_file, read_textfile, die
13 | | from en_emoji import EMOJI
14 | | from logd import logd
   | |_____________________^
15 |   try:
16 |       from fuzzywuzzy import fuzz
   |
help: Organize imports
   |
11 | sys.path.insert(0, "..")
   - from myutil import is_file, read_textfile, die
12 | from en_emoji import EMOJI
13 | from logd import logd
14 +
15 + from myutil import die, is_file, read_textfile
16 +
17 | try:
   |

RUF012 Mutable default value for class attribute
  --> emoji/read_enxml.py:28:13
   |
26 |       ''' solution to read en.xml and output as csv-like data '''
27 |
28 |       FILES = ['en-basic.xml', 'en-derived.xml',
   |  _____________^
29 | |             'zh-basic.xml', 'zh-derived.xml']
   | |_____________________________________________^
30 |
31 |       def __init__(self):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

UP018 [*] Unnecessary `str` call (rewrite as a literal)
  --> emoji/read_enxml.py:64:13
   |
62 |     def value_to_string(v: list) -> list:
63 |         ''' value to string '''
64 |         s = str()
   |             ^^^^^
65 |         for i in v:
66 |             s += '"' + i + '"' + ','
   |
help: Replace with string literal
   |
63 |         ''' value to string '''
   -         s = str()
64 +         s = ''
65 |         for i in v:
   |

DTZ011 `datetime.date.today()` used
  --> emoji/read_enxml.py:94:13
   |
92 | def get_datetag() -> str:
93 |     ''' string in UMMDD '''
94 |     today = date.today()
   |             ^^^^^^^^^^^^
95 |     s = f'U{today.month:02d}{today.day:02d}'
96 |     return s
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

I001 [*] Import block is un-sorted or un-formatted
 --> emoji/test_loge.py:5:1
  |
3 | '''
4 |
5 | from logd import loge
  | ^^^^^^^^^^^^^^^^^^^^^
6 |
7 | def main():
  |
help: Organize imports
  |
6 |
7 +
8 | def main():
  |

I001 [*] Import block is un-sorted or un-formatted
  --> emoji/u8u16.py:10:1
   |
 8 |   '''
 9 |
10 | / import json
11 | | import sys
12 | | from logd import logd
13 | | from mytofrom import to_from_u8, to_from_u16, to_utf8
   | |_____________________________________________________^
14 |
15 |   sys.path.insert(0, "..")
   |
help: Organize imports
   |
11 | import sys
12 +
13 | from logd import logd
   |

I001 [*] Import block is un-sorted or un-formatted
 --> euc_dist.py:5:1
  |
3 | ''' euclidean distance '''
4 |
5 | import numpy as np
  | ^^^^^^^^^^^^^^^^^^
6 | USE_RICH = False
7 | try:
  |
help: Organize imports
  |
5 | import numpy as np
6 +
7 | USE_RICH = False
  |

RUF012 Mutable default value for class attribute
  --> exiftool/exif.py:26:15
   |
24 |   class Solution:
25 |       ''' solution for extract GPS '''
26 |       queries = ["EXIF:GPSLatitude", "EXIF:GPSLatitudeRef",
   |  _______________^
27 | |                "EXIF:GPSLongitude", "EXIF:GPSLongitudeRef"]
   | |___________________________________________________________^
28 |
29 |       def __init__(self, conf):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  --> exiftool/get-date.py:16:9
   |
14 |     cnt = 0
15 |     for f in files:
16 |         cnt += 1
   |         ^^^^^^^^
17 |         d = os.path.getmtime(f)
18 |         print(d)
   |

I001 [*] Import block is un-sorted or un-formatted
  --> extfactor.py:8:1
   |
 6 |   '''
 7 |
 8 | / import argparse
 9 | | import os
10 | | import re
11 | | import sys
12 | | import time
13 | | from random import randint
14 | | from myutil import read_from_stdin, isfile
   | |__________________________________________^
15 |
16 |   def is_positive_integer(the_input):
   |
help: Organize imports
   |
13 | from random import randint
   - from myutil import read_from_stdin, isfile
14 |
15 + from myutil import isfile, read_from_stdin
16 +
17 +
18 | def is_positive_integer(the_input):
   |

I001 [*] Import block is un-sorted or un-formatted
  --> fastapi/api1st.py:16:1
   |
14 |   '''
15 |
16 | / import sys
17 | | from time import time
18 | | from typing import Union, List, Optional
19 | |
20 | | from fastapi import FastAPI
21 | | from pydantic import BaseModel
22 | | import numpy as np
23 | | import numpy_financial as npf
   | |_____________________________^
24 |
25 |   # ruff: noqa: E402
   |
help: Organize imports
   |
17 | from time import time
   - from typing import Union, List, Optional
18 + from typing import List, Optional, Union
19 |
   - from fastapi import FastAPI
20 + import numpy_financial as npf
21 | from pydantic import BaseModel
22 +
23 | import numpy as np
   - import numpy_financial as npf
24 + from fastapi import FastAPI
25 |
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> fastapi/api1st.py:18:1
   |
16 | import sys
17 | from time import time
18 | from typing import Union, List, Optional
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
19 |
20 | from fastapi import FastAPI
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> fastapi/api1st.py:25:1
   |
23 | import numpy_financial as npf
24 |
25 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
26 | sys.path.insert(0, "../")
27 | sys.path.insert(0, "python3/")
   |
help: Remove unused `noqa` directive
   |
24 |
   - # ruff: noqa: E402
25 | sys.path.insert(0, "../")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> fastapi/api1st.py:28:1
   |
26 | sys.path.insert(0, "../")
27 | sys.path.insert(0, "python3/")
28 | from myutil import prt
   | ^^^^^^^^^^^^^^^^^^^^^^
29 | sys.path.insert(0, "../../prime/")
30 | from is_prime import is_prime
   |
help: Organize imports
   |
28 | from myutil import prt
29 +
30 | sys.path.insert(0, "../../prime/")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> fastapi/api1st.py:30:1
   |
28 | from myutil import prt
29 | sys.path.insert(0, "../../prime/")
30 | from is_prime import is_prime
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
31 | sys.path.insert(0, "../datetime/")
32 | sys.path.insert(0, "../datetime/dooms/")
   |
help: Organize imports
   |
30 | from is_prime import is_prime
31 +
32 | sys.path.insert(0, "../datetime/")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> fastapi/api1st.py:34:1
   |
32 |   sys.path.insert(0, "../datetime/dooms/")
33 |   sys.path.insert(0, "python3/datetime/dooms/")
34 | / from dooms_day import DoomsDay
35 | | from be_prepared import prepare_values
   | |______________________________________^
36 |
37 |   app = FastAPI()
   |
help: Organize imports
   |
33 | sys.path.insert(0, "python3/datetime/dooms/")
34 + from be_prepared import prepare_values
35 | from dooms_day import DoomsDay
   - from be_prepared import prepare_values
36 |
   |

UP045 [*] Use `X | None` for type annotations
  --> fastapi/api1st.py:59:12
   |
57 |     ''' give year and abc '''
58 |     value: int  # required field
59 |     after: Optional[int] = 0   # optional field
   |            ^^^^^^^^^^^^^
60 |     before: Optional[int] = 0
61 |     context: Optional[int] = 0
   |
help: Convert to `X | None`
   |
58 |     value: int  # required field
   -     after: Optional[int] = 0   # optional field
59 +     after: int | None = 0   # optional field
60 |     before: Optional[int] = 0
   |

UP045 [*] Use `X | None` for type annotations
  --> fastapi/api1st.py:60:13
   |
58 |     value: int  # required field
59 |     after: Optional[int] = 0   # optional field
60 |     before: Optional[int] = 0
   |             ^^^^^^^^^^^^^
61 |     context: Optional[int] = 0
   |
help: Convert to `X | None`
   |
59 |     after: Optional[int] = 0   # optional field
   -     before: Optional[int] = 0
60 +     before: int | None = 0
61 |     context: Optional[int] = 0
   |

UP045 [*] Use `X | None` for type annotations
  --> fastapi/api1st.py:61:14
   |
59 |     after: Optional[int] = 0   # optional field
60 |     before: Optional[int] = 0
61 |     context: Optional[int] = 0
   |              ^^^^^^^^^^^^^
62 |
63 | @app.put("/dooms/{item_id}")
   |
help: Convert to `X | None`
   |
60 |     before: Optional[int] = 0
   -     context: Optional[int] = 0
61 +     context: int | None = 0
62 |
   |

UP006 [*] Use `list` instead of `List` for type annotation
   --> fastapi/api1st.py:145:14
    |
143 | class GivenNumbers(BaseModel):
144 |     ''' data class '''
145 |     numbers: List[int]
    |              ^^^^
146 |
147 | @app.put("/checkprime/{item_id}")
    |
help: Replace with `list`
    |
144 |     ''' data class '''
    -     numbers: List[int]
145 +     numbers: list[int]
146 |
    |

RUF013 PEP 484 prohibits implicit `Optional`
   --> fastapi/api1st.py:172:33
    |
170 |     return ret
171 |
172 | def prepare_ints(v: int, after: int=None, before: int=None, radius: int=None) -> List[int]:
    |                                 ^^^
173 |     ''' prepare ints '''
174 |     after = 0 if after is None else after
    |
help: Convert to `T | None`

RUF013 PEP 484 prohibits implicit `Optional`
   --> fastapi/api1st.py:172:51
    |
170 |     return ret
171 |
172 | def prepare_ints(v: int, after: int=None, before: int=None, radius: int=None) -> List[int]:
    |                                                   ^^^
173 |     ''' prepare ints '''
174 |     after = 0 if after is None else after
    |
help: Convert to `T | None`

RUF013 PEP 484 prohibits implicit `Optional`
   --> fastapi/api1st.py:172:69
    |
170 |     return ret
171 |
172 | def prepare_ints(v: int, after: int=None, before: int=None, radius: int=None) -> List[int]:
    |                                                                     ^^^
173 |     ''' prepare ints '''
174 |     after = 0 if after is None else after
    |
help: Convert to `T | None`

UP006 [*] Use `list` instead of `List` for type annotation
   --> fastapi/api1st.py:172:82
    |
170 |     return ret
171 |
172 | def prepare_ints(v: int, after: int=None, before: int=None, radius: int=None) -> List[int]:
    |                                                                                  ^^^^
173 |     ''' prepare ints '''
174 |     after = 0 if after is None else after
    |
help: Replace with `list`
    |
171 |
    - def prepare_ints(v: int, after: int=None, before: int=None, radius: int=None) -> List[int]:
172 + def prepare_ints(v: int, after: int=None, before: int=None, radius: int=None) -> list[int]:
173 |     ''' prepare ints '''
    |

PERF402 Use `list` or `list.copy` to create a copy of a list
   --> fastapi/api1st.py:185:9
    |
183 |     vals = []
184 |     for y in range(lower,upper+1):
185 |         vals.append(y)
    |         ^^^^^^^^^^^^^^
186 |     return vals
    |

UP007 [*] Use `X | Y` for type annotations
   --> fastapi/api1st.py:204:34
    |
203 | @app.get("/isprime/{item_id}")
204 | def the_isprime(item_id: int, q: Union[str, None] = None):
    |                                  ^^^^^^^^^^^^^^^^
205 |     '''
206 |     if item_id is 33865, check the prime number from parameter
    |
help: Convert to `X | Y`
    |
203 | @app.get("/isprime/{item_id}")
    - def the_isprime(item_id: int, q: Union[str, None] = None):
204 + def the_isprime(item_id: int, q: str | None = None):
205 |     '''
    |

I001 [*] Import block is un-sorted or un-formatted
  --> fastapi/trylog.py:7:1
   |
 5 |   '''
 6 |
 7 | / from datetime import date
 8 | | from pydantic import BaseModel
 9 | | from loguru import logger
   | |_________________________^
10 |
11 |   logd = logger.debug
   |
help: Organize imports
   |
7  | from datetime import date
   - from pydantic import BaseModel
8  +
9  | from loguru import logger
10 + from pydantic import BaseModel
11 |
   |

FURB167 [*] Use of regular expression alias `re.M`
  --> fbkey.py:31:50
   |
29 |     if DEBUG:
30 |         print("program output:", out)
31 |     reg = re.compile(r'([0-9A-Fa-f]{5,})', flags=re.M)
   |                                                  ^^^^
32 |     m = reg.search(out)
33 |     if m:
   |
help: Replace with `re.MULTILINE`
   |
30 |         print("program output:", out)
   -     reg = re.compile(r'([0-9A-Fa-f]{5,})', flags=re.M)
31 +     reg = re.compile(r'([0-9A-Fa-f]{5,})', flags=re.MULTILINE)
32 |     m = reg.search(out)
   |

I001 [*] Import block is un-sorted or un-formatted
  --> fetch_currency.py:8:1
   |
 7 | # pip install requests
 8 | import requests
   | ^^^^^^^^^^^^^^^
 9 |
10 | def main():
   |
help: Organize imports
   |
9  |
10 +
11 | def main():
   |

RUF059 Unpacked variable `fig` is never used
  --> fft/dft1.py:41:5
   |
39 |     #     matplotlib.use('TkAgg')
40 |
41 |     fig, ax = plt.subplots()
   |     ^^^
42 |     ax.plot(t, x)
43 |     ax.set_xlabel('Time [s]')
   |
help: Prefix it with an underscore or any other dummy variable pattern

RUF059 Unpacked variable `fig` is never used
  --> fft/dft2.py:37:5
   |
35 |     #     matplotlib.use('TkAgg')
36 |
37 |     fig, ax = plt.subplots()
   |     ^^^
38 |     ax.stem(freqs, np.abs(X), use_line_collection=True)
39 |     ax.set_xlabel('Frequency in Hertz [Hz]')
   |
help: Prefix it with an underscore or any other dummy variable pattern

I001 [*] Import block is un-sorted or un-formatted
  --> fft/hann.py:7:1
   |
 5 |   '''
 6 |
 7 | / import matplotlib.pyplot as plt
 8 | |
 9 | | import numpy as np
10 | | from numpy.fft import fft, fftshift
   | |___________________________________^
   |
help: Organize imports
   |
7  | import matplotlib.pyplot as plt
8  + from numpy.fft import fft, fftshift
9  |
10 | import numpy as np
   - from numpy.fft import fft, fftshift
11 |
   |

RUF059 Unpacked variable `f` is never used
  --> fft/night.py:63:5
   |
61 |     spectrum = np.abs(spectrum)
62 |
63 |     f, ax = plt.subplots(figsize=(8, 4))
   |     ^
64 |     S = np.abs(spectrum)
65 |     print(f'np.max: {np.max(S)}')
   |
help: Prefix it with an underscore or any other dummy variable pattern

I001 [*] Import block is un-sorted or un-formatted
  --> fib/calc_factorial.py:7:1
   |
 5 |   '''
 6 |
 7 | / import pickle
 8 | | import sys
 9 | | #import random
10 | | from math import ceil, log10
   | |____________________________^
   |
help: Organize imports
   |
8  | import sys
9  +
10 | #import random
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> fib/factorial-redis.py:23:1
   |
21 | import redis
22 |
23 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
24 | sys.path.insert(0, '.')
25 | sys.path.insert(0, '..')
   |
help: Remove unused `noqa` directive
   |
22 |
   - # ruff: noqa: E402
23 | sys.path.insert(0, '.')
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> fib/fib-redis.py:24:1
   |
22 | import redis
23 |
24 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
25 | sys.path.insert(0, '.')
26 | sys.path.insert(0, '..')
   |
help: Remove unused `noqa` directive
   |
23 |
   - # ruff: noqa: E402
24 | sys.path.insert(0, '.')
   |

I001 [*] Import block is un-sorted or un-formatted
  --> fib/fib.py:14:1
   |
12 |   '''
13 |
14 | / from timeit import default_timer
15 | | from datetime import datetime
16 | | from socket import gethostname
   | |______________________________^
17 |   try:
18 |       from rich.console import Console
   |
help: Organize imports
   |
13 |
   - from timeit import default_timer
14 | from datetime import datetime
15 | from socket import gethostname
16 + from timeit import default_timer
17 +
18 | try:
   |

DTZ002 `datetime.datetime.today()` used
  --> fib/fib.py:33:10
   |
31 | def prepare_msg(duration: float, ulimit: int) -> None:
32 |     ''' prepare message '''
33 |     dt = datetime.today().strftime('%Y-%m-%d')
   |          ^^^^^^^^^^^^^^^^
34 |     hostname = gethostname()
35 |     msg = f'{dt} Host({hostname}) takes {duration:.3f} seconds to get fib({ulimit})'
   |
help: Use `datetime.datetime.now(tz=...)` instead

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> fib/fib_store.py:30:5
   |
28 | def do_nothing(*_args, **_wargs) -> None:
29 |     ''' do nothing '''
30 |     return None
   |     ^^^^^^^^^^^
31 |
32 | DEBUG = True
   |
help: Remove explicit `return None`
   |
29 |     ''' do nothing '''
   -     return None
30 +     return
31 |
   |

UP024 [*] Replace aliased errors with `OSError`
  --> fib/fib_store.py:89:16
   |
87 |             with open(self.pfile, "rb") as inf:
88 |                 self.fibvalues = pickle.load(inf)
89 |         except IOError:
   |                ^^^^^^^
90 |             # not a fatal exception
91 |             print(f'warn: IOError while opening {self.pfile}')
   |
help: Replace `IOError` with builtin `OSError`
   |
88 |                 self.fibvalues = pickle.load(inf)
   -         except IOError:
89 +         except OSError:
90 |             # not a fatal exception
   |

UP024 [*] Replace aliased errors with `OSError`
  --> fib/listp.py:37:12
   |
35 |                 else:
36 |                     print()
37 |     except IOError as e:
   |            ^^^^^^^
38 |         print('IOError:', e)
   |
help: Replace `IOError` with builtin `OSError`
   |
36 |                     print()
   -     except IOError as e:
37 +     except OSError as e:
38 |         print('IOError:', e)
   |

SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  --> fib/loadp.py:22:17
   |
20 |             cnt = 0
21 |             for k,v in mydata.items():
22 |                 cnt += 1
   |                 ^^^^^^^^
23 |                 if cnt > nitem:
24 |                     break
   |

UP024 [*] Replace aliased errors with `OSError`
  --> fib/loadp.py:26:12
   |
24 |                     break
25 |                 print(k, v)
26 |     except IOError as e:
   |            ^^^^^^^
27 |         print('IOError:', e)
   |
help: Replace `IOError` with builtin `OSError`
   |
25 |                 print(k, v)
   -     except IOError as e:
26 +     except OSError as e:
27 |         print('IOError:', e)
   |

PIE808 [*] Unnecessary `start` argument in `range`
  --> fisher_yates_shuffle.py:24:23
   |
22 |     # R1721: Unnecessary use of a comprehension (unnecessary-comprehension)
23 |     #return [i for i in range(0, max_size)]
24 |     return list(range(0, max_size))
   |                       ^
25 |
26 | def show_array(arr):
   |
help: Remove `start` argument
   |
23 |     #return [i for i in range(0, max_size)]
   -     return list(range(0, max_size))
24 +     return list(range(max_size))
25 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> foobar.py:7:1
   |
 5 |   '''
 6 |
 7 | / import os
 8 | | import sys
   | |__________^
 9 |   try:
10 |       sys.path.insert(0, ".")
   |
help: Organize imports
   |
8  | import sys
9  +
10 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> foobar.py:13:5
   |
11 |       sys.path.insert(0, "..")
12 |       sys.path.insert(0, "myutil")
13 | /     from myutil import get_dow, get_doom_num, get_epoch, WhatNow
14 | |     from myutil import is_windows, is_cygwin, get_platform
   | |__________________________________________________________^
15 |   except ImportError as e:
16 |       print(f'ImportError: {e}')
   |
help: Organize imports
   |
12 |     sys.path.insert(0, "myutil")
   -     from myutil import get_dow, get_doom_num, get_epoch, WhatNow
   -     from myutil import is_windows, is_cygwin, get_platform
13 +     from myutil import (
14 +         WhatNow,
15 +         get_doom_num,
16 +         get_dow,
17 +         get_epoch,
18 +         get_platform,
19 +         is_cygwin,
20 +         is_windows,
21 +     )
22 | except ImportError as e:
   |

I001 [*] Import block is un-sorted or un-formatted
 --> get_word_freq.py:5:1
  |
3 |   ''' get_word_freq from files '''
4 |
5 | / import sys
6 | | import re
7 | | from operator import itemgetter
  | |_______________________________^
8 |
9 |   def readfile(f):
  |
help: Organize imports
   |
4  |
5  + import re
6  | import sys
   - import re
7  | from operator import itemgetter
8  |
9  +
10 | def readfile(f):
   |

I001 [*] Import block is un-sorted or un-formatted
  --> guess_filetype.py:7:1
   |
 5 |   '''
 6 |
 7 | / import sys
 8 | | from myutil import read_from_stdin, isfile
   | |__________________________________________^
 9 |
10 |   try:
   |
help: Organize imports
   |
7  | import sys
   - from myutil import read_from_stdin, isfile
8  |
9  + from myutil import isfile, read_from_stdin
10 +
11 | try:
   |

UP012 [*] Unnecessary call to `encode` as UTF-8
  --> hash_factory.py:35:11
   |
33 | def test():
34 |     ''' main '''
35 |     MSG = 'hello world'.encode('UTF-8')
   |           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
36 |     # will throw an exception here
37 |     #get_hash(MSG, 'NO_ALGORITHM')
   |
help: Rewrite as bytes literal
   |
34 |     ''' main '''
   -     MSG = 'hello world'.encode('UTF-8')
35 +     MSG = b'hello world'
36 |     # will throw an exception here
   |

I001 [*] Import block is un-sorted or un-formatted
 --> hello_world.py:7:1
  |
5 | '''
6 |
7 | import sys
  | ^^^^^^^^^^
8 |
9 | def get_python_version():
  |
help: Organize imports
   |
8  |
9  +
10 | def get_python_version():
   |

I001 [*] Import block is un-sorted or un-formatted
  --> image/blobid.py:11:1
   |
 9 |   '''
10 |
11 | / import os
12 | | import sys
13 | |
14 | | from wand.image import Image as WandImage  # type: ignore[import]
15 | | from get_home import get_home
   | |_____________________________^
   |
help: Organize imports
   |
13 |
14 + from get_home import get_home
15 | from wand.image import Image as WandImage  # type: ignore[import]
   - from get_home import get_home
16 |
   |

RUF012 Mutable default value for class attribute
  --> image/blobid.py:36:13
   |
34 | class Solution:
35 |     ''' class solution '''
36 |     files = ['bmp3870.bmp', 'map3850.tif', 'shoelace-knot.png', 'img2668.jpg']
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
37 |
38 |     def __init__(self):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

I001 [*] Import block is un-sorted or un-formatted
 --> image/get_home.py:6:1
  |
4 | '''
5 |
6 | import os
  | ^^^^^^^^^
7 |
8 | def get_home() -> str:
  |
help: Organize imports
  |
7 |
8 +
9 | def get_home() -> str:
  |

I001 [*] Import block is un-sorted or un-formatted
  --> image/iterfiles.py:8:1
   |
 6 |   '''
 7 |
 8 | / import os
 9 | | import sys
10 | | from pathlib import Path
   | |________________________^
11 |   try:
12 |       from loguru import logger  # type: ignore[import]
   |
help: Organize imports
   |
10 | from pathlib import Path
11 +
12 | try:
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> image/iterfiles.py:17:1
   |
15 |     logd = print
16 |
17 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
18 | sys.path.insert(0, '.')
19 | sys.path.insert(0, '..')
   |
help: Remove unused `noqa` directive
   |
16 |
   - # ruff: noqa: E402
17 | sys.path.insert(0, '.')
   |

I001 [*] Import block is un-sorted or un-formatted
  --> image/iterfiles.py:21:1
   |
19 | sys.path.insert(0, '..')
20 | sys.path.insert(0, 'python3/')
21 | from myutil import prt, get_home  # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
help: Organize imports
   |
20 | sys.path.insert(0, 'python3/')
   - from myutil import prt, get_home  # type: ignore[import]
21 + from myutil import get_home, prt  # type: ignore[import]
22 |
   |

SIM102 Use a single `if` statement instead of nested `if` statements
  --> image/iterfiles.py:42:13
   |
40 |                   prt(f"too many > {self.LIMIT} directories has space, exit...")
41 |                   break
42 | /             if not p.is_file():
43 | |                 if ' ' in str(p):
   | |_________________________________^
44 |                       cnt += 1
45 |                       print('[WARN] space in path:', p)
   |
help: Combine `if` statements using `and`

I001 [*] Import block is un-sorted or un-formatted
  --> image/side-by-side.py:20:1
   |
20 | / import os
21 | | import sys
22 | | from wand.display import display  # type: ignore[import]
23 | | from wand.image import Image      # type: ignore[import]
24 | | from get_home import get_home
   | |_____________________________^
   |
help: Organize imports
   |
21 | import sys
   - from wand.display import display  # type: ignore[import]
   - from wand.image import Image      # type: ignore[import]
22 +
23 | from get_home import get_home
24 + from wand.display import display  # type: ignore[import]
25 + from wand.image import Image  # type: ignore[import]
26 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> image/top-down.py:20:1
   |
18 |   '''
19 |
20 | / import os
21 | | import sys
22 | |
23 | | from wand.display import display  # type: ignore[import]
24 | | from wand.image import Image  # type: ignore[import]
25 | | from get_home import get_home
   | |_____________________________^
   |
help: Organize imports
   |
22 |
23 + from get_home import get_home
24 | from wand.display import display  # type: ignore[import]
25 | from wand.image import Image  # type: ignore[import]
   - from get_home import get_home
26 |
   |

RUF012 Mutable default value for class attribute
  --> innprod.py:13:13
   |
11 |       ''' solution '''
12 |
13 |       names = [
   |  _____________^
14 | |         "0050", "0056", "006208", "00692", "00713",
15 | |         "00850", "00878", "00919", "00929", "2885",
16 | |         "2886", "2891", "4938", "5880"
17 | |     ]
   | |_____^
18 |
19 |       p10 = [
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

RUF012 Mutable default value for class attribute
  --> innprod.py:19:11
   |
17 |       ]
18 |
19 |       p10 = [
   |  ___________^
20 | |         121.15, 32.69, 70.1, 30.33, 46.02,
21 | |         32.13, 19.5, 20.19, 17.08, 24.3,
22 | |         36.7, 24.35, 75.4, 25.15]
   | |_________________________________^
23 |       p11 = [
24 |           131.35, 35.08, 74.95, 31.68, 49.58,
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

RUF012 Mutable default value for class attribute
  --> innprod.py:23:11
   |
21 |           32.13, 19.5, 20.19, 17.08, 24.3,
22 |           36.7, 24.35, 75.4, 25.15]
23 |       p11 = [
   |  ___________^
24 | |         131.35, 35.08, 74.95, 31.68, 49.58,
25 | |         34.05, 20.59, 21.65, 18.32, 26,
26 | |         39.5, 27.35, 81.2, 26.95]
   | |_________________________________^
27 |       nums = [
28 |           0, 30_000, 0, 0, 0,
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

RUF012 Mutable default value for class attribute
  --> innprod.py:27:12
   |
25 |           34.05, 20.59, 21.65, 18.32, 26,
26 |           39.5, 27.35, 81.2, 26.95]
27 |       nums = [
   |  ____________^
28 | |         0, 30_000, 0, 0, 0,
29 | |         22_000, 55_000, 0, 0, 20_000,
30 | |         27_000, 12_000, 9_000, 35_000
31 | |     ]
   | |_____^
32 |
33 |       def __init__(self):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

I001 [*] Import block is un-sorted or un-formatted
  --> kana/iroha.py:38:1
   |
36 | '''
37 |
38 | from ab import hira1d
   | ^^^^^^^^^^^^^^^^^^^^^
39 |
40 | def main():
   |
help: Organize imports
   |
39 |
40 +
41 | def main():
   |

RUF012 Mutable default value for class attribute
  --> kana/kana.py:33:14
   |
31 |     afn = 'Lowercase.txt'
32 |     Afn = 'Capital.txt'
33 |     magics = [5,5,5,5,5,5,5,5,5,5,1,99]
   |              ^^^^^^^^^^^^^^^^^^^^^^^^^^
34 |
35 |     def __init__(self):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

I001 [*] Import block is un-sorted or un-formatted
  --> kana/kanji/kjutil.py:7:1
   |
 5 |   '''
 6 |
 7 | / from datetime import date
 8 | | from decimal import Decimal
 9 | | from random import randint
10 | | import locale
   | |_____________^
11 |
12 |   try:
   |
help: Organize imports
   |
6  |
7  + import locale
8  | from datetime import date
9  | from decimal import Decimal
10 | from random import randint
   - import locale
11 |
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> kana/kanji/kjutil.py:20:5
   |
18 | def do_nothing(*_args, **_wargs) -> None:
19 |     ''' do nothing '''
20 |     return None
   |     ^^^^^^^^^^^
21 |
22 | REAL_COMPAIN = False
   |
help: Remove explicit `return None`
   |
19 |     ''' do nothing '''
   -     return None
20 +     return
21 |
   |

DTZ011 `datetime.date.today()` used
  --> kana/kanji/kjutil.py:28:13
   |
26 | def get_datetag() -> str:
27 |     ''' string in UYYMMDD '''
28 |     today = date.today()
   |             ^^^^^^^^^^^^
29 |     yy = today.year - 2000
30 |     s = f'U{yy:02d}{today.month:02d}{today.day:02d}-{randint(0,99999):05d}'
   |
help: Use `datetime.datetime.now(tz=...).date()` instead

I001 [*] Import block is un-sorted or un-formatted
 --> kana/kanji/loadyaml.py:5:1
  |
3 | ''' loading yaml '''
4 |
5 | import yaml
  | ^^^^^^^^^^^
6 |
7 | def main():
  |
help: Organize imports
  |
6 |
7 +
8 | def main():
  |

I001 [*] Import block is un-sorted or un-formatted
  --> kana/kanji/roast.py:10:1
   |
 8 |   '''
 9 |
10 | / import re
11 | | import json
12 | | from kjutil import logd
   | |_______________________^
13 |
14 |   FN = "raw.txt"
   |
help: Organize imports
   |
9  |
10 + import json
11 | import re
   - import json
12 +
13 | from kjutil import logd
   |

PERF402 Use `list` or `list.copy` to create a copy of a list
  --> kana/kanji/roast.py:33:13
   |
31 |         m = re.findall(r'(.)\s*', ln)
32 |         for c in m:
33 |             chars.append(c)
   |             ^^^^^^^^^^^^^^^
34 |         return chars
   |

PERF102 When using only the values of a dict use the `values()` method
  --> kana/kanji/roast.py:63:20
   |
61 |         total_in_k = 0
62 |         cnt = 0
63 |         for _,v in self.a_dict.items():
   |                    ^^^^^^^^^^^^^^^^^
64 |             #logd(f'{cnt}: {k}')
65 |             total_in_k += len(v)
   |
help: Replace `.items()` with `.values()`

SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  --> kana/kanji/roast.py:66:13
   |
64 |             #logd(f'{cnt}: {k}')
65 |             total_in_k += len(v)
66 |             cnt += 1
   |             ^^^^^^^^
67 |         logd(f'the total chars: {total_in_k}')
   |

I001 [*] Import block is un-sorted or un-formatted
  --> montyhall.py:33:1
   |
31 |   '''
32 |
33 | / from random import randint
34 | | from time import time
   | |_____________________^
35 |   try:
36 |       from rich import print as rprint
   |
help: Organize imports
   |
34 | from time import time
35 +
36 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> montyhall.py:36:5
   |
34 |   from time import time
35 |   try:
36 | /     from rich import print as rprint
37 | |     from rich.progress import Progress
   | |______________________________________^
38 |       USE_RICH = True
39 |   except ImportError:
   |
help: Organize imports
   |
35 | try:
   -     from rich import print as rprint
36 |     from rich.progress import Progress
37 +
38 +     from rich import print as rprint
39 |     USE_RICH = True
   |

I001 [*] Import block is un-sorted or un-formatted
  --> myip.py:8:1
   |
 6 |   '''
 7 |
 8 | / import argparse
 9 | | import json
10 | | from typing import Union
11 | | import requests
   | |_______________^
12 |
13 |   DEBUG = True
   |
help: Organize imports
   |
10 | from typing import Union
11 +
12 | import requests
   |

I001 [*] Import block is un-sorted or un-formatted
  --> myip.py:16:5
   |
14 |   USE_RICH = False
15 |   try:
16 | /     from rich import print_json
17 | |     from rich import print as rprint
   | |____________________________________^
18 |       #from rich.console import Console
19 |       USE_RICH = True
   |
help: Organize imports
   |
15 | try:
16 +     from rich import print as rprint
17 |     from rich import print_json
   -     from rich import print as rprint
18 |     #from rich.console import Console
   |

UP007 [*] Use `X | Y` for type annotations
  --> myip.py:62:33
   |
60 |             prt(d)
61 |
62 |     def get_current_ip(self) -> Union[str, None]:
   |                                 ^^^^^^^^^^^^^^^^
63 |         ''' use this to get myip '''
64 |         url = 'https://api.myip.com'
   |
help: Convert to `X | Y`
   |
61 |
   -     def get_current_ip(self) -> Union[str, None]:
62 +     def get_current_ip(self) -> str | None:
63 |         ''' use this to get myip '''
   |

UP007 [*] Use `X | Y` for type annotations
  --> myip.py:77:30
   |
75 |             return None
76 |
77 |     def get_ip_info(self, ip:Union[str, None]) -> None:
   |                              ^^^^^^^^^^^^^^^^
78 |         ''' use this to get IP location and related data '''
79 |         if ip is None:
   |
help: Convert to `X | Y`
   |
76 |
   -     def get_ip_info(self, ip:Union[str, None]) -> None:
77 +     def get_ip_info(self, ip:str | None) -> None:
78 |         ''' use this to get IP location and related data '''
   |

I001 [*] Import block is un-sorted or un-formatted
  --> myutil/__init__.py:14:1
   |
12 |   __VERSION__ = '2024.11.26'
13 |
14 | / from .commonutil import clamp
15 | | from .commonutil import get_home, print_stderr, read_from_stdin
16 | | from .commonutil import is_path_exist, isfile, isdir, mkdir
17 | | from .debug_verbose import MyDebug, MyVerbose, die, prt
18 | | from .hashutil import md5sum, sha1sum, sha256sum, sha384sum, sha512sum, sha3_256sum, sha3_512sum
19 | | from .jsonutil import read_setting, read_textfile, read_jsonfile, write_jsonfile
20 | | from .mydateutil import get_dow, is_leapyear, get_offset_from_year, get_doom_num
21 | | from .pathutil import DefaultConfig
22 | | from .queryutil import query_url_for_data, query_url_for_json
23 | | from .run_cmd import run_command, run_command2, show_platform
24 | | from .thedatetime import get_epoch, WhatNow
25 | | from .versionutil import get_python_version, get_python_versions, require_python_version
26 | | from .__myutil import is_linux, is_cygwin, is_windows, get_platform
   | |___________________________________________________________________^
27 |
28 |   def sep():
   |
help: Organize imports
   |
13 |
   - from .commonutil import clamp
   - from .commonutil import get_home, print_stderr, read_from_stdin
   - from .commonutil import is_path_exist, isfile, isdir, mkdir
14 + from .__myutil import get_platform, is_cygwin, is_linux, is_windows
15 + from .commonutil import (
16 +     clamp,
17 +     get_home,
18 +     is_path_exist,
19 +     isdir,
20 +     isfile,
21 +     mkdir,
22 +     print_stderr,
23 +     read_from_stdin,
24 + )
25 | from .debug_verbose import MyDebug, MyVerbose, die, prt
   - from .hashutil import md5sum, sha1sum, sha256sum, sha384sum, sha512sum, sha3_256sum, sha3_512sum
   - from .jsonutil import read_setting, read_textfile, read_jsonfile, write_jsonfile
   - from .mydateutil import get_dow, is_leapyear, get_offset_from_year, get_doom_num
26 + from .hashutil import (
27 +     md5sum,
28 +     sha1sum,
29 +     sha3_256sum,
30 +     sha3_512sum,
31 +     sha256sum,
32 +     sha384sum,
33 +     sha512sum,
34 + )
35 + from .jsonutil import read_jsonfile, read_setting, read_textfile, write_jsonfile
36 + from .mydateutil import get_doom_num, get_dow, get_offset_from_year, is_leapyear
37 | from .pathutil import DefaultConfig
38 | from .queryutil import query_url_for_data, query_url_for_json
39 | from .run_cmd import run_command, run_command2, show_platform
   - from .thedatetime import get_epoch, WhatNow
40 + from .thedatetime import WhatNow, get_epoch
41 | from .versionutil import get_python_version, get_python_versions, require_python_version
   - from .__myutil import is_linux, is_cygwin, is_windows, get_platform
42 |
43 +
44 | def sep():
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> myutil/__init__.py:34:5
   |
32 | def do_nothing(*_args, **_wargs) -> None:
33 |     ''' do nothing '''
34 |     return None
   |     ^^^^^^^^^^^
35 |
36 | is_file = isfile
   |
help: Remove explicit `return None`
   |
33 |     ''' do nothing '''
   -     return None
34 +     return
35 |
   |

RUF022 [*] `__all__` is not sorted
  --> myutil/__init__.py:40:11
   |
39 |   # sort by alphatic if possible
40 |   __all__ = [
   |  ___________^
41 | |     'clamp',
42 | |     'die',
43 | |     'do_nothing',
44 | |     'get_dow',
45 | |     'get_doom_num',
46 | |     'get_epoch',
47 | |     'get_home',
48 | |     'get_offset_from_year',
49 | |     'get_platform',
50 | |     'get_python_version',
51 | |     'get_python_versions',
52 | |     'is_cygwin',
53 | |     'is_dir',
54 | |     'is_file',
55 | |     'is_leapyear',
56 | |     'is_linux',
57 | |     'is_path_exist',
58 | |     'is_windows',
59 | |     'isdir',
60 | |     'isfile',
61 | |     'md5sum',
62 | |     'mkdir',
63 | |     'print_stderr',
64 | |     'prt',
65 | |     'query_url_for_data',
66 | |     'query_url_for_json',
67 | |     'read_from_stdin',
68 | |     'read_jsonfile',
69 | |     'read_textfile',
70 | |     'read_setting',
71 | |     'require_python_version',
72 | |     'run_command',
73 | |     'run_command2',
74 | |     'sha1sum',
75 | |     'sha256sum',
76 | |     'sha384sum',
77 | |     'sha512sum',
78 | |     'sha3_256sum',
79 | |     'sha3_512sum',
80 | |     'show_platform',
81 | |     'write_jsonfile',
82 | |     'DefaultConfig',
83 | |     'MyDebug',
84 | |     'MyVerbose',
85 | |     'WhatNow'
86 | | ]
   | |_^
   |
help: Apply an isort-style sorting to `__all__`
   |
40 | __all__ = [
41 +     'DefaultConfig',
42 +     'MyDebug',
43 +     'MyVerbose',
44 +     'WhatNow',
45 |     'clamp',
46 |     'die',
47 |     'do_nothing',
   -     'get_dow',
48 |     'get_doom_num',
49 +     'get_dow',
50 |     'get_epoch',
--------------------------------------------------------------------------------
72 |     'read_jsonfile',
73 +     'read_setting',
74 |     'read_textfile',
   -     'read_setting',
75 |     'require_python_version',
76 |     'run_command',
77 |     'run_command2',
78 |     'sha1sum',
79 +     'sha3_256sum',
80 +     'sha3_512sum',
81 |     'sha256sum',
82 |     'sha384sum',
83 |     'sha512sum',
   -     'sha3_256sum',
   -     'sha3_512sum',
84 |     'show_platform',
   -     'write_jsonfile',
   -     'DefaultConfig',
   -     'MyDebug',
   -     'MyVerbose',
   -     'WhatNow'
85 +     'write_jsonfile'
86 | ]
   |

I001 [*] Import block is un-sorted or un-formatted
  --> myutil/hashutil.py:16:1
   |
14 |   __VERSION__ = '2024.03.28'
15 |
16 | / import os
17 | | import hashlib
   | |______________^
18 |
19 |   def hash_factory(fn: str, hash_func) -> str:
   |
help: Organize imports
   |
15 |
16 + import hashlib
17 | import os
   - import hashlib
18 |
19 +
20 | def hash_factory(fn: str, hash_func) -> str:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> myutil/jsonutil.py:9:1
   |
 7 |   __VERSION__ = "2024.03.28"
 8 |
 9 | / import json
10 | | from .commonutil import isfile
   | |______________________________^
11 |
12 |   def read_jsonfile(fn:str, debug: bool=False) -> Any:
   |
help: Organize imports
   |
9  | import json
10 +
11 | from .commonutil import isfile
12 |
13 +
14 | def read_jsonfile(fn:str, debug: bool=False) -> Any:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> myutil/pathutil.py:8:1
   |
 6 |   '''
 7 |
 8 | / import os
 9 | | from .debug_verbose import MyDebug
   | |__________________________________^
10 |
11 |   __MODULE__ = "DefaultConfig"
   |
help: Organize imports
   |
8  | import os
9  +
10 | from .debug_verbose import MyDebug
   |

I001 [*] Import block is un-sorted or un-formatted
 --> myutil/queryutil.py:6:1
  |
4 |   '''
5 |
6 | / import json
7 | | import urllib.request
  | |_____________________^
8 |
9 |   def query_url_for_data(url: str, debug: bool=False):
  |
help: Organize imports
   |
8  |
9  +
10 | def query_url_for_data(url: str, debug: bool=False):
   |

I001 [*] Import block is un-sorted or un-formatted
  --> myutil/run_cmd.py:8:1
   |
 6 |   '''
 7 |
 8 | / import subprocess
 9 | | import sys
10 | | from sysconfig import get_platform
   | |__________________________________^
11 |   try:
12 |       from rich import print as rprint
   |
help: Organize imports
   |
10 | from sysconfig import get_platform
11 +
12 | try:
   |

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> myutil/thedatetime.py:32:11
   |
30 |         what now
31 |     '''
32 |     now = datetime.now()
   |           ^^^^^^^^^^^^^^
33 |     # Extract hour and minute
34 |     print(f'{now.year=}')   # date +%Y
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> myutil/thedatetime.py:52:13
   |
50 |     def _setup(self):
51 |         ''' fill up the data members '''
52 |         t = datetime.now()
   |             ^^^^^^^^^^^^^^
53 |         self.year = t.year
54 |         self.month = t.month
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

YTT204 `sys.version_info.minor` compared to integer (python4), compare `sys.version_info` to tuple
  --> myutil/versionutil.py:38:40
   |
36 | def need_python36() -> None:
37 |     ''' if not python version >= 3.6, raise exception '''
38 |     if sys.version_info.major == 3 and sys.version_info.minor >= 6:
   |                                        ^^^^^^^^^^^^^^^^^^^^^^
39 |         pass
40 |     else:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> np_genrandom_std.py:24:1
   |
22 |   '''
23 |
24 | / import time
25 | | from typing import Any
26 | | import numpy as np
27 | | from myutil import do_nothing
   | |_____________________________^
28 |
29 |   try:
   |
help: Organize imports
   |
25 | from typing import Any
26 +
27 | import numpy as np
   |

I001 [*] Import block is un-sorted or un-formatted
  --> numpy/arr.py:7:1
   |
 5 |   '''
 6 |
 7 | / from timeit import default_timer
 8 | | import asyncio
 9 | | import concurrent
10 | | import numpy as np
11 | | from rich.console import Console
   | |________________________________^
12 |
13 |   MAXCNT = 500_000_000
   |
help: Organize imports
   |
6  |
   - from timeit import default_timer
7  | import asyncio
8  | import concurrent
   - import numpy as np
9  + from timeit import default_timer
10 +
11 | from rich.console import Console
12 |
13 + import numpy as np
14 +
15 | MAXCNT = 500_000_000
   |

I001 [*] Import block is un-sorted or un-formatted
  --> numpy/ndist.py:15:1
   |
15 | / import sys
16 | | import time
17 | | from typing import Annotated
18 | | import numpy as np
19 | | from pydantic import BaseModel
20 | | import typer
   | |____________^
21 |
22 |   sys.path.insert(0, "./")
   |
help: Organize imports
   |
17 | from typing import Annotated
18 +
19 + import typer
20 + from pydantic import BaseModel
21 +
22 | import numpy as np
   - from pydantic import BaseModel
   - import typer
23 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> numpy/ndist.py:25:1
   |
23 | sys.path.insert(0, "../")
24 | sys.path.insert(0, "python/")
25 | from myutil import prt, read_jsonfile  # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
26 |
27 | class Dist(BaseModel):
   |
help: Organize imports
   |
26 |
27 +
28 | class Dist(BaseModel):
   |

I001 [*] Import block is un-sorted or un-formatted
  --> numpy/normal_dist.py:15:1
   |
15 | / import argparse
16 | | import sys
17 | | import numpy as np
   | |__________________^
18 |
19 |   CANNOT_DRAW = False
   |
help: Organize imports
   |
16 | import sys
17 +
18 | import numpy as np
   |

I001 [*] Import block is un-sorted or un-formatted
  --> numpy/np_pmt.py:9:1
   |
 7 |   '''
 8 |
 9 | / import sys
10 | | from typing import Annotated
11 | | import numpy_financial as npf  # type: ignore[import]
12 | | from pydantic import BaseModel
   | |______________________________^
13 |   try:
14 |       import typer
   |
help: Organize imports
   |
10 | from typing import Annotated
11 +
12 | import numpy_financial as npf  # type: ignore[import]
13 | from pydantic import BaseModel
14 +
15 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> numpy/np_pmt.py:22:1
   |
20 | sys.path.insert(0, "../")
21 | sys.path.insert(0, "python3/")
22 | from myutil import prt  # type: ignore[import]
   | ^^^^^^^^^^^^^^^^^^^^^^
23 |
24 | class Loan(BaseModel):
   |
help: Organize imports
   |
23 |
24 +
25 | class Loan(BaseModel):
   |

I001 [*] Import block is un-sorted or un-formatted
  --> numpy/pmt_json.py:9:1
   |
 7 |   '''
 8 |
 9 | / import sys
10 | | from decimal import Decimal, ROUND_HALF_UP
11 | | from typing import Annotated
12 | | import numpy_financial as npf  # type: ignore[import]
13 | | from pydantic import BaseModel
   | |______________________________^
14 |   try:
15 |       import typer
   |
help: Organize imports
   |
9  | import sys
   - from decimal import Decimal, ROUND_HALF_UP
10 + from decimal import ROUND_HALF_UP, Decimal
11 | from typing import Annotated
12 +
13 | import numpy_financial as npf  # type: ignore[import]
14 | from pydantic import BaseModel
15 +
16 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> numpy/pmt_json.py:23:1
   |
21 |   sys.path.insert(0, "../")
22 |   sys.path.insert(0, "python3/")
23 | / from myutil import prt  # type: ignore[import]
24 | | from myutil import read_jsonfile  # type: ignore[import]
   | |________________________________^
25 |
26 |   class Loan(BaseModel):
   |
help: Organize imports
   |
22 | sys.path.insert(0, "python3/")
   - from myutil import prt  # type: ignore[import]
   - from myutil import read_jsonfile  # type: ignore[import]
23 + from myutil import (
24 +     prt,  # type: ignore[import]
25 +     read_jsonfile,  # type: ignore[import]
26 + )
27 +
28 |
   |

FURB157 [*] Verbose expression in `Decimal` constructor
  --> numpy/pmt_json.py:39:66
   |
37 |     # numpy_financial.pmt returns negative cash outflow for repayment.
38 |     payment = abs(npf.pmt(val.rate/12, val.nper, val.pv))
39 |     payment_rounded = int(Decimal(str(payment)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
   |                                                                  ^^^
40 |     prt(f'{"monthly payment (rounded)":<28}: {payment_rounded:,d}')
   |
help: Replace with `1`
   |
38 |     payment = abs(npf.pmt(val.rate/12, val.nper, val.pv))
   -     payment_rounded = int(Decimal(str(payment)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
39 +     payment_rounded = int(Decimal(str(payment)).quantize(Decimal(1), rounding=ROUND_HALF_UP))
40 |     prt(f'{"monthly payment (rounded)":<28}: {payment_rounded:,d}')
   |

PERF402 Use `list` or `list.copy` to create a copy of a list
  --> numpy/sum_timeit.py:25:9
   |
23 |     res = []
24 |     for i in range(DEFAULT_SIZE):
25 |         res.append(i)
   |         ^^^^^^^^^^^^^
26 |     return res
   |

SIM103 Return the condition `n % 24 == 0` directly
  --> omc/a24bcde.py:41:9
   |
39 |           if n%10==0:
40 |               return False
41 | /         if n%24==0:
42 | |             return True
43 | |         return False
   | |____________________^
44 |
45 |       def action(self):
   |
help: Replace with `return n % 24 == 0`

SIM103 Return the condition directly
  --> omc/abc_ab.py:43:9
   |
41 |           m3 = self.b
42 |           tmp = m1 + m2 + m3
43 | /         if tmp % 111 == 0:
44 | |             #print(f'{m1} + {m2} + {m3}')
45 | |             #print(f'input: {self.input} tmp: {tmp}')
46 | |             return True
47 | |         return False
   | |____________________^
48 |
49 |       @staticmethod
   |
help: Inline condition

SIM103 Return the condition `p + q + r <= self.TOTAL` directly
  --> omc/bead106.py:21:9
   |
19 |           if p < 1 or q < 1 or r < 1:
20 |               return False
21 | /         if (p+q+r) <= self.TOTAL:
22 | |             return True
23 | |         return False
   | |____________________^
24 |
25 |       def find_answer(self):
   |
help: Replace with `return p + q + r <= self.TOTAL`

I001 [*] Import block is un-sorted or un-formatted
  --> omc/d240318-q16.py:10:1
   |
 8 | '''
 9 |
10 | from itertools import combinations
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
11 |
12 | class Solution:
   |
help: Organize imports
   |
11 |
12 +
13 | class Solution:
   |

SIM102 Use a single `if` statement instead of nested `if` statements
  --> omc/d240319-q25.py:27:9
   |
25 |       print(len(the_list))
26 |       for x in the_list:
27 | /         if 100000 < x:
28 | |             if x % 75 == 0:
   | |___________________________^
29 |                   print(x, x//75)
   |
help: Combine `if` statements using `and`

I001 [*] Import block is un-sorted or un-formatted
  --> omc/d240319-q27.py:10:1
   |
 8 |   '''
 9 |
10 | / from itertools import combinations
11 | | from sympy import Rational, gcd
   | |_______________________________^
   |
help: Organize imports
   |
10 | from itertools import combinations
11 +
12 | from sympy import Rational, gcd
   |

SIM103 Return the condition `p * p == q` directly
  --> omc/defdef.py:34:9
   |
32 |           p = 100*D+10*E+F
33 |           q = 10000*A+1000*B+100*C+10*D+A
34 | /         if p*p == q:
35 | |             return True
36 | |         return False
   | |____________________^
37 |
38 |       def action(self):
   |
help: Replace with `return p * p == q`

SIM102 Use a single `if` statement instead of nested `if` statements
  --> omc/digit21.py:12:5
   |
10 |       digits = list(str(v))
11 |       vals = [int(x) for x in digits]
12 | /     if sum(vals) == 21:
13 | |         if vals[1]-vals[2]==1:
   | |______________________________^
14 |               print(v)
15 |               return True
   |
help: Combine `if` statements using `and`

I001 [*] Import block is un-sorted or un-formatted
  --> omc/mcn.py:8:1
   |
 6 |   '''
 7 |
 8 | / import itertools as it
 9 | | from sympy import Rational
   | |__________________________^
10 |
11 |   def checkVals(vals):
   |
help: Organize imports
   |
8  | import itertools as it
9  +
10 | from sympy import Rational
11 |
12 +
13 | def checkVals(vals):
   |

SIM103 Return the condition `target - s == 0` directly
  --> omc/mcn.py:19:5
   |
17 |           s += t
18 |       #print(vals, s)
19 | /     if target - s == 0:
20 | |         return True
21 | |     return False
   | |________________^
   |
help: Replace with `return target - s == 0`

SIM102 Use a single `if` statement instead of nested `if` statements
  --> omc/mcn.py:40:9
   |
39 |       for n in it.product(pp, qq, rr, ss):
40 | /         if len(set(n)) == 4:
41 | |             if sum(list(n)) == 21:
   | |__________________________________^
42 |                   tries.append(list(n))
   |
help: Combine `if` statements using `and`

I001 [*] Import block is un-sorted or un-formatted
 --> omc/mutual.py:7:1
  |
5 | '''
6 |
7 | from math import gcd
  | ^^^^^^^^^^^^^^^^^^^^
8 |
9 | def main():
  |
help: Organize imports
   |
8  |
9  +
10 | def main():
   |

SIM103 Return the condition `not (a == b or b == c or c == a)` directly
  --> omc/numbercards.py:22:9
   |
20 |       def is_different(a, b, c):
21 |           ''' is different '''
22 | /         if a == b or b == c or c == a:
23 | |             return False
24 | |         return True
   | |___________________^
25 |
26 |       @staticmethod
   |
help: Replace with `return not (a == b or b == c or c == a)`

SIM103 Return the condition directly
  --> omc/numbercards.py:29:9
   |
27 |       def is_small2big(a, b, c):
28 |           ''' a, b, c small to big '''
29 | /         if c > b > a:   # c > b and b > a
30 | |             return True
31 | |         return False
   | |____________________^
32 |
33 |       def is_sum_match(self, a, b, c):
   |
help: Inline condition

SIM103 Return the condition `total == self.target` directly
  --> omc/numbercards.py:36:9
   |
34 |           ''' is sum(a,b,c) == target '''
35 |           total = a + b + c
36 | /         if total == self.target:
37 | |             return True
38 | |         return False
   | |____________________^
39 |
40 |       def test(self):
   |
help: Replace with `return total == self.target`

SIM102 Use a single `if` statement instead of nested `if` statements
  --> omc/numbercards.py:57:13
   |
55 |           for n in it.combinations(pp, 3):
56 |               (p, q, r) = n
57 | /             if self.is_different(p, q, r):
58 | |                 if self.is_small2big(p, q, r):
   | |______________________________________________^
59 |                       cnt += 1
60 |                       if self.is_sum_match(p, q, r):
   |
help: Combine `if` statements using `and`

SIM103 Return the condition `n % 1000 == t` directly
  --> omc/one23.py:10:5
   |
 8 |   def test_n(n: int, t: int) -> bool:
 9 |       ''' test n '''
10 | /     if n % 1000 == t:
11 | |         return True
12 | |     return False
   | |________________^
13 |
14 |   def main():
   |
help: Replace with `return n % 1000 == t`

SIM103 Return the condition `1000 <= n <= 9999` directly
  --> omc/onethird.py:14:5
   |
12 |   def is_four_digit(n):
13 |       ''' true if four digits number '''
14 | /     if 1000 <= n <= 9999:
15 | |         return True
16 | |     return False
   | |________________^
17 |
18 |   def is_five_digit(n):
   |
help: Replace with `return 1000 <= n <= 9999`

SIM103 Return the condition `10000 <= n <= 99999` directly
  --> omc/onethird.py:20:5
   |
18 |   def is_five_digit(n):
19 |       ''' true if five digits number '''
20 | /     if 10000 <= n <= 99999:
21 | |         return True
22 | |     return False
   | |________________^
23 |
24 |   def check_nine_digit(m, n):
   |
help: Replace with `return 10000 <= n <= 99999`

RUF012 Mutable default value for class attribute
  --> omc/p25-q14.py:12:14
   |
10 |       ''' try to find solution '''
11 |
12 |       primes = {
   |  ______________^
13 | |             13, 17, 19, 23, 29,
14 | |             31, 37, 41, 43, 47,
15 | |             53, 59, 61, 67, 71,
16 | |             73, 79, 83, 89, 97}
   | |_______________________________^
17 |
18 |       def __init__(self):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

PERF102 When using only the values of a dict use the `values()` method
  --> omc/p25-q14.py:79:20
   |
77 |                 lv3 += 1
78 |         print(f'{lv0=} {lv1=} {lv2=} {lv3=} {matched=}')
79 |         for _,v in ans.items():
   |                    ^^^^^^^^^
80 |             print(v)
   |
help: Replace `.items()` with `.values()`

I001 [*] Import block is un-sorted or un-formatted
  --> omc/p38-q22.py:11:1
   |
 9 | '''
10 |
11 | from sympy import Rational
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^
12 |
13 | def get_product(xn, xd):
   |
help: Organize imports
   |
12 |
13 +
14 | def get_product(xn, xd):
   |

SIM103 Return the condition `bool(sum(ds) == 21 and ds[1] - ds[2] == 1)` directly
  --> omc/p41-q15.py:37:9
   |
35 |           self.digits = list(str(n))
36 |           ds = [int(x) for x in self.digits]
37 | /         if sum(ds) == 21 and ds[1]-ds[2]==1:
38 | |             return True
39 | |         return False
   | |____________________^
   |
help: Replace with `return bool(sum(ds) == 21 and ds[1] - ds[2] == 1)`

SIM102 Use a single `if` statement instead of nested `if` statements
  --> omc/pen_p61.py:28:21
   |
26 |               for p in range(100-n, 1,-1):
27 |                   for e in range(100-n-p, 1,-1):
28 | /                     if n > p > e:
29 | |                         if n+p+e == 100:
   | |________________________________________^
30 |                               cnt += 1
31 |                               if self.check(n,p,e):
   |
help: Combine `if` statements using `and`

SIM102 Use a single `if` statement instead of nested `if` statements
  --> omc/qq15.py:31:13
   |
29 |           for v in it.combinations(the_list, 3):
30 |               t = sum(list(v))
31 | /             if 15<=t<=29:
32 | |                 if t not in check_set:
   | |______________________________________^
33 |                       list_sums.add(t)
34 |           if len(list_sums) == 10:
   |
help: Combine `if` statements using `and`

RUF100 [*] Unused `noqa` directive (non-enabled: `E741`)
  --> omc/sendmoremoney.py:32:9
   |
30 |         # pylint: disable=unbalanced-tuple-unpacking
31 |         assert len(c2) == 8
32 |         # ruff: noqa: E741
   |         ^^^^^^^^^^^^^^^^^^
33 |         [S,E,N,D,M,O,R,Y] = c2
34 |         if S==0 or M==0:
   |
help: Remove unused `noqa` directive
   |
31 |         assert len(c2) == 8
   -         # ruff: noqa: E741
32 |         [S,E,N,D,M,O,R,Y] = c2
   |

SIM103 Return the condition `send + more == money` directly
  --> omc/sendmoremoney.py:41:9
   |
39 |           money = M*10000+O*1000+N*100+E*10+Y
40 |           #print(send,more,money)
41 | /         if send + more == money:
42 | |             return True
43 | |         return False
   | |____________________^
44 |
45 |       def action(self):
   |
help: Replace with `return send + more == money`

RUF012 Mutable default value for class attribute
  --> omc/serial5-37-71.py:11:12
   |
 9 | class Solution:
10 |     ''' to solve '''
11 |     PART = [(0,1,2), (0,1,3), (0,1,4), (1,2,3), (1,2,4), (2,3,4)]
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

I001 [*] Import block is un-sorted or un-formatted
  --> omc/six_multiple/sixes.py:9:1
   |
 7 | '''
 8 |
 9 | from itertools import combinations
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
10 |
11 | class Solution:
   |
help: Organize imports
   |
10 |
11 +
12 | class Solution:
   |

RUF012 Mutable default value for class attribute
  --> omc/sixty_prime_sum.py:10:14
   |
 8 |       ''' class solution '''
 9 |       # primes <= 100 (size=25)
10 |       primes = [
   |  ______________^
11 | |         2,3,5,7,11,13,17,19,23,29,
12 | |         31,37,41,43,47,53,59,61,67,71,
13 | |         73,79,83,89,97]
   | |_______________________^
14 |
15 |       def __init__(self):
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

PERF402 Use `list` or `list.copy` to create a copy of a list
  --> omc/spend_money.py:62:17
   |
60 |             p = []
61 |             for y in z:
62 |                 p.append(y)
   |                 ^^^^^^^^^^^
63 |             self.cases.append(p)
   |

PIE808 [*] Unnecessary `start` argument in `range`
  --> omc/test7.py:54:20
   |
52 |     ''' main '''
53 |     correct_ans = None
54 |     for n in range(0,128):
   |                    ^
55 |         r = num2ans(n)
56 |         correct_ans = try_test(r)
   |
help: Remove `start` argument
   |
53 |     correct_ans = None
   -     for n in range(0,128):
54 +     for n in range(128):
55 |         r = num2ans(n)
   |

RUF012 Mutable default value for class attribute
  --> omc/threex3coins.py:15:13
   |
13 | class Solution:
14 |     ''' solution '''
15 |     coins = [3, 3, 3]
   |             ^^^^^^^^^
16 |     values = [50, 10, 5]
17 |     TOTAL = 100
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

RUF012 Mutable default value for class attribute
  --> omc/threex3coins.py:16:14
   |
14 |     ''' solution '''
15 |     coins = [3, 3, 3]
16 |     values = [50, 10, 5]
   |              ^^^^^^^^^^^
17 |     TOTAL = 100
   |
help: Consider initializing in `__init__` or annotating with `typing.ClassVar`

TRY004 Prefer `TypeError` exception for invalid type
  --> omc/utils.py:20:9
   |
18 |     ''' the shortest way to test if palindrome '''
19 |     if not isinstance(the_str, str):
20 |         raise ValueError
   |         ^^^^^^^^^^^^^^^^
21 |     return the_str==the_str[::-1]
   |

I001 [*] Import block is un-sorted or un-formatted
  --> omc/y24p25q3.py:8:1
   |
 6 |   '''
 7 |
 8 | / from math import sqrt
 9 | | from utils import digit_root, digit_sum
   | |_______________________________________^
10 |
11 |   def is_integer(val: float):
   |
help: Organize imports
   |
8  | from math import sqrt
9  +
10 | from utils import digit_root, digit_sum
11 |
12 +
13 | def is_integer(val: float):
   |

SIM102 Use a single `if` statement instead of nested `if` statements
  --> omc/y24p28q15.py:11:5
   |
 9 |       能被15和18整除，但不能被28整除
10 |       '''
11 | /     if n % 15 == 0 and n % 18 == 0:
12 | |         if n % 28 != 0:
   | |_______________________^
13 |               return True
14 |       return False
   |
help: Combine `if` statements using `and`

SIM103 Return the condition `bool('4' in ss and n % 4 != 0)` directly
  --> omc/y24p29q23.py:10:5
   |
 8 |       ''' input n '''
 9 |       ss = list(str(n))
10 | /     if '4' in ss and n%4!=0:
11 | |         return True
12 | |     return False
   | |________________^
   |
help: Replace with `return bool('4' in ss and n % 4 != 0)`

I001 [*] Import block is un-sorted or un-formatted
  --> omc/y24p32q30.py:9:1
   |
 7 | '''
 8 |
 9 | from itertools import combinations
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
10 |
11 | def swap(m, n):
   |
help: Organize imports
   |
10 |
11 +
12 | def swap(m, n):
   |

SIM102 Use a single `if` statement instead of nested `if` statements
  --> omc/y24p36q15.py:23:5
   |
21 |       ''' need r > 1 '''
22 |       [a, b, c] = the_list
23 | /     if a>1 and b>1 and c>1:
24 | |         if a==b==c:
   | |___________________^
25 |               return True
26 |       return False
   |
help: Combine `if` statements using `and`

I001 [*] Import block is un-sorted or un-formatted
  --> omc/y24p37q18.py:9:1
   |
 7 | '''
 8 |
 9 | from itertools import combinations
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
10 |
11 | class Solution:
   |
help: Organize imports
   |
10 |
11 +
12 | class Solution:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> pandas/boxplot_by_years.py:13:1
   |
11 |   '''
12 |
13 | / import os
14 | | import sys
15 | | import pandas as pd
16 | | import matplotlib.pyplot as plt
   | |_______________________________^
17 |   try:
18 |       from rich.console import Console
   |
help: Organize imports
   |
14 | import sys
   - import pandas as pd
15 +
16 | import matplotlib.pyplot as plt
17 +
18 + import pandas as pd
19 +
20 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> pandas/check_csv.py:7:1
   |
 5 |   '''
 6 |
 7 | / import argparse
 8 | | import os
 9 | | import sys
10 | | import re
   | |_________^
11 |
12 |   def logd(*args, **wargs) -> None:
   |
help: Organize imports
   |
8  | import os
9  + import re
10 | import sys
   - import re
11 |
12 +
13 | def logd(*args, **wargs) -> None:
   |

PLR2044 [*] Line with empty comment
 --> pandas/cmaps_data.py:1:1
  |
1 | #
  | ^
2 |
3 | '''
  |
help: Delete the empty comment
  |
  - #
1 |
  |

I001 [*] Import block is un-sorted or un-formatted
  --> pandas/commune_all.py:3:1
   |
 1 |   #!/usr/bin/env python3
 2 |
 3 | / import os
 4 | | import sys
 5 | | import numpy as np
 6 | | import pandas as pd
 7 | | import matplotlib.pyplot as plt
 8 | | import seaborn as sns
   | |_____________________^
 9 |   try:
10 |       import rich.console
   |
help: Organize imports
   |
4  | import sys
   - import numpy as np
   - import pandas as pd
5  +
6  | import matplotlib.pyplot as plt
7  | import seaborn as sns
8  +
9  + import numpy as np
10 + import pandas as pd
11 +
12 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> pandas/driving_data.py:33:1
   |
31 |       logi = print
32 |
33 | / from strutil import sec2mmss, str2sec, get_between_dates
34 | | from showutil import show_curios, show_extra_header, show_workingdays
35 | | from showutil import show_simplecsv, show_outputs, EXT_KEYS
36 | | from showutil import peek_target, output2csv
   | |____________________________________________^
37 |
38 |   try:
   |
help: Organize imports
   |
32 |
   - from strutil import sec2mmss, str2sec, get_between_dates
   - from showutil import show_curios, show_extra_header, show_workingdays
   - from showutil import show_simplecsv, show_outputs, EXT_KEYS
   - from showutil import peek_target, output2csv
33 + from showutil import (
34 +     EXT_KEYS,
35 +     output2csv,
36 +     peek_target,
37 +     show_curios,
38 +     show_extra_header,
39 +     show_outputs,
40 +     show_simplecsv,
41 +     show_workingdays,
42 + )
43 + from strutil import get_between_dates, sec2mmss, str2sec
44 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> pandas/driving_data.py:41:5
   |
39 |       sys.path.insert(0, "..")
40 |       sys.path.insert(0, "../../")
41 | /     from myutil import query_url_for_data, read_jsonfile, isfile, die # type: ignore[import]
42 | |     from myutil import MyDebug, MyVerbose, DefaultConfig # type: ignore[import]
   | |________________________________________________________^
43 |   except ImportError:
44 |       print('[ERROR] cannot import myutil...')
   |
help: Organize imports
   |
40 |     sys.path.insert(0, "../../")
   -     from myutil import query_url_for_data, read_jsonfile, isfile, die # type: ignore[import]
   -     from myutil import MyDebug, MyVerbose, DefaultConfig # type: ignore[import]
41 +     from myutil import (  # type: ignore[import]  # type: ignore[import]
42 +         DefaultConfig,
43 +         MyDebug,
44 +         MyVerbose,
45 +         die,
46 +         isfile,
47 +         query_url_for_data,
48 +         read_jsonfile,
49 +     )
50 | except ImportError:
   |

DTZ011 `datetime.date.today()` used
   --> pandas/driving_data.py:301:33
    |
299 |         self._tag = 'fill_outputs'
300 |         self._log('enters...')
301 |         self.outputs['today'] = date.today()
    |                                 ^^^^^^^^^^^^
302 |         ans = peek_target(des, "count")
303 |         count = str(int(floor(ans)))
    |
help: Use `datetime.datetime.now(tz=...).date()` instead

RUF046 Value being cast to `int` is already an integer
   --> pandas/driving_data.py:303:21
    |
301 |         self.outputs['today'] = date.today()
302 |         ans = peek_target(des, "count")
303 |         count = str(int(floor(ans)))
    |                     ^^^^^^^^^^^^^^^
304 |         logd(f'count: {count}')
305 |         self.outputs['count'] = count
    |
help: Remove unnecessary `int` call

I001 [*] Import block is un-sorted or un-formatted
 --> pandas/showutil.py:6:5
  |
5 |   try:
6 | /     from rich.table import Table
7 | |     from rich.console import Console
  | |____________________________________^
8 |       USE_TABLE = True
9 |   except ImportError:
  |
help: Organize imports
  |
5 | try:
6 +     from rich.console import Console
7 |     from rich.table import Table
  -     from rich.console import Console
8 |     USE_TABLE = True
  |

I001 [*] Import block is un-sorted or un-formatted
  --> pandas/showutil.py:12:1
   |
10 |       print('[FAIL] rich module not found, install with pip3 install rich')
11 |       USE_TABLE = False
12 | / import numpy as np
13 | | from working_days import LoadWorkingDays
14 | | from strutil import str2sec
   | |___________________________^
15 |
16 |   BASIC_KEYS = ['max', '75%', 'mean', '50%', '25%', 'min', 'std']
   |
help: Organize imports
   |
11 |     USE_TABLE = False
   - import numpy as np
   - from working_days import LoadWorkingDays
12 | from strutil import str2sec
13 + from working_days import LoadWorkingDays
14 +
15 + import numpy as np
16 |
   |

FURB122 [*] Use of `f.write` in a for loop
   --> pandas/showutil.py:133:9
    |
131 |       with open(csvfn, 'wt', encoding='utf-8') as f:
132 |           f.write('date,seconds\n')
133 | /         for idx, row in the_df.iterrows():
134 | |             f.write(f'{row["date"]},{row["seconds"]}\n')
    | |________________________________________________________^
135 |       print(f'[INFO] saved to {csvfn}')
    |
help: Replace with `f.writelines`
    |
132 |         f.write('date,seconds\n')
    -         for idx, row in the_df.iterrows():
    -             f.write(f'{row["date"]},{row["seconds"]}\n')
133 +         f.writelines(f'{row["date"]},{row["seconds"]}\n' for idx, row in the_df.iterrows())
134 |     print(f'[INFO] saved to {csvfn}')
    |

I001 [*] Import block is un-sorted or un-formatted
 --> pandas/strutil.py:5:1
  |
3 |   ''' some useful string snippets '''
4 |
5 | / from datetime import date
6 | | import re
  | |_________^
  |
help: Organize imports
  |
4 |
5 + import re
6 | from datetime import date
  - import re
7 |
  |

TRY004 Prefer `TypeError` exception for invalid type
  --> pandas/strutil.py:18:9
   |
16 |     if not isinstance(timestr, str):
17 |         print('str2sec: not a string?', timestr)
18 |         raise ValueError
   |         ^^^^^^^^^^^^^^^^
19 |     # mm:ss.ss (mm part could be 3 digits)
20 |     m = re.match(r'\d+:\d\d(\.\d\d)?', timestr)
   |

I001 [*] Import block is un-sorted or un-formatted
  --> pandas/working_days.py:10:1
   |
 8 | '''
 9 |
10 | import sys
   | ^^^^^^^^^^
11 | try:
12 |     from rich.console import Console
   |
help: Organize imports
   |
10 | import sys
11 +
12 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> pandas/working_days.py:20:5
   |
18 | try:
19 |     sys.path.insert(0, "..")
20 |     from myutil import read_jsonfile, DefaultConfig # type: ignore[import]
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
21 | except ImportError:
22 |     logd('failed to import myutil')
   |
help: Organize imports
   |
19 |     sys.path.insert(0, "..")
   -     from myutil import read_jsonfile, DefaultConfig # type: ignore[import]
20 +     from myutil import DefaultConfig, read_jsonfile  # type: ignore[import]
21 | except ImportError:
   |

I001 [*] Import block is un-sorted or un-formatted
 --> percent_dec.py:7:1
  |
5 |   '''
6 |
7 | / import argparse
8 | | from myutil import read_from_stdin
9 | | from percent_encdec import percent_dec
  | |______________________________________^
  |
help: Organize imports
  |
7 | import argparse
8 +
9 | from myutil import read_from_stdin
  |

I001 [*] Import block is un-sorted or un-formatted
 --> percent_enc.py:7:1
  |
5 |   '''
6 |
7 | / import argparse
8 | | from myutil import read_from_stdin
9 | | from percent_encdec import percent_enc, show_unicode_escape
  | |___________________________________________________________^
  |
help: Organize imports
  |
7 | import argparse
8 +
9 | from myutil import read_from_stdin
  |

I001 [*] Import block is un-sorted or un-formatted
  --> periodic/brief.py:7:1
   |
 5 |   '''
 6 |
 7 | / import json
 8 | | import os
 9 | | import sys
   | |__________^
10 |   try:
11 |       from rich import Console
   |
help: Organize imports
   |
9  | import sys
10 +
11 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> periodic/brief.py:18:5
   |
16 | try:
17 |     sys.path.insert(0, "..")
18 |     from myutil import read_jsonfile, isfile
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
19 | except ImportError:
20 |     print("Error: myutil module not found")
   |
help: Organize imports
   |
17 |     sys.path.insert(0, "..")
   -     from myutil import read_jsonfile, isfile
18 +     from myutil import isfile, read_jsonfile
19 | except ImportError:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> periodic/query-elements.py:8:1
   |
 6 | '''
 7 |
 8 | from brief import ShowElement
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 9 |
10 | def main():
   |
help: Organize imports
   |
9  |
10 +
11 | def main():
   |

I001 [*] Import block is un-sorted or un-formatted
  --> play_miranda.py:7:1
   |
 5 |   '''
 6 |
 7 | / import os
 8 | | import random
 9 | | import re
10 | | import sys
11 | | import time
12 | | from typing import List
13 | |
14 | | from myutil import get_home, read_jsonfile, isfile
   | |__________________________________________________^
   |
help: Organize imports
   |
13 |
   - from myutil import get_home, read_jsonfile, isfile
14 + from myutil import get_home, isfile, read_jsonfile
15 |
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> play_miranda.py:12:1
   |
10 | import sys
11 | import time
12 | from typing import List
   | ^^^^^^^^^^^^^^^^^^^^^^^
13 |
14 | from myutil import get_home, read_jsonfile, isfile
   |

UP006 [*] Use `list` instead of `List` for type annotation
  --> play_miranda.py:47:53
   |
46 |     @staticmethod
47 |     def get_immediate_subdirectories(a_dir: str) -> List:
   |                                                     ^^^^
48 |         '''
49 |         refer from:
   |
help: Replace with `list`
   |
46 |     @staticmethod
   -     def get_immediate_subdirectories(a_dir: str) -> List:
47 +     def get_immediate_subdirectories(a_dir: str) -> list:
48 |         '''
   |

I001 [*] Import block is un-sorted or un-formatted
  --> qr/segno_demo.py:8:1
   |
 6 |   '''
 7 |
 8 | / import os
 9 | | import segno
   | |____________^
10 |
11 |   def main():
   |
help: Organize imports
   |
8  | import os
9  +
10 | import segno
11 |
12 +
13 | def main():
   |

I001 [*] Import block is un-sorted or un-formatted
  --> random/five_char_verbs.py:9:1
   |
 7 |   '''
 8 |
 9 | / import os
10 | | import sys
11 | | import re
   | |_________^
12 |
13 |   class Solution:
   |
help: Organize imports
   |
9  | import os
10 + import re
11 | import sys
   - import re
12 |
13 +
14 | class Solution:
   |

I001 [*] Import block is un-sorted or un-formatted
 --> random/ran.py:5:1
  |
3 | ''' just pick one name from name list randomly '''
4 |
5 | import random
  | ^^^^^^^^^^^^^
6 | try:
7 |     from rich import print as rprint
  |
help: Organize imports
  |
5 | import random
6 +
7 | try:
  |

I001 [*] Import block is un-sorted or un-formatted
  --> random/random_string.py:10:1
   |
 8 |   '''
 9 |
10 | / import os
11 | | import re
12 | | import sys
13 | | from random import randint
   | |__________________________^
14 |   try:
15 |       from rich.console import Console
   |
help: Organize imports
   |
13 | from random import randint
14 +
15 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> random/verbs_random.py:7:1
   |
 5 |   '''
 6 |
 7 | / import os
 8 | | import re
 9 | | import json
10 | | import random
   | |_____________^
11 |   try:
12 |       from rich import print as pprint
   |
help: Organize imports
   |
6  |
   - import os
   - import re
7  | import json
8  + import os
9  | import random
10 + import re
11 +
12 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> random/verbs_random.py:12:5
   |
10 |   import random
11 |   try:
12 | /     from rich import print as pprint
13 | |     from rich.console import Console
   | |____________________________________^
14 |       prt = pprint
15 |       console = Console()
   |
help: Organize imports
   |
11 | try:
   -     from rich import print as pprint
12 |     from rich.console import Console
13 +
14 +     from rich import print as pprint
15 |     prt = pprint
   |

BLE001 Do not catch blind exception: `Exception`
  --> random/verbs_random.py:44:20
   |
42 |                     if " " not in text:
43 |                         verbs.append(text)
44 |             except Exception as e:
   |                    ^^^^^^^^^
45 |                 logd(f"Error reading {fn}: {e}")
46 |         return verbs
   |

BLE001 Do not catch blind exception: `Exception`
  --> random/verbs_random.py:64:20
   |
62 |                         verbs.append(m.group(0))
63 |                         cnt += 1
64 |             except Exception as e:
   |                    ^^^^^^^^^
65 |                 logd(f"Error reading {self.fn}: {e}")
66 |         return verbs
   |

I001 [*] Import block is un-sorted or un-formatted
  --> rdf/rdf_parse.py:25:1
   |
24 | sys.path.insert(0, "..")
25 | from myutil import isfile, read_textfile, sha256sum, MyDebug, MyVerbose
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
26 |
27 | class Solution(MyDebug, MyVerbose):
   |
help: Organize imports
   |
24 | sys.path.insert(0, "..")
   - from myutil import isfile, read_textfile, sha256sum, MyDebug, MyVerbose
25 + from myutil import MyDebug, MyVerbose, isfile, read_textfile, sha256sum
26 +
27 |
   |

SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  --> read_ten_lines.py:16:13
   |
14 |         cnt = 0
15 |         for ln in fin:
16 |             cnt += 1
   |             ^^^^^^^^
17 |             if cnt > 10:
18 |                 break
   |

I001 [*] Import block is un-sorted or un-formatted
  --> reth.py:11:1
   |
 9 |   __VERSION__ = '2024.05.29'
10 |
11 | / import os
12 | | import re
13 | | import sys
14 | | from glob import glob
15 | | from typing import List
   | |_______________________^
16 |
17 |   def die(*args, **kwargs) -> None:
   |
help: Organize imports
   |
16 |
17 +
18 | def die(*args, **kwargs) -> None:
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> reth.py:15:1
   |
13 | import sys
14 | from glob import glob
15 | from typing import List
   | ^^^^^^^^^^^^^^^^^^^^^^^
16 |
17 | def die(*args, **kwargs) -> None:
   |

UP006 [*] Use `list` instead of `List` for type annotation
  --> reth.py:38:28
   |
36 |             print(*args, **wargs, file=sys.stderr)
37 |
38 |     def is_digits(self) -> List:
   |                            ^^^^
39 |         ''' is digits '''
40 |         self.logd('is_digits: try normal digit...')
   |
help: Replace with `list`
   |
37 |
   -     def is_digits(self) -> List:
38 +     def is_digits(self) -> list:
39 |         ''' is digits '''
   |

UP006 [*] Use `list` instead of `List` for type annotation
  --> reth.py:63:32
   |
61 |         return pairs
62 |
63 |     def is_han_digits(self) -> List:
   |                                ^^^^
64 |         ''' han digits '''
65 |         print('try han digits...')
   |
help: Replace with `list`
   |
62 |
   -     def is_han_digits(self) -> List:
63 +     def is_han_digits(self) -> list:
64 |         ''' han digits '''
   |

SIM115 Use a context manager for opening files
  --> reurl.py:51:19
   |
49 |             out = sys.stderr
50 |         else:
51 |             out = open(os.devnull, 'wb')
   |                   ^^^^
52 |
53 |         content_type = r.headers['Content-Type']
   |

I001 [*] Import block is un-sorted or un-formatted
  --> rich/sp.py:8:1
   |
 6 |   '''
 7 |
 8 | / from random import randint
 9 | | from time import sleep
10 | | from rich.console import Console
11 | | from rich.spinner import SPINNERS
   | |_________________________________^
12 |   #from rich.text import Text
   |
help: Organize imports
   |
9  | from time import sleep
10 +
11 | from rich.console import Console
12 | from rich.spinner import SPINNERS
13 +
14 | #from rich.text import Text
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> rpc/concat.py:12:1
   |
10 | import sys
11 |
12 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
13 | sys.path.insert(0, '../')
14 | sys.path.insert(0, '../../')
   |
help: Remove unused `noqa` directive
   |
11 |
   - # ruff: noqa: E402
12 | sys.path.insert(0, '../')
   |

I001 [*] Import block is un-sorted or un-formatted
  --> rpc/concat.py:16:1
   |
14 | sys.path.insert(0, '../../')
15 | sys.path.insert(0, 'python3/')
16 | from myutil import read_jsonfile
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
17 |
18 | def test(fn):
   |
help: Organize imports
   |
17 |
18 +
19 | def test(fn):
   |

SIM118 Use `key in dict` instead of `key in dict.keys()`
  --> rpc/fetch_currency_rate.py:12:9
   |
10 | def grep_keyword(data, keyword):
11 |     ''' grep_keyword '''
12 |     for kk in data.keys():
   |         ^^^^^^^^^^^^^^^^^
13 |         try:
14 |             kk.index(keyword)
   |
help: Remove `.keys()`

I001 [*] Import block is un-sorted or un-formatted
  --> rpc/firstai.py:8:1
   |
 6 |   '''
 7 |
 8 | / import sys
 9 | | from datetime import datetime
10 | | import google.generativeai as genai
11 | | from rich.console import Console
12 | | from rich import print as prt
   | |_____________________________^
13 |   sys.path.insert(0, "..")
14 |   sys.path.insert(0, "../..")
   |
help: Organize imports
   |
9  | from datetime import datetime
10 +
11 | import google.generativeai as genai
12 | from rich.console import Console
13 +
14 | from rich import print as prt
15 +
16 | sys.path.insert(0, "..")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> rpc/firstai.py:16:1
   |
14 | sys.path.insert(0, "../..")
15 | sys.path.insert(0, "python3")
16 | from myutil import read_jsonfile, DefaultConfig
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
17 |
18 | class Solution:
   |
help: Organize imports
   |
15 | sys.path.insert(0, "python3")
   - from myutil import read_jsonfile, DefaultConfig
16 + from myutil import DefaultConfig, read_jsonfile
17 +
18 |
   |

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> rpc/firstai.py:52:19
   |
50 |         logd("incoming msg...")
51 |         with open(self.log, "at", encoding='utf-8') as flog:
52 |             print(datetime.now(), file=flog)
   |                   ^^^^^^^^^^^^^^
53 |             print(msg, file=flog)
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

I001 [*] Import block is un-sorted or un-formatted
  --> rpc/getapikey.py:12:1
   |
11 | sys.path.insert(0, "..")
12 | from myutil import read_jsonfile, DefaultConfig
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
help: Organize imports
   |
11 | sys.path.insert(0, "..")
   - from myutil import read_jsonfile, DefaultConfig
12 + from myutil import DefaultConfig, read_jsonfile
13 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> rpc/query_water.py:12:1
   |
12 | / import requests
13 | | from bs4 import BeautifulSoup
   | |_____________________________^
14 |
15 |   def save2file(the_str, ofn):
   |
help: Organize imports
   |
14 |
15 +
16 | def save2file(the_str, ofn):
   |

I001 [*] Import block is un-sorted or un-formatted
  --> rpc/req_guassian.py:15:1
   |
14 | sys.path.insert(0, "..")
15 | from myutil import read_jsonfile, isfile
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
16 |
17 | try:
   |
help: Organize imports
   |
14 | sys.path.insert(0, "..")
   - from myutil import read_jsonfile, isfile
15 + from myutil import isfile, read_jsonfile
16 |
   |

SIM102 Use a single `if` statement instead of nested `if` statements
  --> rpc/send-attached.py:77:9
   |
75 |       def _check(self):
76 |           ''' check '''
77 | /         if self.bodyfile:
78 | |             if not isfile(self.bodyfile):
   | |_________________________________________^
79 |                   print('[ERROR] bodyfile not found:', self.bodyfile)
80 |                   sys.exit(1)
   |
help: Combine `if` statements using `and`

I001 [*] Import block is un-sorted or un-formatted
  --> rpc/testqr.py:8:1
   |
 7 |   # pylint: disable=import-error
 8 | / import argparse
 9 | | import os
10 | | from collections import OrderedDict
11 | | from urllib.parse import urlencode
12 | |
13 | | import requests
14 | | #import numpy as np
15 | | from httpbin import show_results
16 | | from PIL import Image
   | |_____________________^
17 |
18 |   # pylint: disable=using-constant-test
   |
help: Organize imports
   |
13 | import requests
14 +
15 | #import numpy as np
   |

UP024 [*] Replace aliased errors with `OSError`
  --> rpc/validate_gaussian.py:36:16
   |
34 |                     val = float(ln.strip())
35 |                     arr.append(val)
36 |         except IOError:
   |                ^^^^^^^
37 |             print(f'[ERROR] IOError while open: {fn}')
38 |             print('[INFO] may execute **req_guassian.py** to generate data.txt')
   |
help: Replace `IOError` with builtin `OSError`
   |
35 |                     arr.append(val)
   -         except IOError:
36 +         except OSError:
37 |             print(f'[ERROR] IOError while open: {fn}')
   |

UP024 [*] Replace aliased errors with `OSError`
  --> rpc/validate_gaussian.py:49:16
   |
47 |                 for val in arr:
48 |                     print(f'{val}', file=ofile)
49 |         except IOError as e:
   |                ^^^^^^^
50 |             print(f'Except happens: {e}')
   |
help: Replace `IOError` with builtin `OSError`
   |
48 |                     print(f'{val}', file=ofile)
   -         except IOError as e:
49 +         except OSError as e:
50 |             print(f'Except happens: {e}')
   |

I001 [*] Import block is un-sorted or un-formatted
  --> run_gcd.py:13:1
   |
11 |   '''
12 |
13 | / import argparse
14 | |
15 | | # official math.gcd
16 | | from math import gcd as math_gcd
17 | | from random import randint
18 | | from timeit import timeit
   | |_________________________^
19 |   try:
20 |       from numpy import gcd as numpy_gcd
   |
help: Organize imports
   |
18 | from timeit import timeit
19 +
20 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
 --> run_test3.py:5:1
  |
3 | ''' run test3 from run_gcd '''
4 |
5 | from run_gcd import test3
  | ^^^^^^^^^^^^^^^^^^^^^^^^^
6 |
7 | def main():
  |
help: Organize imports
  |
6 |
7 +
8 | def main():
  |

I001 [*] Import block is un-sorted or un-formatted
  --> show_arrows.py:7:1
   |
 5 |   '''
 6 |
 7 | / from typing import Annotated
 8 | | import typer
 9 | | from rich.columns import Columns
10 | | from rich.panel import Panel
11 | | from rich.console import Console
   | |________________________________^
12 |
13 |   def no_rich(is_csv: bool, reverse: bool = False):
   |
help: Organize imports
   |
7  | from typing import Annotated
8  +
9  | import typer
10 | from rich.columns import Columns
11 + from rich.console import Console
12 | from rich.panel import Panel
   - from rich.console import Console
13 |
14 +
15 | def no_rich(is_csv: bool, reverse: bool = False):
   |

I001 [*] Import block is un-sorted or un-formatted
  --> spath.py:16:1
   |
14 |   # alias path='echo $PATH | sed "s/:/\n/g"'
15 |
16 | / import argparse
17 | | from dataclasses import dataclass
18 | | import os
19 | | from sysconfig import get_platform
20 | | from typing import Any
   | |______________________^
21 |
22 |   # while import stage, do not use logd
   |
help: Organize imports
   |
16 | import argparse
17 + import os
18 | from dataclasses import dataclass
   - import os
19 | from sysconfig import get_platform
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> spath.py:66:5
   |
64 | def do_nothing(*_args, **_wargs) -> None:
65 |     ''' do nothing '''
66 |     return None
   |     ^^^^^^^^^^^
67 |
68 | class PathLister:
   |
help: Remove explicit `return None`
   |
65 |     ''' do nothing '''
   -     return None
66 +     return
67 |
   |

I001 [*] Import block is un-sorted or un-formatted
 --> sql/getloc.py:7:1
  |
5 | '''
6 |
7 | import sqlite3
  | ^^^^^^^^^^^^^^
8 | try:
9 |     import hexdump
  |
help: Organize imports
  |
7 | import sqlite3
8 +
9 | try:
  |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> sql/getloc.py:18:5
   |
16 | def dump_nothing(_buffer) -> None:
17 |     ''' dump nothing '''
18 |     return None
   |     ^^^^^^^^^^^
19 |
20 | class Solution:
   |
help: Remove explicit `return None`
   |
17 |     ''' dump nothing '''
   -     return None
18 +     return
19 |
   |

I001 [*] Import block is un-sorted or un-formatted
  --> syspath.py:15:1
   |
15 | import sys
   | ^^^^^^^^^^
16 |
17 | def main():
   |
help: Organize imports
   |
16 |
17 +
18 | def main():
   |

SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  --> ten_digits.py:77:13
   |
75 |         arr = []
76 |         for ii in it.combinations(self.start, 5):
77 |             cnt += 1
   |             ^^^^^^^^
78 |             s = ''.join(ii)
79 |             arr.append(int(s))
   |

UP035 `typing.List` is deprecated, use `list` instead
 --> the_gcd.py:7:1
  |
6 | import sys
7 | from typing import List
  | ^^^^^^^^^^^^^^^^^^^^^^^
8 |
9 | from myutil import read_from_stdin
  |

UP006 [*] Use `list` instead of `List` for type annotation
  --> the_gcd.py:21:16
   |
19 |     return gcd(n, m % n)
20 |
21 | def main(argv: List[str]) -> None:
   |                ^^^^
22 |     ''' main function '''
23 |     vals = []
   |
help: Replace with `list`
   |
20 |
   - def main(argv: List[str]) -> None:
21 + def main(argv: list[str]) -> None:
22 |     ''' main function '''
   |

SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  --> triangle.py:81:13
   |
79 |                 print()
80 |             print(t, end=' ')
81 |             cnt += 1
   |             ^^^^^^^^
82 |         print()
   |

SIM102 Use a single `if` statement instead of nested `if` statements
   --> triangle.py:122:13
    |
120 |                   #print(f'{m} <= {n}')
121 |                   continue
122 | /             if self.gcd(m, n) == 1:
123 | |                 #print(f'gcd({m}, {n}) == 1')
124 | |                 if (m+n)%2 == 1:
    | |________________________________^
125 |                       self.mnlist.append((m, n))
    |
help: Combine `if` statements using `and`

I001 [*] Import block is un-sorted or un-formatted
  --> typer_example.py:10:1
   |
 8 |   '''
 9 |
10 | / import sys
11 | | from typing import List, Optional, Annotated
   | |____________________________________________^
12 |
13 |   try:
   |
help: Organize imports
   |
10 | import sys
   - from typing import List, Optional, Annotated
11 + from typing import Annotated, List, Optional
12 |
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> typer_example.py:11:1
   |
10 | import sys
11 | from typing import List, Optional, Annotated
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
12 |
13 | try:
   |

I001 [*] Import block is un-sorted or un-formatted
  --> typer_example.py:16:5
   |
14 |       import typer
15 |       print("version of typer:", typer.__version__)
16 | /     from rich import print as rprint
17 | |     from loguru import logger
   | |_____________________________^
18 |   except ImportError as e:
19 |       print('[FAIL] failed to load module:', e)
   |
help: Organize imports
   |
15 |     print("version of typer:", typer.__version__)
   -     from rich import print as rprint
16 |     from loguru import logger
17 +
18 +     from rich import print as rprint
19 | except ImportError as e:
   |

RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  --> typer_example.py:24:5
   |
22 | def do_nothing(*_args, **_wargs) -> None:
23 |     ''' do nothing '''
24 |     return None
   |     ^^^^^^^^^^^
25 |
26 | class Main:
   |
help: Remove explicit `return None`
   |
23 |     ''' do nothing '''
   -     return None
24 +     return
25 |
   |

UP006 [*] Use `list` instead of `List` for type annotation
  --> typer_example.py:60:35
   |
58 |             self.show_list(ll, i)
59 |
60 |     def show_list(self, the_list: List, v: int) -> None:
   |                                   ^^^^
61 |         ''' show the list '''
62 |         print('[', end='')
   |
help: Replace with `list`
   |
59 |
   -     def show_list(self, the_list: List, v: int) -> None:
60 +     def show_list(self, the_list: list, v: int) -> None:
61 |         ''' show the list '''
   |

UP045 [*] Use `X | None` for type annotations
  --> typer_example.py:81:38
   |
79 |     # typer.Argument()] = None,
80 |     #
81 |     def main(self, values: Annotated[Optional[List[int]],
   |                                      ^^^^^^^^^^^^^^^^^^^
82 |                                      typer.Argument(help="specify values")] = None,
83 |             after: Annotated[int,
   |
help: Convert to `X | None`
   |
80 |     #
   -     def main(self, values: Annotated[Optional[List[int]],
81 +     def main(self, values: Annotated[List[int] | None,
82 |                                      typer.Argument(help="specify values")] = None,
   |

UP006 [*] Use `list` instead of `List` for type annotation
  --> typer_example.py:81:47
   |
79 |     # typer.Argument()] = None,
80 |     #
81 |     def main(self, values: Annotated[Optional[List[int]],
   |                                               ^^^^
82 |                                      typer.Argument(help="specify values")] = None,
83 |             after: Annotated[int,
   |
help: Replace with `list`
   |
80 |     #
   -     def main(self, values: Annotated[Optional[List[int]],
81 +     def main(self, values: Annotated[Optional[list[int]],
82 |                                      typer.Argument(help="specify values")] = None,
   |

I001 [*] Import block is un-sorted or un-formatted
 --> unicode/apple_logo.py:8:1
  |
8 | / from showutf8 import show_utf8char
9 | | from myutil import get_python_versions
  | |______________________________________^
  |
help: Organize imports
   |
8  | from showutf8 import show_utf8char
9  +
10 | from myutil import get_python_versions
   |

I001 [*] Import block is un-sorted or un-formatted
  --> unicode/show_emojis.py:10:1
   |
 8 | '''
 9 |
10 | import sys
   | ^^^^^^^^^^
11 | sys.path.insert(0, '../emoji/')
   |
help: Organize imports
   |
10 | import sys
11 +
12 | sys.path.insert(0, '../emoji/')
   |

SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  --> unicode/show_emojis.py:54:13
   |
52 |         for k, v in self.emojis.items():
53 |             print(f'{k}: {v}')
54 |             cnt += 1
   |             ^^^^^^^^
55 |             if cnt > 10:
56 |                 break
   |

UP025 [*] Remove unicode literals from strings
  --> unicode/showutf8.py:26:9
   |
24 |     print()
25 |
26 |     S = u' '.join(u"\u037E").encode('utf-8').strip()
   |         ^^^^
27 |     print(type(S))
28 |     print(f"greek question mark: {S!r}")
   |
help: Remove unicode prefix
   |
25 |
   -     S = u' '.join(u"\u037E").encode('utf-8').strip()
26 +     S = ' '.join(u"\u037E").encode('utf-8').strip()
27 |     print(type(S))
   |

UP025 [*] Remove unicode literals from strings
  --> unicode/showutf8.py:26:19
   |
24 |     print()
25 |
26 |     S = u' '.join(u"\u037E").encode('utf-8').strip()
   |                   ^^^^^^^^^
27 |     print(type(S))
28 |     print(f"greek question mark: {S!r}")
   |
help: Remove unicode prefix
   |
25 |
   -     S = u' '.join(u"\u037E").encode('utf-8').strip()
26 +     S = u' '.join("\u037E").encode('utf-8').strip()
27 |     print(type(S))
   |

I001 [*] Import block is un-sorted or un-formatted
  --> unihan/suzhou_numerals.py:11:1
   |
 9 |   '''
10 |
11 | / import random
12 | | import sys
   | |__________^
13 |   try:
14 |       from rich.console import Console
   |
help: Organize imports
   |
12 | import sys
13 +
14 | try:
   |

TRY004 Prefer `TypeError` exception for invalid type
  --> unihan/suzhou_numerals.py:45:9
   |
43 |     ''' get integer value from suzhou numerals '''
44 |     if not isinstance(s, str):
45 |         raise ValueError('s is not str')
   |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
46 |     if s in suzhou_numerals:
47 |         return chr(int(suzhou_numerals[s], 16))
   |

I001 [*] Import block is un-sorted or un-formatted
  --> util/collect_import.py:5:1
   |
 3 |   ''' collect import '''
 4 |
 5 | / import os
 6 | | import re
 7 | | import sys
 8 | | from loguru import logger
   | |_________________________^
 9 |
10 |   # ruff: noqa: E402
   |
help: Organize imports
  |
7 | import sys
8 +
9 | from loguru import logger
  |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> util/collect_import.py:10:1
   |
 8 | from loguru import logger
 9 |
10 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
11 | sys.path.insert(0, "./")
12 | sys.path.insert(0, "../")
   |
help: Remove unused `noqa` directive
   |
9  |
   - # ruff: noqa: E402
10 | sys.path.insert(0, "./")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> util/mkrep.py:7:1
   |
 5 |   '''
 6 |
 7 | / import re
 8 | | import operator
 9 | | import os
10 | | import sys
11 | | from rich import print as rprint
12 | | from loguru import logger
   | |_________________________^
13 |
14 |   # ruff: noqa: E402
   |
help: Organize imports
   |
6  |
   - import re
7  | import operator
8  | import os
9  + import re
10 | import sys
   - from rich import print as rprint
11 +
12 | from loguru import logger
13 |
14 + from rich import print as rprint
15 +
16 | # ruff: noqa: E402
   |

RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  --> util/mkrep.py:14:1
   |
12 | from loguru import logger
13 |
14 | # ruff: noqa: E402
   | ^^^^^^^^^^^^^^^^^^
15 | sys.path.insert(0, "./")
16 | sys.path.insert(0, "../")
   |
help: Remove unused `noqa` directive
   |
13 |
   - # ruff: noqa: E402
14 | sys.path.insert(0, "./")
   |

I001 [*] Import block is un-sorted or un-formatted
  --> uuid_demo.py:8:1
   |
 6 | '''
 7 |
 8 | import uuid
   | ^^^^^^^^^^^
 9 |
10 | def sep() -> None:
   |
help: Organize imports
   |
9  |
10 +
11 | def sep() -> None:
   |

C408 Unnecessary `tuple()` call (rewrite as a literal)
  --> xlsxwriter/go.py:35:24
   |
33 |         mydict = {}
34 |         for i in range(cfrom, cto):
35 |             myvalues = tuple()
   |                        ^^^^^^^
36 |             acol = Solution.getcn('A', i)
37 |             dcol = Solution.getcn(col_initial, i)
   |
help: Rewrite as a literal

I001 [*] Import block is un-sorted or un-formatted
  --> yaml/ly.py:5:1
   |
 3 |   ''' loading yaml '''
 4 |
 5 | / import json
 6 | | import os
 7 | | import sys
 8 | | from typing import Union
   | |________________________^
 9 |   sys.path.insert(0, "..")
10 |   sys.path.insert(0, "python3/")
   |
help: Organize imports
   |
8  | from typing import Union
9  +
10 | sys.path.insert(0, "..")
   |

UP007 [*] Use `X | Y` for type annotations
  --> yaml/ly.py:20:30
   |
18 |     sys.exit(1)
19 |
20 | def try_location(fn: str) -> Union[str, None]:
   |                              ^^^^^^^^^^^^^^^^
21 |     ''' try to find file from current location and then
22 |         same location of current script
   |
help: Convert to `X | Y`
   |
19 |
   - def try_location(fn: str) -> Union[str, None]:
20 + def try_location(fn: str) -> str | None:
21 |     ''' try to find file from current location and then
   |

Found 451 errors.
[*] 310 fixable with the `--fix` option (36 hidden fixes can be enabled with the `--unsafe-fixes` option).
```
