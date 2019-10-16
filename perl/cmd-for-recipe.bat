@echo off

rem
rem some quick tips and recipes about ''for'' in the cmd shell
rem
rem 2007/11/07 by ericosur

echo.
echo recipes about using the "FOR" shell command
echo.
goto end

rem list the line of first column
:for /f "tokens=1 delims=" %%f in (file.txt) do echo %%f

rem list all content from file.txt
:for /f "tokens=*" %%f in (file.txt) do echo %%f

rem same as the above
:for /f %%f in ('cat file.txt') do echo %%f

rem print the every line in the ''file.txt'', delims was set to <null>
:for /f "delims=" %%f in (file.txt) do echo %%f

rem parse the cmd /? output
:for /f "delims=" %%x in ('cmd /?') do echo %%x

rem parse the result from '.....'
:for /f "tokens=2 delims=|" %%x in ('exif img_1265.jpg') do echo %%x

rem list all '.jpg' files in the "d:\backup" directory recursively
:for /r "d:\backup" %%g in (*.jpg) do echo %%g
:>for /r "D:\GPS_Study\北海道地圖" %g in (*.zip) do unzip %g

rem parse the ver output and take the string in the []
:for /f "tokens=2* delims=[]" %%g in ('ver') do set _version=%%g
:echo %_version%

rem take the first token from "date /t" output
:for /f "tokens=1" %%g in ('date /t') do set _date=%%g
:echo %_date%

rem list every variables from environment
:for /f "delims==" %%g in ('set') do echo %%g

rem take the 3rd part of the path, cannot list every item :(
:for /f "tokens=3* delims=;=" %%x in ('path') do echo %%x

rem list each path name in the ''path'', but would be go crazy if spaces in the string
:for %%g in (%path%) do echo %%g

rem quickly generate a batch file for filelist
:for /f %%f in ('cat file.txt') do echo exif %%f >> delall.bat

:end
