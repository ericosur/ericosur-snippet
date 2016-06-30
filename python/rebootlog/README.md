# Google Spreadsheet Demo
## precondition
### install pyvenv
```
$ sudo apt-get install pyvenv-3.5
```
### prepare pyvenv
```
$ cd $HOME
$ pyvenv-3.5 my_env
$ source my_env/bin/activate
```
### how to run
Just run `update_rebootlog.sh`, it will enter a python3 virtual environment, and calling `update_worksheet.py` with proper arguments. `update_worksheet.py` will get some data from `myutil.py`, and then write these data into a specified google spreadsheet "rebootlog".

Reference
=========
- [gspread documentation](http://gspread.readthedocs.io/en/latest/#exceptions)
- [gspread github](https://github.com/burnash/gspread)
- [markdown basic writing and formatting syntax](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
