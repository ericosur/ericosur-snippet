# readme

## num_variants.py

It parses ```../data/Unihan_NumericValues.txt``` and output a json file.

NOTE:
    1. for TW/JP/KR users
       - U+5146 兆 and U+79ED 秭 means 1,000,000,000,000 (1e12), trillion
    2. for SC users, U+5146 兆 and U+79ED 秭 means 1,000,000 (1e6), million
       - and they say 万亿(wànyì) instead

This script will use case 1 (1e12) for 兆. Must be sure the context for this character. There is 1 million times between these cases.

## suzhou_numerals.py

- suzhou numerals: ```〡〢〣〤〥〦〧〨〩〇〸〹〺```
- these characters are not included in ```Unihan_NumericValues.txt```
- some commnets refer to ```suzhou_numerals.py```

