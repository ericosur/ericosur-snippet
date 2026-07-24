# Kana Utilities

Small scripts and data files for experimenting with Japanese kana orderings.

## Scope

This folder focuses on:

- 平仮名 (hiragana)
- 片仮名 (katakana)
- Traditional ordering notes such as いろは

The data includes old kana characters like ゐ / ゑ and placeholder entries (`？`) in the ya/wa rows.

## Files

- `ab.py`
	- Core data module.
	- Defines kana in both 1D and 2D Python lists:
		- `hira1d`, `kata1d`
		- `hiragana`, `katakana`
- `hira.py`
	- Imports `hiragana` and `katakana` from `ab.py` and prints each row.
	- Useful as a quick visual dump of the table layout.
- `iroha.py`
	- Uses the Iroha poem (`いろはにほへと...`) and maps each character to its index in `hira1d`.
	- Prints each character with its gojuon-based position (1-based index).
- `kana.py`
	- Loads kana from plain-text files (`Lowercase.txt`, `Capital.txt`) and prints grouped output.
	- Uses a `magics` grouping list to control row widths.
	- Can also emit grouped data in Python-list style via `output_py()`.
- `Lowercase.txt`
	- One hiragana character per line.
- `Capital.txt`
	- One katakana character per line.

## Quick Usage

Run scripts from this directory:

```bash
cd kana
python3 hira.py
python3 iroha.py
python3 kana.py
```

Notes:

- `hira.py` and `iroha.py` import from `ab.py`, so running them from this folder is the simplest path.
- `kana.py` reads `Lowercase.txt` and `Capital.txt` via relative paths.

## Related Folder

The `kanji/` subfolder is a separate workflow for 常用漢字 (Joyo Kanji) data generation and format conversion.

## Terms (Reference)

- 変体仮名 (へんたいがな)
- 異体仮名
- 万葉仮名 (まんようがな / Manyogana)
