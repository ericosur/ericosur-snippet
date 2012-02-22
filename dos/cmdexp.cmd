:: Sample usage

@echo off

rem extract the sub to use, not execute it directly

setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
call :sleep 1
call :IsConnected
if %IsConnected%==0 (echo Connected) else echo Not connected
call :GetIP
echo %GetIP%
call :GetSubnet
echo %GetSubnet%
call :GetGateway
echo %GetGateway%
call :GetHostName
echo %GetHostName%
call :GetVolumeName H:
if "%GetVolName%" GTR "" (echo %GetVolName%) else echo.
call :GetFreeSpace D:
echo %GetFreeSpace%
call :FirstAvailableDriveLetter
if "%FirstAvailableDriveLetter%" GTR "" (
  echo %FirstAvailableDriveLetter%
  net use %FirstAvailableDriveLetter% \\%COMPUTERNAME%\C$ /persistent:no
  set DIRCMDORG=%DIRCMD%
  set DIRCMD=
  dir %FirstAvailableDriveLetter%
  set DIRCMD=%DIRCMDORG%
  net use %FirstAvailableDriveLetter% /delete
)
call :DateTimeName "C:\work\my test.doc"
echo %DateTimeName%
set test=Paul R. Sadowski
call :StrLen %test%
echo %test% is %StrLen% characters in length.
goto :EOF

:: Subroutines

:sleep
:: sleep for x number of seconds
ping -n %1 127.0.0.1 > NUL 2>&1
goto :EOF

:IsConnected
:: check if Internet connected
setlocal
ping whois.arin.net | find "TTL" > NUL
if ERRORLEVEL 1 (set IsConnected=1) ELSE (set IsConnected=0)
endlocal & set IsConnected=%IsConnected%
goto :EOF

:GetIP
:: IP for primary adapter
setlocal
for /f "delims=: tokens=1-2" %%c in ('ipconfig /all ^| find "IP Address"') do set GetIP=%%d
endlocal & set GetIP=%GetIP:~1%
goto :EOF

:GetSubnet
:: Subnet Mask for primary adapter
setlocal
for /f "delims=: tokens=1-2" %%c in ('ipconfig /all ^| find "Subnet Mask"') do set GetSubnet=%%d
endlocal & set GetSubnet=%GetSubnet:~1%
goto :EOF

:GetGateway
:: Default Gateway
setlocal
for /f "delims=: tokens=1-2" %%c in ('ipconfig /all ^| find "Default Gateway"') do set GetGateway=%%d
endlocal & set GetGateway=%GetGateway:~1%
goto :EOF

:GetHostName
:: Hostname of local machine
setlocal
for /f "delims=: tokens=1-2" %%c in ('ipconfig /all ^| find "Host Name"') do set GetHostName=%%d
endlocal & set GetHostName=%GetHostName:~1%
goto :EOF

:GetVolumeName
:: Retrieves the volume name for the specified drive
setlocal
if EXIST %1\NUL (
  for /f "tokens=5* delims= " %%c in ('vol %1') do (
    if NOT "%%d"=="" set GetVolumeName=%%d
  )
)
endlocal & set GetVolumeName=%GetVolumeName%
goto :EOF

:GetFreeSpace
:: Returns the free disk space in bytes for the specified drive
:: Returns -1 on error
setlocal
set GetFreeSpace=-1
if EXIST %1\NUL (
  for /f "usebackq tokens=1-10" %%a in (`dir /-p /-s /-c %1 ^| findstr /i /C:" Bytes Free"`) do set GetFreeSpace=%%c
)
endlocal & set GetFreeSpace=%GetFreeSpace%
goto :EOF


:FirstAvailableDriveLetter
:: Find first available drive letter
:: change the test share as appropriate for your system
setlocal
for %%c in (C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
  if NOT EXIST %%c:\NUL (
    net use %%c: \\%COMPUTERNAME%\C$ /persistent:no > NUL 2>&1
    if NOT ERRORLEVEL 1 (
      endlocal & set FirstAvailableDriveLetter=%%c: & net use %%c: /delete > NUL 2>&1 & goto :EOF
    )
  )
)
endlocal
goto :EOF

:DateTimeName
::Adds date and time to a filename
::such as my C:\work\my test.doc becomes
::C:\work\my test-06-25-2004.15.33.23.doc
setlocal
set DateTimeName=%DATE:/=-%.%TIME::=.%
set DateTimeName=%DateTimeName:~0,-3%
set DateTimeName=%~d1%~p1%~n1-%DateTimeName:~4%%~x1
endlocal & set DateTimeName=%DateTimeName%
goto :EOF

:StrLen
:: Get the length of a string
setlocal & set TmpCnt=%*
if not defined TmpCnt (
  set StrLen=0
) else (
:Lenloop
  set TmpCnt=%TmpCnt:~1%
  set /a StrLen +=1
  if defined TmpCnt goto Lenloop
)
endlocal & set StrLen=%StrLen%
goto :EOF
