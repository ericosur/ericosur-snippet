@echo off
echo making list.txt .....
dir /s /b > list.txt

rem		need ''list.txt'', output to ''md5.txt''
echo making md5 list .....
perl d:\ericosur-google\finddup\md5_list.pl

rem		need ''md5.txt'', output to STDOUT
echo matching duplicated file and output to report.txt .....
perl d:\ericosur-google\finddup\get_dup.pl > report.txt

