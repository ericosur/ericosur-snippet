Script "ext_stroke.pl" will extract
"kTotalStrokes" data line from
"Unihan_DictionaryLikeData.txt" and result output to
"extract_ktotalstrokes.txt".


At unicode v7, strokes data range U+3400 to U+FA2D,
27826 records.
At unicode v8, strokes data range U+3400 to U+2F986,
74912 records total.

This script will only grep from U+0000 to U+FFFF.

You could get total result from this command:
$ grep kTotalStrokes Unihan_DictionaryLikeData.txt > udld8.txt


How to sort zh-CN zh-TW ?

case 1
單一字時，先用全筆劃排序，相同時，再用部首/餘筆劃排序

1st: kTotalStrokes (small to large)
[1-9][0-9]{0,2}

2st: kRSUnicode (small to large radical-stroke)
[1-9][0-9]{0,2}\'?\.[0-9]{1,2}

字詞的排序，用全筆劃排序，第一字相同再用第二字依序

case 2
漢語拼音字母排序
kHanyuPinyin
(\d{5}\.\d{2}0,)*\d{5}\.\d{2}0:([a-z\x{300}-\x{302}\x{304}\x{308}\x{30C}]+,)*[a-z\x{300}-\x{302}\x{304}\x{308}\x{30C}]+
