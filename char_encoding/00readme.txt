Note
====

data/big5_2003-b2u.txt	(19582)
data/big5-bopomofo.txt	(13053) big5 對應注音符號表
data/big5-bopomofo-u8.txt	(13053) big5 對應注音符號表 save as UTF-8 format
data/bpmf.dat	stored by zh2bpmf.pl
data/cp950-b2u.txt	windows codepage 950 big5 to unicode table (13503)
data/gb2312-normalized-pinyin.txt	(6727) GB2312

big5.txt	(13739)

unihan.txt	取出的 big5 字元有 13063 字 (kBigFive 欄位) *1

diff-out.txt	cp950-b2u.txt 與 kBigFive 的差異比較檔 (440)

內建 table 的 script:

gb18030_4b.pl	GB18030 vs UCS4 table (39339)
gb18030_table.pl	GB18030 vs UCS2 table (21873)
big2003.pl	(19583) big5-2003
bigfive2003table.pl	(19582) big5-2003
ucs2tab.pl

from wiki:
大五碼普遍被認為包含13,053字，但在計算0xA259-0xA261的度量衡單位用字
(兙兛兞兝兡兣嗧瓩糎) ，再減去重收了兩次的「兀」(0xC94A)和「嗀」(0xDDFC)後，
應為13,060字。

*1 可由下列 URL 取得 unihan.txt
http://www.unicode.org/Public/UNIDATA/Unihan.zip
$ grep -i kbigfive unihan.txt > kbigfive.txt

======================================================================
2014-08-18
After fetch unihan unicode 7.0.0, it splits into multiple files.

for documentation:
http://www.unicode.org/reports/tr44/

http://zh.wikipedia.org/wiki/%E5%9B%BD%E5%AE%B6%E6%A0%87%E5%87%86%E4%BB%A3%E7%A0%81
GB0 (GB 2312-80) (6763 han characters)

http://zh.wikipedia.org/wiki/%E5%A4%A7%E4%BA%94%E7%A2%BC
big five (13063 from unihan data)
