# README

This folder contains emoji-related scripts and generated data tables.
The main focus is:

- converting emoji characters to escaped Unicode forms
- generating lookup tables from CLDR annotation XML
- searching or picking emoji by keyword

## Main files

Generated data:

- `en_emoji.py`: English emoji keyword table, generated from CLDR XML
- `cp_emoji.py`: reverse-style table keyed by emoji codepoint string
- `wtf.csv`: CSV-like dump produced from the XML inputs

Source XML copied from CLDR:

- `en-basic.xml`
- `en-derived.xml`
- `zh-basic.xml`
- `zh-derived.xml`

Utility and demo scripts:

- `u8u16.py`: show Unicode escape, UTF-16 escape, and UTF-8 bytes for an emoji
- `mytofrom.py`: conversion helpers used by `u8u16.py`
- `surgg.py`: surrogate-pair related demo
- `pickup.py`: search emoji from keywords listed in `keys.txt`
- `test_emoji.py`: query `en_emoji.py` with a keyword
- `read_enxml.py`: parse CLDR XML and dump CSV-style output
- `parse_enxml.py`: parse CLDR XML and generate Python lookup tables

## Typical usage

### Convert an emoji to escaped forms

```bash
python3 u8u16.py ❤️
python3 u8u16.py 😃
```

Example output shape:

```text
         input: 😃
unicode-escape: \U0001f603
      utf16-be: \ud83d\ude03
       to_utf8: f09f9883
```

This is useful when an editor or downstream format does not handle literal emoji well.

### Search emoji by keyword

```bash
python3 test_emoji.py smile
python3 pickup.py
```

`pickup.py` reads search terms from `keys.txt` and looks them up in `en_emoji.py`.

## Update workflow

If you want to refresh the generated emoji tables, update the CLDR XML inputs first and then
re-run the local generators.

### 1. Prepare a CLDR checkout

Example:

```bash
mkdir -p "$HOME/src/github"
cd "$HOME/src/github"
git clone https://github.com/unicode-org/cldr.git
cd cldr
git checkout release-46-1
```

`runme.sh` expects the CLDR checkout at:

```text
$HOME/src/github/cldr
```

### 2. Regenerate local data

From this `emoji/` directory:

```bash
./runme.sh
```

This script:

1. copies XML files from the CLDR checkout
2. runs `read_enxml.py`
3. runs `parse_enxml.py`

Generated outputs:

- `wtf.csv`
- `en_emoji.py`
- `cp_emoji.py`

## Data format notes

For example, the string `❤️🇧🇴🙋‍♀️🏈😃` may render correctly on a current system, but some tools are
still easier to work with when the emoji is stored as escape sequences.

### JSON / JavaScript / QML

UTF-16 escape sequences are often convenient in JSON-like string literal formats:

```json
{
  "smile": "\ud83d\ude03"
}
```

### Python / C++

Unicode escape sequences such as `\u2764\ufe0f` or `\U0001f603` are often easier to diff, copy,
and keep stable in source files.

## Dependencies

Standard library is enough for some scripts, but XML parsing uses third-party packages:

- `beautifulsoup4`
- `lxml`

Optional console output dependency:

- `rich`

`read_enxml.py` and `parse_enxml.py` will exit with an install hint if `bs4` is missing.

## Related files

- [food/README.md](./food/README.md): notes for the curated food emoji subset
- `sample.json`, `emj.json`: sample input data for conversion tests
- `keys.txt`, `targets.txt`: keyword input lists for lookup scripts
