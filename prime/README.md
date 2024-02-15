# Readme

> New record prime (GIMPS): $2^{82,589,933}-1$ with 24,862,048 digits by P. Laroche, G. Woltman, A. Blosser, et al. (7 Dec 2018).

[TOC]

###### tags: ```python3``` ```script``` ```python``` ```prime``` ```shuf``` ```sed``` ```cut```

## scripts

- ```factor.pl``` takes **basic_prime.txt** as prime number table
- ```fac_by_table.pl``` takes **prime_100k.txt** or **prime_1M.txt** as table
- ```fprm.py``` use small primes to filter out non-primes

- ```search_in_primes.py```
  needs text data file ```prime_100k.txt```, will save it as ```primes.p``` for futher use. It answers lower/upper primes near the given number. For example, given 24, will get ```(23 <<<<< 29)```. It means between ```(23, 29)``` and closer to ```23```.

- ```nearby_primes.py``` could list nearby primes from specified number
- ```miller_rabin.py``` to test if a prime number

- ```goldbach_conj.py``` implements [goldbach's conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture) that any even number ($< 10^{14}$ ) could be sum of two primes

> python scripts with ```_sta``` means it runs under iOS [pythonista](http://omz-software.com/pythonista/)

## prime number table

* basic_prime.txt: prime numbers under 1,000 (first is 2, last is 991, with 168 prime numbers)
* prime_100k.txt: 100,000 prime numbers (last is 1,299,709)
* prime_1M.txt: one million prime numbers (last is 15,485,863)

> tables could be downloaded at
[millions primes](http://primes.utm.edu/lists/small/millions/)

## tips

### how to cut the prime colume from head 100 lines

The format of prime_100k.txt is:

id  prime
\d+\s+\d+

```
head -100 prime_100k.txt | cut -d ' ' -f 2
```

### pick several lines from a large file randomly

big.txt and large.txt are rather large file, use **shuf** to pick random lines
from such file

```
shuf -n 10 large.txt
```
and use **check_prime.py** to test
```
shuf -n 10 large.txt | python3 check_prime.py -
```

### pick specified line from file

print line 23 from large.txt (show the 23rd prime)

```
sed -n 23p large.txt
```

print line 100 to 120
```
sed -n 100,120p large.txt
```

## somehow curios

* $2^2+3^2+4^2=29$
* $2^3+3^2$ means $8+9$
* $064810$ means $0 \cdot 8^2 \cdot 9^2 \cdot 0$

### web sites
  - https://t5k.org/curios/page.php/56.html
  - OEIS On-Line Encyclopedia of Integer Sequences

## primesieve

```
jeff:~$ primesieve 2147483648000 --time
Sieve size = 256 KiB
Threads = 16
100%
Seconds: 62.109
Primes: 78502287015

kitty:~$ primesieve 2147483648000 --time
Sieve size = 128 KiB
Threads = 8
100%
Seconds: 164.921
Primes: 78502287015

rasmus@zen33:~$ primesieve 2147483648000 --time
Sieve size = 128 KiB
Threads = 8
100%
Seconds: 203.400
Primes: 78502287015

pixel6a $ primesieve 2147483648000 --time
Sieve size = 256 KiB
Threads = 8
100%
Seconds: 214.921
Primes: 78502287015

rasmus@tuf:~$ primesieve 2147483648000 --time
Sieve size = 256 kilobytes
Threads = 12
100%
Seconds: 221.339
Primes: 78502287015

d:\Tool> primesieve 2147483648000 --time
Sieve size = 128 KiB
Threads = 4
100%
Seconds: 465.456
Primes: 78502287015
```

## line_count

- use big.txt
- jeff.local, py3.8.10, --clear-cache
```
function      average, s  min, s  ratio
wccount             0.03   0.029   1.00
bufcount           0.037   0.037   1.28
itercount          0.087   0.085   2.98
kylecount           0.11     0.1   3.57
opcount              0.1     0.1   3.60
mapcount            0.11    0.11   3.71
simplecount         0.11    0.11   3.82
```
- tuf.local, conda py3.10, --clear-cache
```
function      average, s  min, s  ratio
wccount            0.044   0.034   1.00
bufcount           0.048   0.042   1.24
itercount           0.14    0.13   3.95
mapcount            0.16    0.15   4.50
kylecount           0.17    0.16   4.82
simplecount         0.17    0.16   4.90
opcount             0.19    0.18   5.42
```
- tuf.local, conda py3.9.17 --clear-cache
```
function      average, s  min, s  ratio
wccount             0.03   0.028   1.00
bufcount           0.043   0.037   1.32
itercount           0.14    0.14   5.01
opcount             0.16    0.15   5.55
mapcount            0.18    0.16   5.62
kylecount           0.17    0.16   5.67
simplecount         0.18    0.17   6.02
```
- kitty.local, py3.10.12 --clear-cache
```
function      average, s  min, s  ratio
itercount           0.33    0.28   1.00
mapcount            0.43    0.28   1.00
kylecount            0.4    0.29   1.03
simplecount          0.4     0.3   1.09
opcount             0.41     0.3   1.09
bufcount            0.51    0.38   1.38
wccount             0.76    0.41   1.48
```

### old

```
 function      average, s  min, s  ratio
 wccount            0.005  0.0042   1.00
 bufcount          0.0081  0.0081   1.91
 fadvcount         0.0094  0.0091   2.13
 opcount            0.018   0.015   3.42
 simplecount        0.019   0.016   3.66
 kylecount          0.019   0.017   4.03
 mapcount           0.027   0.021   4.97
 itercount          0.044   0.031   7.21
-
# python3.1 ginstrom.py
 function      average, s  min, s  ratio
 wccount           0.0049  0.0046   1.00
 itercount          0.021    0.02   4.47
 mapcount           0.023   0.023   5.09
 bufcount           0.034   0.032   7.02
 opcount            0.043   0.043   9.46
 simplecount         0.05   0.046  10.20
 kylecount           0.05    0.05  10.95
-
# python ginstrom.py /big/mkv/file
 function      average, s  min, s  ratio
 wccount             0.51    0.49   1.00
 opcount              1.8     1.8   3.58
 simplecount          1.8     1.8   3.66
 kylecount            1.9     1.9   3.75
 mapcount              19       2   4.01
 fadvcount            2.3     2.2   4.52
 bufcount             2.3     2.2   4.52
# wc /big/mkv/file
# 7137518   40523351 1836139137 /big/mkv/file
-
# with --clear-cache
 function      average, s  min, s  ratio
 simplecount         0.06   0.057   1.00
 opcount            0.067   0.057   1.00
 kylecount          0.057   0.057   1.00
 itercount           0.06   0.058   1.02
 mapcount           0.059   0.058   1.02
 fadvcount          0.064   0.058   1.02
 bufcount            0.07   0.062   1.09
 wccount            0.072   0.065   1.15

# python3.1 with --clear-cache
 function      average, s  min, s  ratio
 itercount          0.061   0.057   1.00
 simplecount        0.069   0.061   1.06
 mapcount           0.062   0.061   1.07
 wccount            0.067   0.064   1.11
 kylecount          0.067   0.065   1.12
 opcount            0.072   0.067   1.17
 bufcount           0.083   0.073   1.27

```

## references

* http://prime-numbers.org/
* http://primes.utm.edu/lists/small/millions/
* https://www.geeksforgeeks.org/special-prime-numbers/
