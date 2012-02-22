@echo off
perl num-to-desk.pl > nul
grep '(1)' all-desk.txt >1.txt
grep '(2)' all-desk.txt >2.txt
grep '(3)' all-desk.txt >3.txt
grep '(4)' all-desk.txt >4.txt
grep '(5)' all-desk.txt >5.txt
grep '(6)' all-desk.txt >6.txt
grep '(7)' all-desk.txt >7.txt
grep '(8)' all-desk.txt >8.txt
wc -l ?.txt > cnt.txt
perl percent.pl
