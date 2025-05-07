# readme

I think there is no absolutely correct/wrong for the following cases. I am a TC user so the following I described may not quite correct for SC or other han character users. Since I can read some of SC materials, some of them are mixed into my usage context as well.

## num_variants.py

It parses ```../data/Unihan_NumericValues.txt``` and output a json file.

### million or trillion

- for TW/JP/KR users
  - U+5146 兆 and U+79ED 秭 (I never used this char for trillion) means 1,000,000,000,000 (1e12), trillion
- for SC (esp. modern China) users, U+5146 兆 and U+79ED 秭 means 1,000,000 (1e6), million, and they say 万亿(wànyì, SC) or 萬億 (TC) for trillion instead.
  - I will know it is an SC context if say 万亿

This script will take case 1 (1e12) for 兆. MUST confirm the context while using  this character 兆. There is 1 million times between them.

### another way to count numbers

I only used it verbally when I was in the military. It is quite strange if you speak numbers like this in usual life. Only for spoken, not for writing. Say ```幺兩三四五六拐八鈎洞``` instead of ```一二三四五六七八九零``` (1234567890). It is easier to tell these numbers if bad voice quality. (compare it to [NATO alpha](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet))

For daily life you use 洞 to metion 零 (zero, 0). Most SC/TC users could understand.
For 七(7) vs 拐, 九(9) vs 鈎, it is less common in daily usage.

### 中文數字大寫

These characters are marked as part of kAccountingNumeric.

- It is mentioned as "Chinese/Mandrin Number Capitals" (中文數字大寫 (壹, 貳, 參, 肆, 伍, 陸, 柒, 捌, 玖, 零, 拾, 佰, 仟)) (1,2,3,4,5,6,7,8,9,ten,hundred,thousand)
- No another capitalized characters for
  - 萬 (ten-thousand, 1e4)
  - 億 (hundred-million, 1e8)
  - 兆 (trillion, 1e12)
- (TC) "dollar", use 圓 while capitalized, and 元 for daily use
- they are used for accounting, bank service, or checks clearing
- While using these characters in checks, MUST NOT (or strongly discouraged to) use simplified or variant form of these characters (like 參 -> 参)

#### bills

##### KRW

- For modern KRW, no han characters on it. (after middle of 20th-centry)

##### NTD

中文數字大寫 is used.

 - coin: 壹圓 / 伍圓 / 拾圓 (1, 5, 10 TWD)
 - coin: no 中文數字大寫 五十 (50 TWD), no han char 20 TWD (hardly see)
 - bill: 壹佰圓 / 貳佰圓 / 伍佰圓 (100, 200, 500 TWD) (200 is hardly to see)
 - bill: 壹仟圓 / 貳仟圓 (1000, 2000 TWD) (2000 is hardly to see)

##### HKD

##### JPY

 - coin: 一円 / 五円 / 十円 (1, 5, 10 yen)
 - coin: 五十円 / 百円 / 五百円 (50, 100, 500 yen)
 - bill: 千円 / 五千円 / 壱万円 (1000, 5000, 10000 yen)
 - bill: 弐千円 (2000 yen, hard to see)

##### RMB / CNY

I am not familiar with CNY 人民幣 bills. 中文數字大寫 is used.

- bill: 壹圓 / 伍圓 / 拾圓 (1, 5, 10 CNY)
- bill: 貳拾圓 / 伍拾圓 / 壹佰圓 (20, 50, 100 CNY)

- There was arguments for 圓 or 元 (CNY/KRW). Once it is legal, I don't care.

## suzhou_numerals.py

Refer to [suzhou numerals](https://en.wikipedia.org/wiki/Suzhou_numerals).

- I saw these characters are used to tell the price of products in HongKong.
- There's an episode in some Sherlock Holmes TV series where these numerals are used. Even you use han characters, these symbols are still mysterious if you never see before.
- suzhou numerals: ```〡〢〣〤〥〦〧〨〩〇〸〹〺```
- these characters are not included in ```Unihan_NumericValues.txt```
- more comments in ```suzhou_numerals.py```
