@echo off
dir /s/b > list.txt
perl add_size.pl list.txt outsize.txt
perl calc_total_size.pl outsize.txt

rem del list.txt
rem del outsize.txt
