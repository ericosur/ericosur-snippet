# README

## invoke

Just ```make```. Use ```make clean``` to remove generated files.
Currently the script ```mkraw.py``` generates:

- kanji.yaml
- kanji.json
- kanji_one_char_one_line.txt

- raw.txt
  It is manual copy from ```joyokanjihyo_20101130.pdf``` and paste to ```raw.txt```.

### joyokanji

- 常用漢字(joyo kanji) of Japanese data from: https://ja.wiktionary.org/wiki/%E4%BB%98%E9%8C%B2:%E5%B8%B8%E7%94%A8%E6%BC%A2%E5%AD%97%E3%81%AE%E4%B8%80%E8%A6%A7

- joyo kanji of japanese, total 2136 characters (since 2010)

- If consider Kyūjitai ("旧字体", old-form kanji) vs Shinjitai ("新字体", new-form of kanji). There are 5314 old-kanji characters.

github resource:
- https://github.com/mimneko/kanji-data
- https://github.com/himeyama/joyo-kanji
- https://gist.github.com/KEINOS/fb660943484008b7f5297bb627e0e1b1


other references:
- [新字體](https://zh.wikipedia.org/zh-tw/%E6%96%B0%E5%AD%97%E4%BD%93)
- [日本漢字](https://zh.wikipedia.org/zh-tw/%E6%97%A5%E6%9C%AC%E6%B1%89%E5%AD%97)

## reference

- GB/T 2312標準共收錄6763個漢字，其中一級漢字3755個，二級漢字3008個；同時收錄了包括拉丁字母、希臘字母、日文平假名及片假名字母、注音符號、俄語西里爾字母在內的682個字符。(https://zh.wikipedia.org/wiki/GB_2312)

- For big5 table, there are about 13063 han characters in it.


- 《大漢和辭典》是最大的日本漢字字典，共記載接近四萬五千個漢字，不過現代日文的常用漢字僅約兩千餘字。

- 《康熙字典》共載47,043字頭。

- 中華民國教育部為了推動國字標準化政策，自1973年起開始整理國字，直到1982年頒布了「常用國字標準字體表」4808字與「次常用國字標準字體表」6341字。後又經多次局部修改，最新一次修改是1998年。後並頒佈常用國字標準字體筆順手冊，規定國字標準筆順寫法。

- It is a rough category
  - zh_CN for simplified chinese
  - zh_TW for tradition chinese
  - ja for japanese (here I metion about joyo kanji)

  - It is not a definite number that one person should read/write how many han characters. 依據黃富順（民83）的研究，(zh_TW) 一般成人日常生活所需之基本字彙為 2,328 字

  - I use a de facto (rather old) han character standard to guess how many han characters for zh_CN (6763), zh_TW (13063), ja (2136). The de facto does not cover all han character in everyday life, but it could handle at least 90% to 95% daily use.

- Great we have unicode. Even unicode collects tons of han characters that seems no body uses, the number is still growing.

- [基於花園明朝字體的開放原始碼中文字型](https://github.com/max32002/max-hana)

- [漢文教育用基礎漢字](https://zh.wikipedia.org/zh-tw/%E6%BC%A2%E6%96%87%E6%95%99%E8%82%B2%E7%94%A8%E5%9F%BA%E7%A4%8E%E6%BC%A2%E5%AD%97) about 1,800 characters
