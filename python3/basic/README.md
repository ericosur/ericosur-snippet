# README

## CSV,TSV,DSV

- CSV: Comma-Separated Values
- TSV: Tab-Separated Values
- DSV: Delimiter-Separated Values
  - ref: https://matthodges.com/posts/2024-08-12-csv-bad-dsv-good/

> [!NOTE]
> from: https://myapollo.com.tw/post/page/3/

## more styles for github markdown

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

## Update Summary

update on 2026/08/21

- `ifc.py` supports `--rich` / `-r` for explicit Rich output and `--print` / `-p`
  for stdlib `print` output.
- `ipaddr.py` supports the same mutually exclusive `--rich` / `-r` and
  `--print` / `-p` options.
- `typer_example.py` supports `-h` / `--help` and uses `17` when `-A`, `-B`,
  or `-C` is provided without positional values.
- `getmac.py` was checked successfully with no editor diagnostics. It is a
  Linux/ADB helper that reads the WLAN MAC address from `adb shell ip link
  show wlan0`. Its current output still includes temporary diagnostic labels.

