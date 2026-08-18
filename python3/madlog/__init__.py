#!/usr/bin/env python3

"""Shared logging helpers (rich.console with print fallback, optional loguru backend)."""

from __future__ import annotations

import importlib
from collections.abc import Callable
from contextlib import nullcontext
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from rich.console import Console


class _FallbackConsole:
    """Minimal console fallback when rich is unavailable."""

    def log(self, *args: Any, **kwargs: Any) -> None:
        print(*args, **kwargs)

    def status(self, *_args: Any, **_kwargs: Any):
        return nullcontext()


def get_prt(use_print: bool = False) -> Callable[..., Any]:
    """Return rich.print when available, else built-in print.

    Args:
        use_print: If True, always use built-in print. If False (default),
                   try to use rich.print, fall back to built-in print.

    Returns:
        A callable print function (rich.print or built-in print).
    """
    if use_print:
        return print
    try:
        return importlib.import_module("rich").print
    except ImportError:
        return print


def get_console(warn_msg: str | None = None, warn_printer=None) -> Console | _FallbackConsole:
    """Return rich Console when available, else a fallback console."""
    try:
        Console = importlib.import_module("rich.console").Console
        return Console()
    except ImportError:
        if warn_msg:
            (warn_printer or print)(warn_msg)
        return _FallbackConsole()


def _build_console_logger(console: Any, level: str, style: str):
    """Build one logger callable for a specified level."""
    is_fallback = isinstance(console, _FallbackConsole)

    def _log(*args: Any, **kwargs: Any) -> None:
        if is_fallback:
            console.log(f"[{level}]", *args, **kwargs)
        else:
            console.log(f"[{style}]{level}[/]", *args, **kwargs)

    return _log


def get_loggers(
    use_loguru: bool = False,
    warn_msg: str | None = None,
    warn_printer=None,
):
    """Return (logd, logi, logw, loge) from selected backend.

    Defaults to rich.console; falls back to print when rich is unavailable.
    When use_loguru=True, prefer loguru and fall back to rich/print if unavailable.
    """
    if use_loguru:
        try:
            logger = importlib.import_module("loguru").logger
            return logger.debug, logger.info, logger.warning, logger.error
        except ImportError:
            if warn_msg:
                (warn_printer or print)(warn_msg)

    console = get_console(warn_msg=warn_msg, warn_printer=warn_printer)
    return (
        _build_console_logger(console, "DEBUG", "cyan"),
        _build_console_logger(console, "INFO", "green"),
        _build_console_logger(console, "WARN", "yellow"),
        _build_console_logger(console, "ERROR", "red"),
    )


def get_logd(warn_msg: str | None = None, warn_printer=None, use_loguru: bool = False):
    """Return debug logger callable."""
    return get_loggers(use_loguru=use_loguru, warn_msg=warn_msg, warn_printer=warn_printer)[0]


def get_logi(warn_msg: str | None = None, warn_printer=None, use_loguru: bool = False):
    """Return info logger callable."""
    return get_loggers(use_loguru=use_loguru, warn_msg=warn_msg, warn_printer=warn_printer)[1]


def get_logw(warn_msg: str | None = None, warn_printer=None, use_loguru: bool = False):
    """Return warning logger callable."""
    return get_loggers(use_loguru=use_loguru, warn_msg=warn_msg, warn_printer=warn_printer)[2]


def get_loge(warn_msg: str | None = None, warn_printer=None, use_loguru: bool = False):
    """Return error logger callable."""
    return get_loggers(use_loguru=use_loguru, warn_msg=warn_msg, warn_printer=warn_printer)[3]


prt = get_prt()
logd, logi, logw, loge = get_loggers(
    use_loguru=False,
    warn_msg="[warn] cannot import rich.console",
    warn_printer=prt,
)


__all__ = [
    "get_console",
    "get_logd",
    "get_loge",
    "get_loggers",
    "get_logi",
    "get_logw",
    "get_prt",
    "logd",
    "loge",
    "logi",
    "logw",
    "prt",
]
