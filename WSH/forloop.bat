@echo off

rem repeat ten times
set var=1 2 3 4 5 6 7 8 9 0
for %%i in (%var%) do  (
    openssl rand 16 -hex
)
