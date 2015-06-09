@echo off

for /F "tokens=1,2,3,4 delims=/ " %a in ("apple/ball/cat dog") do echo %a
