@echo off
set foo=%date%
set foo=%foo:/=%
set foo=%foo:~4,4%%foo:~0,4%

echo.%foo%


for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (
   set ddate=%%c%%a%%b)

echo.%ddate%
