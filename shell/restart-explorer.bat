@echo off

rem the trivia way: (no external tools)
taskkill /f /im explorer.exe & start explorer.exe

exit

REM Find the PID of explorer.exe
for /f "skip=3 tokens=2" %%a in ('tasklist /FI "IMAGENAME eq explorer.exe"') do (
    set "PID=%%a"
    goto :found
)
echo explorer.exe is not running.
goto :end

:found
echo Killing explorer.exe with PID %PID%
taskkill /F /PID %PID%

REM Wait a bit to ensure explorer.exe has exited
timeout /t 2 >nul

REM Restart explorer.exe
start explorer.exe
echo explorer.exe restarted.

:end
