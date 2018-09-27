# readme

hello_pd.py is a simple python script that uses module pandas to do some
filter on data table.

[reference](https://ithelp.ithome.com.tw/articles/10194003)

## module

install **pandas** module if needed

```
$ sudo -H pip install pandas
```

### hello_pd.py ###

This script read data from rates.csv and show some examples to use
*__*pandas.DataFrame*__*.

The data table is manually tailored from [Bank of Taiwan](https://rate.bot.com.tw/xrt?Lang=zh-TW) and saved as *__*rates.csv*__*


### driving_data.py ###

This script uses *__*driving_data.csv*__* which is exported from [google drive](https://docs.google.com/spreadsheets/d/1blQrG8jU20Uy5Vwm1C6FkNjaCKoNW0UWjRCzrwpSSSM/edit#gid=0).
Table looks like:

| date | duration |
|:----:|:--------:|
|2018-09-05|54:15.96|
|2018-09-07|52:09.26|

The script will read the table and output mean and 50% value from table.

