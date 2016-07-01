test4prime
==========

fact4d.py
---------

___need external python module: sympy___

fact4d.py 將 1000 到 9999 的所有數作質因數分解，其結果輸出於 __4d_fact.txt__

  may use command:

  ```
  grep --color=never '*' 4d_fact.txt > not_prime.txt
  ```

  grep all primes into file: __not_prime.txt__


analprm.pl
----------

___need external perl module: Perl6::Junction___

main() will tell load_file() to load specified file __not_prime.txt__

- show_large_factor() will show all prime factor that is bigger than '$condition'.
  - all prime factors will be stored at __%prime_factor__
