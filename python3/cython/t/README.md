# README

trivia demo for cython

before, pure python...

```
kitty:~/t$ time py3 fibo.py
102334155

real    0m42.000s
user    0m41.988s
sys 0m0.012s
```

after, using cython...

```
kitty:~/t$ time py3 call_fibo.py
102334155

real    0m7.840s
user    0m7.836s
sys 0m0.004s
```

## how-to

fibo.py and fibo.pyx is the same

1. prepare **setup.py**
2. run this: ```python3 setup.py build_ext --inplace```
3. using **call_fibo.py** to run the function

## note

2023-03-20 validate against python 3.10

