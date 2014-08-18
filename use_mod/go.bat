@echo off

if not exists use.dot goto end
dot -Tpng -o go.png use.dot
start go.png

:end
