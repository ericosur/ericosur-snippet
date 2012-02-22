
fact4d.py 將 1000 到 9999 的所有數作質因數分解，其結果輸出於 4d_fact.txt，
使用 grep --color=never '*' 4d_fact.txt > not_prime.txt，將非質數的
行輸出至 not_prime.txt。

analprm.pl 其中的 

show_large_factor() 會將所有質因數大於 '$condition' 的數印出來。
load_file() 作整理。質因數存於 %prime_factor


