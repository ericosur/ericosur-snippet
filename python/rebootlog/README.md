# Google Spreadsheet Demo
## precondition
### install pyvenv
```
sudgo apt-get install pyvenv-3.5
```
### prepare pyvenv
```
cd $HOME
pyvenv-3.5 my_env
source my_env/bin/activate
```
### python packages
```
pip install gspread oauth2client pyOpenSSL
```
### how to run
Just run `update_rebootlog.sh`, it will enter a python3 virtual environment, and calling `update_worksheet.py` with proper arguments. `update_worksheet.py` will get some data from `myutil.py`, and then write these data into a specified google spreadsheet "rebootlog".

Reference
=========
- [blog to describe how to use gspread to trace a price](http://city.shaform.com/blog/2016/03/19/gspread.html)
- [gspread documentation](http://gspread.readthedocs.io/en/latest/#exceptions)
- [gspread github](https://github.com/burnash/gspread)
- [markdown basic writing and formatting syntax](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
