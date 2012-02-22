@echo  off

rem my own perl loader

if '%1==' goto err

set plfile=

if exist %1 goto run

set plfile=%1.pl
if exist %1 goto run

set plfile=d:\perl\eric\%1
if exist %plfile% goto run

set plfile=d:\perl\eric\%1.pl
if exist %plfile% goto run

echo still cannot find the perl script file
goto err

:run
d:\perl\bin\perl -w %pifile% %2 %3 %4 %5 %6 %7 %8 %9
goto end

:err
echo please specified perl script file name

:end
set plfile=
