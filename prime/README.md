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

## references

* http://prime-numbers.org/
* http://primes.utm.edu/lists/small/millions/
