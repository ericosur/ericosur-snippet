@echo off

rem demo how to take the part of date/time string

:: take the first 10 char like 2007/01/01
set mydate=%date:~0,10%

:: replace '/' into null
set mydate=%mydate:/=%

set mytime=%time:~0,8%

echo %mydate%
echo %mytime%

set mydate=
set mytime=

