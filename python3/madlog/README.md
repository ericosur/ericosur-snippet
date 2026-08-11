# madlog

Reusable logging helpers for small Python scripts.

## Features

- Rich-first logging (uses `rich.console.Console().log` when available)
- Safe fallback to plain `print` when rich is not installed
- Optional Loguru backend for `debug/info/warning/error`
- Tiny API surface that is easy to copy to other repositories

## Exposed helpers

- `get_prt()`
- `get_console(warn_msg=None, warn_printer=None)`
- `get_loggers(use_loguru=False, warn_msg=None, warn_printer=None)`
- `get_logd(...)`, `get_logi(...)`, `get_logw(...)`, `get_loge(...)`

Module-level callables are also available:

- `prt`, `logd`, `logi`, `logw`, `loge`

## Quick usage

```python
from madlog import get_logd

logd = get_logd("[warn] cannot import rich.console")
logd("hello")
```

If your script needs spinner/status APIs, keep a console instance too:

```python
from madlog import get_console, get_logd

console = get_console("[warn] cannot import rich.console")
logd = get_logd()

with console.status("working...", spinner="dots"):
    # do something
    pass
```

## Optional: use Loguru

```python
from madlog import get_loggers

logd, logi, logw, loge = get_loggers(use_loguru=True)
logi("running with loguru")
```

When Loguru is unavailable, madlog automatically falls back to Rich/print.
