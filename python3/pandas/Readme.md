# readme

In this folder, some python scripts uses module *__*csv*__* and *__*pandas*__*
to manipulate data table.

hello_pd.py is a simple python script that uses module pandas to do some
filter on data table.

[reference](https://ithelp.ithome.com.tw/articles/10194003)

## module

install **pandas** module if needed

```
$ sudo -H pip install pandas
```

### hello_pd.py ###

This script read data from **rates.csv** and show some examples to use
*__*pandas.DataFrame*__*.

The data table is manually tailored from [Bank of Taiwan](https://rate.bot.com.tw/xrt?Lang=zh-TW) and saved as *__*rates.csv*__*

TODO: how to use the csv exported from previously metioned URL?

### driving_data.py ###

config: ```$HOME/Private/driving_data.json```

This script uses *__*driving_data.csv*__* which is located at google spreadsheet.
The table will look like:

| date | duration |
|:----:|:--------:|
|2018-09-05|54:15.96|
|2018-09-07|52:09.26|

Actions of this script:
  * downloads data table from gspread by itself (need network, apikey)
  * saves table as local csv file
  * read data from csv file
  * output some statistic values like mean and median number

There is a sample script to demo how to use curl to download gspread worksheet
by curl.
