# README

May refer to another repository of mine: [zh2bpmf.pl](https://github.com/ericosur/charencoding/blob/master/appl/zh2bpmf.pl)

## translate text table into json

### working scripts

* Tables are generated from [phone.txt](./phone.txt) by [translate_table.py](./translate_table.py):
    - [phone.json](./phone.json)
    - [bpmf.json](./bpmf.json)

* May use [lookup_bpmf.py](./lookup_bpmf.py) to lookup bopomofo of han characters
*


### data table

- [bopomofo-u8.txt](./bopomofo-u8.txt) 13,053 entries
- [phone.txt](./phone.txt) 1504 lines
    - phonetic spelling of 70,476 han characters
    - unique phonetic spelling: 1492


## layout

```
'/.,;-1234567890abcdefghijklmnopqrstuvwxyz'
'ㄥㄡㄝㄤㄦㄅㄉˇˋㄓˊ˙ㄚㄞㄢㄇㄖㄏㄎㄍㄑㄕㄘㄛㄨㄜㄠㄩㄙㄟㄣㄆㄐㄋㄔㄧㄒㄊㄌㄗㄈ'
```
