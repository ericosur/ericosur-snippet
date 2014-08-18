@echo off

rem Use nmake if no make availible
rem nmake

perl mkl.pl > dotlist.mak

make
