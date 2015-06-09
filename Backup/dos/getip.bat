@echo off

call :GetIP
echo %GetIP%

:GetIP
:: IP for primary adapter
setlocal
for /f "delims=: tokens=1-2" %%c in ('ipconfig /all ^| %windir%\system32\find "IP Address"') do set GetIP=%%d
endlocal & set GetIP=%GetIP:~1%
goto :EOF

:EOF
