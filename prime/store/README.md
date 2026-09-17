# `store`

The `store` package loads a table of prime numbers from a text file or a
pickle file and provides lookup helpers for querying that table.

## Public API

The package exports these primary classes and functions:

- `GetConfig`: reads `setting.json` and resolves the configured prime-data
	paths.
- `StorePrime`: loads, queries, and optionally saves an uncompressed prime
	table.
- `LoadCompressPrime`: loads and saves a compressed prime table when the
	optional compressed-loader module is available.
- `QueryPrime`: the base query implementation used by `StorePrime`; import it
	from `store.query_prime` when needed.
- `read_textfile`: loads one integer per line from a text file.
- `make_arrow`: formats the direction between a value and nearby primes.
- `prt`, `dbg`, `MyDebug`, and `MyVerbose`: shared output and diagnostic
	utilities.

The package also re-exports several helpers from the shared `myutil` module,
including `get_home`, `read_setting`, `is_file`, and `is_dir`.

## Basic Usage

Use `GetConfig` to select one of the data sets defined in `setting.json`, then
pass its text and pickle paths to `StorePrime`:

```python
from store import GetConfig, StorePrime

config = GetConfig()
config.set_configkey("big")

with StorePrime(
		txtfn=config.get_full_path("txt"),
		pfn=config.get_full_path("pickle"),
) as primes:
		print(primes.get_count())
		print(primes.get_around(100))
		print(primes.list_nearby(100))
```

The context manager loads the pickle when it exists. If the pickle is missing,
it loads the configured text file and saves a pickle when the context exits.

## Configuration

By default, `GetConfig` reads `setting.json` from the current working
directory. The file defines the prime-data directory and the available data
sets: `small`, `big`, `large`, `h119`, and `h422`.

Each data set provides these keys:

- `txt`: text-file name
- `pickle`: pickle-file name
- `compress_pickle`: compressed pickle-file name
- `max`: largest prime in the data set
- `num`: number of primes in the data set

The default data directory is `.prime` under the user home directory. The
loader also looks there when a relative input path is not found in the current
directory.

## Direct Execution

The preferred way to use the package is through its public imports:

```bash
python -c "from store import StorePrime"
```

`query_prime.py` can also be run directly as a module or script; it only
prints a message and does not load prime data by itself:

```bash
python -m store.query_prime
python store/query_prime.py
```

Most other files in this directory are package modules and should be imported
through `store` rather than run as standalone scripts.

## Development Checks

From the repository root:

```bash
python -m ruff check store
python -m pytest -q
```
