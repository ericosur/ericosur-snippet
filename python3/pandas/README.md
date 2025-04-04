# README on pandas

In this folder, python scripts uses the following modules to manipulate data table:
    - csv
    - pandas
    - openpyxl

- [hello_pd.py](./hello_pd.py) is a simple python script that uses module pandas to do some filter on data table. [reference](https://ithelp.ithome.com.tw/articles/10194003)

## module

use the following command to install necessary modules

```bash
pip install -r requirement.txt
```

### hello_pd.py

This script read data from **rates.csv** and show some examples to use ```pandas.DataFrame```.

The data table is manually tailored from [Bank of Taiwan](https://rate.bot.com.tw/xrt?Lang=zh-TW) and saved as ```rates.csv```

TODO: how to use the csv exported from previously metioned URL?

### driving_data.py

#### easy start

- easiest way: run ```make```, it will download data from google drive and show details

- run ```make check``` if anything wrong happens

#### description

config: ```$HOME/Private/driving_data.json```

This script uses ```driving_data.csv``` which is located at google spreadsheet. The table will look like:

| date     | duration |
|:--------:|:--------:|
|2018-09-05|54:15.96  |
|2018-09-07|52:09.26  |

Actions of this script:

- downloads data table from gspread by itself (need network, apikey)
- saves table as local csv file
- read data from csv file
- output some statistic values like mean and median number

There is a sample script to demo how to use curl to download gspread worksheet
by curl.

### empty_book.py

A trivia sample of module _*_openpyxl_*_ that could read/write xlsx format file.
