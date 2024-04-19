# kid RSA

[KID RSA](https://www.cs.uri.edu/cryptography/publickeykidkrypto.htm)

## algorithm

```latex
M =  a * b -1

e =  a1 * M + a

d =  b1 * M + b

n = (e * d ) / M = a1 * b1 * M + a * b1 + a1 * b +1
```

## files

* fulltest.py is the script to run test and run at CLI

* the following scripts are using console module of pythonista:
  * fulltest.py
  * encrpyt.py
  * decrypt.py
  * genkey_sta.py
  * help_modulo.py

* utility modules:
  * kid_rsa.py (implementation of algorithm)
  * sta_prompt.py (for pythonista input/output)

For common CLI usage, only kid_rsa.py is required, refer to **fulltest.py** for the function usage.
