Google Spreadsheet Demo
=======================

'update_rebootlog.sh' will enter venv of python3.x, and calling 'update_worksheet.py' with proper arguments.

update_worksheet.py will get some data from myutil.py, and then write these data into a specified google spreadsheet "rebootlog".


$ pyvenv-3.5 my_env
$ source my_env/bin/activate

Reference
=========

gspread

documentation:
http://gspread.readthedocs.io/en/latest/#exceptions

github:
https://github.com/burnash/gspread
