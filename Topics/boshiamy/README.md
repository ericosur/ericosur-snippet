README
======

## 嘸蝦米查碼

官方 http://boshiamy.com/liuquery.php

## data from

- [Blocks.txt](http://unicode.org/Public/UNIDATA/Blocks.txt)
    - updated on 2021-11-03 (v14.0.0)
- [boshiamy_radicals.txt](https://terryhung.pixnet.net/blog/post/27952497)
    - which is close to __terry_THLiu.txt__
- [phone.txt](https://github.com/chinese-opendesktop/cin-tables)
- [r12a converter](https://r12a.github.io/app-conversion/)


## usage

### lookup

Launch python script with boshiamy radicals.
It will list all possible characters.
May also use regular expression like:

```
python3 find_spell.py ix qm ^jn ^.gz$ ^uue$
```

### cin -> json

* convert boshiamy_radicals.txt to liu.json by using __split_radicals.py__


### unicode reference

result from __filter.py__

CJK Unified Ideographs
CJK Unified Ideographs Extension A-G

http://zht.glyphwiki.org/

#### CJK Unified Ideographs Extension A

wiki: https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_A
U+3400 .. U+4DBF
6,592 code points
6,582 assigned
> filter.py got 6,582 (pass)
https://unicode.org/charts/PDF/U3400.pdf


#### CJK Unified Ideographs Extension B

wiki: https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_B
U+20000 .. U+2A6DF
42,720 code points
42,711 assigned
> filter.py got 42,708 (3 missing)
missing (in hex)
20085,𠂅,lwvz
雍丸
22028,𢀨,ffab
巨郎
22029,𢀩,pbbi
𠂹左

2a6d7 .. 2a6df (no char here)

https://unicode.org/charts/PDF/U20000.pdf

U+21D53    𡵓

#### CJK Unified Ideographs Extension C

wiki: https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_C
U+2A700 .. U+2B73F
4,160 code points
4,149 assigned
> filter.py got 4,149 (pass)
https://unicode.org/charts/PDF/U2A700.pdf

#### CJK Unified Ideographs Extension D

wiki: https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_D
U+2B740 .. U+2B81F
224 code points
222 assigned
> filter.py got 222 (pass)
https://unicode.org/charts/PDF/U2B740.pdf

#### CJK Unified Ideographs Extension E

wiki: https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_E
U+2B820 .. U+2CEAF
5,776 code points
5,762 assigned
> filter.py got 0
https://unicode.org/charts/PDF/U2B820.pdf

#### CJK Unified Ideographs Extension F

wiki: https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_F
U+2CEB0 .. U+2EBEF
7,488 code points
7,473 assigned
> filter.py got 0
https://unicode.org/charts/PDF/U2CEB0.pdf


#### CJK Unified Ideographs Extension G

wiki: https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_F
U+30000..U+3134F
4,944 code points
4,939 assigned
https://www.unicode.org/charts/PDF/U30000.pdf

### tips

* sed specified line from a text file
```
sed -n 25709,39137p many_lines_text.txt
```

* combine
```
cat common.txt ext-a.txt ext-b.txt ext-c.txt ext-d.txt > cc.txt
```
