# README

Some scripts work with 天干地支 (tiān gān dì zhī)

## list

天干地支 There are 60 combinations.
NOTE: not all combination is available/valid. For example, if this year is 甲子, and the next would 乙丑, and 丙寅 and so on.
Not possible to see 甲丑.

Here we could split (天干) 甲乙丙丁戊己庚辛壬癸 into two groups, by odd/even order. First group is 甲丙戊庚壬. 2nd group is 乙丁己辛癸.
Same, split (地支) 子丑寅卯辰巳午未申酉戌亥 into two groups. First group is 子寅辰午申戌, and the second group is 丑卯巳未酉亥.

Only the first (天干) group maps to the frist (地支) group, and
only the 2nd (天干) group maps to the 2nd (地支) group.

| no |group 天干  |group 地支  | combination |
|---|-----------|------------|--------------|
|1st| 甲丙戊庚壬  | 子寅辰午申戌 | 5C1 x 6C1 = 30 |
|2nd| 乙丁己辛癸  | 丑卯巳未酉亥 | 5C1 x 6C1 = 30 |


Here are the all possible combinations (30+30=60). **Not** 10C1 x 12C1 = 120.

```
甲子  乙丑  丙寅  丁卯  戊辰  己巳  庚午  辛未  壬申  癸酉  甲戌  乙亥
丙子  丁丑  戊寅  己卯  庚辰  辛巳  壬午  癸未  甲申  乙酉  丙戌  丁亥
戊子  己丑  庚寅  辛卯  壬辰  癸巳  甲午  乙未  丙申  丁酉  戊戌  己亥
庚子  辛丑  壬寅  癸卯  甲辰  乙巳  丙午  丁未  戊申  己酉  庚戌  辛亥
壬子  癸丑  甲寅  乙卯  丙辰  丁巳  戊午  己未  庚申  辛酉  壬戌  癸亥
```

```json
{
  "天干": ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"],
  "地支": ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"],
  "生肖": ["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]
}
```

"地支" and "生肖" is if-and-only-if one-on-one relationship.

## scripts

- ```gngan_yaljux.py``` provides _*_class GanChi_*_ and some utility functions. It uses **typer** to do some self-test/demo.
- ```typer_gng.py``` uses **typer** to list TianGanDiZhi. Use **--help** to check the details.
- ```ganzhi.py``` uses **argparse** to list TianGanDiZhi. Use **--help** to check the details.
