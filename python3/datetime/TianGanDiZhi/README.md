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

## quick demo (Makefile)

This folder provides a Makefile to run common demos quickly.

```bash
make help
```

Default demo (includes both examples):

```bash
make demo
```

### 2-1. Query year to 天干/地支

Example: year 2030

```bash
make year Y=2030
```

Equivalent direct command:

```bash
python ganzhi.py 2030
```

### 2-2. Query 天干/地支 to possible years

Use numeric index pair (A, B):

- A is 天干 index, range 0..9
- B is 地支 index, range 0..11
- A+B must be even

Example: A=1 (乙), B=3 (卯)

```bash
make ab A=1 B=3
```

Equivalent direct command:

```bash
python ganzhi.py -a 1 -b 3
```

Other useful targets:

- ```make list``` to list all 天干/地支/生肖
- ```make tests``` to run unit tests
- ```make lint``` to run Ruff checks in this folder

## tests

- ```test_gngan_yaljux.py``` contains unit tests for core behavior in ```gngan_yaljux.py```.
- It covers:
  - year normalization and invalid input handling
  - GanChi reminder/mapping for known values
  - validation rule of ```check_ab()```
  - cycle shape and output constraints of ```brute_force_try()```

Run tests from this folder:

```bash
python -m unittest -v test_gngan_yaljux.py
```

Or from workspace root:

```bash
python -m unittest -v datetime/TianGanDiZhi/test_gngan_yaljux.py
```

## logging callback convention

To avoid name collisions with functions like ```numpy.log``` or ```math.log```,
logger callback parameters in this folder use the name ```_logd```.

Examples:

- ```GanChi(_logd=...)```
- ```do_values(..., _logd=...)```
- ```do_ab(..., _logd=...)```
- ```do_tests(_logd=...)```
