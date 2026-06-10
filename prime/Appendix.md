# Appendix

This file summarizes historical notes that were removed from `README.md` during
the cleanup. They are kept here for reference without making the main README
harder to scan.

## Historical Note

The old README opened with a note about the GIMPS record prime announced on
2018-12-07:

```text
2^82,589,933 - 1
```

It has 24,862,048 digits and was credited there to P. Laroche, G. Woltman,
A. Blosser, and others.

## Removed Script Notes

The previous README mentioned a few scripts or data names that are not part of
the current top-level folder inventory:

- `factor.pl`: described as using `basic_prime.txt` as a prime table.
- `fac_by_table.pl`: described as using `prime_100k.txt` or `prime_1M.txt`.
- `search_in_primes.py`: described as reading `prime_100k.txt`, caching it as
  `primes.p`, and returning nearby lower/upper primes such as `23 <<<<< 29`
  for an input near `24`.

The current equivalent for `search_in_primes.py` lives under `100k/`, and
`run_example.py` is marked in that script as the upgraded version.

## Old Prime Table Notes

The old README listed these table descriptions:

| file | description |
| --- | --- |
| `basic_prime.txt` | Primes under 1,000; first `2`, last `991`, total `168`. |
| `prime_100k.txt` | 100,000 primes; last prime `1,299,709`. |
| `prime_1M.txt` | 1,000,000 primes; last prime `15,485,863`. |

It also linked prime table downloads from:

- <http://primes.utm.edu/lists/small/millions/>

## Shell Tips From The Old README

Extract the prime column from the first 100 rows of a two-column prime table:

```bash
head -100 prime_100k.txt | cut -d ' ' -f 2
```

Pick random rows from a large file:

```bash
shuf -n 10 large.txt
```

Pick random rows and check them with `check_prime.py`:

```bash
shuf -n 10 large.txt | python3 check_prime.py -
```

Print one line or a range of lines:

```bash
sed -n 23p large.txt
sed -n 100,120p large.txt
```

## Prime Curios

The old README kept a short "curios" section:

- `2^2 + 3^2 + 4^2 = 29`
- `2^3 + 3^2` was noted as `8 + 9`.
- `064810` was noted as `0 * 8^2 * 9^2 * 0`.

Related links from that section:

- <https://t5k.org/curios/page.php/56.html>
- OEIS, the On-Line Encyclopedia of Integer Sequences: <https://oeis.org/>

## Primesieve Benchmarks

The previous README recorded local `primesieve 2147483648000 --time` results
for several machines. All runs reported:

```text
Primes: 78502287015
```

Summary of recorded timings:

| machine | sieve size | threads | seconds |
| --- | ---: | ---: | ---: |
| `jeff` | 256 KiB | 16 | 62.109 |
| `kitty` | 128 KiB | 8 | 164.921 |
| `rasmus@zen33` | 128 KiB | 8 | 203.400 |
| `pixel6a` | 256 KiB | 8 | 214.921 |
| `rasmus@tuf` | 256 KiB | 12 | 221.339 |
| `d:\Tool` | 128 KiB | 4 | 465.456 |

These numbers are machine-specific and should not be treated as general
performance claims.

## Line Count Benchmarks

The old README also stored benchmark results for `line_count.py` across several
machines and Python versions. The tested functions included:

- `wccount`
- `bufcount`
- `itercount`
- `kylecount`
- `opcount`
- `mapcount`
- `simplecount`
- older runs also included `fadvcount`

High-level observations from the saved tables:

- On `jeff.local` with Python 3.8.10 and `--clear-cache`, `wccount` was fastest
  at about `0.029` seconds minimum, followed by `bufcount`.
- On `tuf.local` with conda Python 3.10 and `--clear-cache`, `wccount` was also
  fastest at about `0.034` seconds minimum.
- On `tuf.local` with conda Python 3.9.17 and `--clear-cache`, `wccount`
  remained fastest at about `0.028` seconds minimum.
- On `kitty.local` with Python 3.10.12 and `--clear-cache`, Python-level
  iteration methods appeared faster than `wccount` in that recorded run.
- Older historical runs compared Python 3.1 behavior, `/big/mkv/file`, and
  cache-cleared runs where relative rankings varied.

The exact raw tables were removed from the main README because they are long,
environment-specific, and better treated as dated benchmark notes.

## Removed References

The old reference list contained:

- <http://prime-numbers.org/>
- <http://primes.utm.edu/lists/small/millions/>
- <https://www.geeksforgeeks.org/special-prime-numbers/>
