@echo off

rem batch to retrieve date string according to system locale correctly

set yy=
set mm=
set dd=
call :getyymmdd yy mm dd

set yy=%yy:~0,4%
set mm=%mm:~0,2%
set dd=%dd:~0,2%
echo.[%yy%]
echo.[%mm%]
echo.[%dd%]
echo.%yy%%mm%%dd% | clip
goto:eof

:getyymmdd
setlocal
for /f "skip=1 tokens=3-6 delims=:(\-/)" %%a in (
  'echo.^|date'
) do (
  goto:%%a%%b%%c
)

:yymmdd
echo Get date in yymmdd format
set yy=%date:~0,4%
set mm=%date:~5,2%
set dd=%date:~8,2%
goto:result

:mmddyy
echo Get date in mmddyy format
set mm=%date:~0,2%
set dd=%date:~3,2%
set yy=%date:~6,4%
goto:result

:ddmmyy
echo Get date in ddmmyy format
set dd=%date:~0,2%
set mm=%date:~3,2%
set yy=%date:~6,4%
goto:result

:yyddmm
echo Get date in yyddmm format
set yy=%date:~0,4%
set mm=%date:~5,2%
set dd=%date:~8,2%
goto:result

:result

endlocal & (set %~1=%yy% & set %~2=%mm% & set %~3=%dd%)
exit /b
