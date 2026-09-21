# readme

## primesieve

- To get the nth prime number `primesieve -n 1000000`, get:

```
$ primesieve -n 1000000
Sieve size = 256 KiB
Threads = 2
Seconds: 0.001
Nth prime: 15485863
```

- `primesieve 15485863 --print > p1e6.txt` to store 1 million prime numbers.

```
primesieve 15485863 --print > p1e6.txt
```

- convert txt to python pickle: `py convert_txt.py p1e6.txt p1e6.p --pickle`

