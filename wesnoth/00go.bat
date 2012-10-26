@echo off
gzip -d -c fuck.gz > fuck
perl unit.pl > 1.txt
perl gen_cmd.pl

rem uedit32 fuck
rem uedit32 1.txt
