@echo off

rem call py2exe to translate python to executable
python setup.py py2exe

rem zip -r eks-dist.zip dist
rar a eks-dist.rar dist
