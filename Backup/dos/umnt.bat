@echo off

rem unmount the connection
rem maybe I should use the for-loop

echo mount M drive
net use m: /delete >nul

echo mount N drive
net use n: /delete >nul

echo mount X drive
net use x: /delete >nul

echo mount x drive
net use x: /delete >nul

echo mount y drive
net use y: /delete >nul

echo mount Z drive
net use z: /delete >nul
