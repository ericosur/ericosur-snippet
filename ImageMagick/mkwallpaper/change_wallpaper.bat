@echo off

rem dir /s/b d:\share\ngc-dl\*.jpg > list.txt
dir /s/b d:\share\ngc-dl\*.jpg > list.txt

rem call script to make wallpaper
perl mk_wallpaper.pl

set bmpfile=myngc.bmp

if exist %bmpfile% goto replace
goto end

:replace

rem copy bitmap to %windir%
copy /y %bmpfile% %WINDIR% > nul

rem
rem		change registry
rem 	HKEY_CURRENT_USER\Control Panel\Desktop\Wallpaper
rem
reg add "HKCU\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d %windir%\%bmpfile% /f

rem update user parameters
rundll32 user32.dll,UpdatePerUserSystemParameters

:end

set bmpfile=
