# Prime Scripts

Small command-line experiments and utilities for prime numbers: primality
testing, nearby-prime lookup, Goldbach pairs, sieve generation, prime-date
searches, and prime-table storage.

Most scripts are Python 3. Several use the local `store` package to load prime
tables from text, pickle, or compressed pickle files.

## Requirements

Common dependencies:

- Python 3
- `sympy` for `check_prime.py`, `is_prime.py`, `check_need.py`, and
  `root_square.py`
- `rich`, `typer`, and `pydantic` for `is_prime.py`
- `compress_pickle` for compressed prime tables via `LoadCompressPrime`
- `redis` plus a running Redis server for `prime-redis.py`
- `matplotlib` for `test_exist.py`

The scripts look for prime table files either in this folder or under
`$HOME/.prime`. Table names and limits are configured in `setting.json`.

## Prime Tables

The active table configuration is:

| key | text file | pickle | compressed pickle | max prime | count |
| --- | --- | --- | --- | ---: | ---: |
| `small` | `small.txt` | `small.p` | `small.p.lzma` | 1,299,709 | 100,000 |
| `big` | `big.txt` | `big.p` | `big.p.lzma` | 15,485,863 | 1,000,000 |
| `large` | `large.txt` | `large.p` | `large.p.lzma` | 49,979,687 | 3,000,000 |
| `h119` | `h119.txt` | `h119.p` | `h119.p.lzma` | 1,190,494,759 | 60,000,000 |
| `h422` | `h422.txt` | `h422.p` | `h422.p.lzma` | 4,222,234,741 | 200,000,000 |

Prime tables can be downloaded from:

- <https://primes.utm.edu/lists/small/millions/>

The checked-in `data/prime_100k.txt` contains the first 100,000 primes.

## Main Scripts

| script | purpose |
| --- | --- |
| `is_prime.py` | Typer-based CLI for primality checks using `sympy`, falling back to `gmpy2` if available. It can also search before/after/context ranges, find primes around a value, run demos, and test random odd numbers. |
| `check_prime.py` | Simpler primality checker using `sympy.ntheory.primetest.isprime`; accepts command-line values or stdin with `-s`. |
| `MillerRabin.py` | Miller-Rabin implementation from LiteratePrograms; can test values or generate a random 32-bit probable prime. |
| `miller_rabin.py` | Alternative Miller-Rabin implementation with a modular exponentiation test mode. |
| `nearby_primes.py` | Uses `StorePrime` to list primes near one or more input values. Defaults to the `big` table. |
| `run_example.py` | Demo and smoke-test runner for `StorePrime` and `LoadCompressPrime`; reports whether inputs are prime or between adjacent primes. |
| `goldbach_conj.py` | Finds Goldbach prime pairs for given even numbers using the configured prime table. |
| `goldbach_sta.py` | Pythonista-oriented Goldbach implementation. |
| `fun500.py` | Small Goldbach-style demo that samples prime partners for the value `500`. |
| `sieve.py` | Sieve of Eratosthenes implementation that generates primes up to `1_000_000` and verifies against stored prime tables when possible. |
| `fprm.py` | Older filtering experiment that removes multiples of small primes from numbers below `100000`; `sieve.py` is the faster version. |
| `check_need.py` | Loads primes through `StorePrime` and double-checks every stored value with `sympy`. |
| `prime_date.py` | Searches dates from 2000-01-01 to 2099-12-31 where every left-truncated `YYYYMMDD` value is prime. |
| `root_square.py` | Searches primes of the form `P = m^2 + 2^2`, with `m` also prime, using `StorePrime` and `sympy`. |
| `sqare_root.py` | Older version of `root_square.py` using `MillerRabin.py`. The filename is intentionally left as-is. |
| `fer_sum_two_sq.py` | Unfinished Fermat two-squares experiment. It currently exits immediately. |
| `lc.py` | Binary-searches a sorted prime text file by reading specific line numbers instead of loading the whole file. |
| `line_count.py` | Benchmarks several ways to count lines in a large text file. |
| `prime-redis.py` | Loads prime tables into Redis and compares Redis/list lookup behavior. |
| `test_config.py` | Prints and tests the configured prime table paths. |
| `test_exist.py` | Benchmarks `in`, `set`, and `bisect` membership checks and plots timing results. |
| `the_prt.py` | Tiny helper that exposes `rich.print` when available, otherwise built-in `print`. |

Scripts with `_sta` in the name are intended for iOS
[Pythonista](http://omz-software.com/pythonista/).

## Package And Subfolders

| path | contents |
| --- | --- |
| `store/` | Local support package for loading prime tables, querying nearby primes, reading config, creating arrows, and optional compressed-pickle support. |
| `100k/` | Utilities focused on `prime_100k.txt` lookup. |
| `mk_table/` | Scripts for building or transforming prime tables, including CSV conversion and `primesieve` helpers. |
| `powmod_test/` | Python and Perl experiments for modular exponentiation and last-digit power behavior. |
| `find_in_constant/` | Perl helper for finding prime-looking sequences inside constants. |
| `hards/` | Perl scripts and data for four-digit or "hard" prime experiments. |
| `mr/` | Java Miller-Rabin implementations. |
| `data/` | Checked-in sample prime table data. |

## Examples

Check numbers directly:

```bash
python is_prime.py 97 100 7427466391
python check_prime.py 97 100
```

Read values from stdin:

```bash
shuf -n 10 prime.txt | python check_prime.py -s
shuf -i 1001-9999 -n 10 | python check_prime.py -s
```

Search around a number:

```bash
python is_prime.py 1000000 --around 5
python nearby_primes.py 1000000
```

Find Goldbach pairs:

```bash
python goldbach_conj.py 500 1000
```

Exercise the `StorePrime` loader:

```bash
python run_example.py
python run_example.py --lcp --large 15485863
```

Run the sieve:

```bash
python sieve.py
```

## Useful Shell Snippets

The downloaded prime tables usually have two columns:

```text
id  prime
\d+ \d+
```

Cut the prime column from the first 100 lines:

```bash
head -100 prime_100k.txt | cut -d ' ' -f 2
```

Pick random lines from a large file and check them:

```bash
shuf -n 10 large.txt | python check_prime.py -s
```

Print specific lines from a table:

```bash
sed -n 23p large.txt
sed -n 100,120p large.txt
```

## Notes

The README previously recorded local `primesieve` and line-count benchmark
results. Those measurements are environment-specific, so keep new benchmark
results close to the scripts or in a dated note when comparing machines.

Related references:

- <https://t5k.org/curios/>
- <https://oeis.org/>
- <https://www.geeksforgeeks.org/special-prime-numbers/>
