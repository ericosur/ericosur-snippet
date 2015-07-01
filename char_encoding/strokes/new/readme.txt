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
