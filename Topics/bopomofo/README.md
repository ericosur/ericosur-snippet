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

```python
a='/.,;-1234567890abcdefghijklmnopqrstuvwxyz'
len(a)=41
b='ㄥㄡㄝㄤㄦㄅㄉˇˋㄓˊ˙ㄚㄞㄢㄇㄖㄏㄎㄍㄑㄕㄘㄛㄨㄜㄠㄩㄙㄟㄣㄆㄐㄋㄔㄧㄒㄊㄌㄗㄈ'
len(b)=41
# 一聲通常不標，注音輸入時且接按空白出字，但空白不代表一聲
輕聲的符號為「˙」
```

## sort

- wiki: https://zh.wikipedia.org/zh-tw/%E6%B3%A8%E9%9F%B3%E7%AC%A6%E8%99%9F
    - 聲母 ㄅㄆㄇㄈ ㄉㄊㄋㄌ ㄍㄎㄏ ㄐㄑㄒ ㄓㄔㄕㄖ ㄗㄘㄙ
    - 介音 ㄧㄨㄩ
    - 韻母 ㄚㄛㄜㄝ ㄞㄟㄠㄡ ㄢㄣㄤㄥ ㄦ

- 注音排序的基本原則
    - 聲母優先： 首先按照聲母的順序排列，例如「ㄅ」排在「ㄆ」之前。
    - 韻母次之： 同一聲母下，再按照韻母的順序排列，例如「ㄅㄚ」排在「ㄅㄛ」之前。
    - 聲調最後： 同一聲母和韻母下，再按照聲調的順序排列，例如「ㄅㄚ」排在「ㄅㄚˊ」之前。

- python module pypinyin: https://github.com/mozillazg/python-pinyin

