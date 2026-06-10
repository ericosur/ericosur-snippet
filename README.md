# ericosur-snippet

A personal collection of code snippets, small tools, experiments, playgrounds,
and prototypes across several languages and command-line utilities.

The repository is intentionally broad. Most folders are grouped by language,
tool, topic, or experiment type. Recent small utilities are usually written in
Python, while older snippets include Perl, shell, C/C++, Java, Lua, Go, Rust,
QBasic, and Windows-related examples.

## Top-Level Layout

| path | type | description |
| --- | --- | --- |
| `python3/` | Python snippets | Python 3 scripts, tests, and small utilities. |
| `deprecated-python/` | Legacy Python | Older Python material kept for reference. |
| `perl/`, `myperl/` | Perl snippets | Perl examples and helper scripts. |
| `shell/`, `sed/`, `regexp/` | Text and shell tools | Shell, stream-editing, and regular-expression experiments. |
| `C/`, `golang/`, `java/`, `lua/`, `rust/`, `qbasic/` | Language folders | Snippets grouped by programming language. |
| `js/`, `ts/` | Web language snippets | JavaScript and TypeScript examples. |
| `autohotkey/`, `win32/` | Windows tooling | Windows automation and Win32-related snippets. |
| `ImageMagick/`, `exiftool/`, `opencv/`, `graphviz/` | Tool-focused folders | Experiments around image, metadata, computer-vision, and graph tooling. |
| `prime/`, `euler/` | Math folders | Prime-number and Project Euler style experiments. |
| `game/`, `rpi/`, `bin2hex/`, `unzzz/` | Topic folders | Smaller topic-specific experiments and utilities. |
| `phrase/`, `logo/`, `Topics/`, `Workfile/` | Data and notes | Reference material, work files, or topic collections. |
| `Backup/`, `tmp/` | Working folders | Backup or temporary material. |

## Root Files

| file | description |
| --- | --- |
| `README.md` | This overview. |
| `SUBMODULES.md` | Notes for initializing, updating, adding, and removing Git submodules. |
| `.gitmodules` | Registered submodules, including `C/fmt`, `prime/powmod_test/fast-modular-exponentiation`, and `phrase/sc-dictionary`. |
| `.gitignore`, `.ignore` | Ignore rules for Git and search tools. |
| `pylintrc` | Python lint configuration. |
| `py_template`, `tmplate.py` | Python script templates. |
| `dp2px.py` | Android density-independent-pixel and pixel conversion helper. |
| `anafl.pl` | Perl helper that counts files by extension. |
| `cr.pl` | Perl helper for running `pngcrush` on PNG files. |
| `rb` | Shell helper for removing a UTF-8 BOM from a file through an external script. |

## Submodules

This repository uses Git submodules. For a fresh clone:

```bash
git clone --recursive <repo-url>
```

For an existing clone:

```bash
git submodule update --init
git submodule update --recursive --remote
```

See `SUBMODULES.md` for the longer workflow notes.

## Notes

- The repository is a snippet archive, so folders may contain experiments,
  one-off scripts, old prototypes, or partially finished ideas.
- Prefer reading a folder's own README when working inside a specific topic
  directory.
- Some tools assume external command-line programs are installed, such as
  `pngcrush`, ImageMagick, ExifTool, Graphviz, or language-specific runtimes.

## History

- 2026-06-10: refine the README
- 2017-02-22: moved all `qt/` content into `myqt.git`.
- 2014-08-18: migrated snippets from Google Code to GitHub.
