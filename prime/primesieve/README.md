# README


## build

need **libprimesieve-dev**

```
sudo apt install primesieve libprimesieve-dev
```

## notes

```
$ primesieve 6461335109 --count
Sieve size = 256 KiB
Threads = 12
100%
Seconds: 0.177
Primes: 300000000
```

## next1e8

Generates primes in batches of 100,000,000 (`total_count` in the source), resumable
after a crash/power loss and starting a new batch from a seed file.

```
g++ -O3 next1e8.cpp -lprimesieve -o next1e8
./next1e8
```

Files (all relative to the working directory):
- `primes_part2_1e8.txt` — output, one prime per line, appended across batches (never truncated)
- `next1e8.state` — checkpoint (`count last_prime`), used to resume an interrupted batch
- `next1e8.log` — timestamped START/RESUME/NEW_BATCH/STOP/ERROR events
- `start_after.seed` — one-shot: put a prime value here to start the *next* batch of
  100,000,000 after it once the current batch is complete; consumed (renamed to
  `start_after.seed.used`) once its first checkpoint is durable

Startup priority: an in-progress (incomplete) checkpoint always resumes as-is; otherwise
`start_after.seed` (if present) starts a fresh batch; otherwise falls back to the tail of
`primes_part2_1e8.txt`, or fails if there is no starting point at all.

## querying the generated primes: memory usage

`../combined_prime.py` queries the combined `h422.u32` + `part2.u64` prime tables (built
from this tool's output). Two lookup strategies were measured (`resource.getrusage(...).ru_maxrss`,
1000 random queries across the full 2..8,736,028,057 range):

- `numpy.memmap(...)` + `np.searchsorted(...)`: **2,320 MB RSS after just 1 query**, ~3,846 MB
  after 10+ (in this environment, a single touch pulled in most/all of the mapped file(s) —
  likely aggressive mmap readahead or an overlay-filesystem quirk, not the usual O(log n)
  page-touch behavior).
- Manual `seek()` + `read()` binary search (no mmap): **~16 MB RSS, flat, after 1000 queries.**

Conclusion: prefer `seek()`/`read()` binary search over `mmap`/`searchsorted` for large
sorted binary files here — it's what `combined_prime.py` uses.


