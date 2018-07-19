# readme for loading bitmap from eten font files

```
$ echo "中" | iconv -f UTF-8 -t BIG5 |hexdump -C
00000000  a4 a4 0a                                          |...|
```

## what is inside

stdfont.24b has 942768 bytes
per to rule, there are
```
5401 + 7652 + 41 = 13094
```
characters in this file,
```
942768 / 13094 = 72
```
every character occupys 72 bytes for 24x24 font.

so each pixel use 1bit,
```
(72 * 8) / (24 * 24) = 1
```

## rule

```
/*

  stdfont.24? │標準字型│ 常用字 │A440-C67E │5401│
  (hanstd.24) │        │次常用字│C940-F9D5 │7652│
              │        │ 倚天字 │F9D6-F9FE │  41│

  spcfont.24  │特殊符號│ 標準字 │A140-A3BF │ 408│
  (han-gr.24) │        │ 控制字 │A3C0-A3E0 │  33│<- 保留 │ │ 可造字 │a3e1-a3fe │ 30│<- 保留 spcfsupp.24 │特殊字型│ │c6a1-c8fe │ 365│408 max (han-gr1.24)│ │ │ │*318│han's 24 ascfont.24 │ ascii │ │ │ 256│ (han-asc.24)│ │ │ │ │
*/

/* fontinfo 的傳回值 */
#define font_asc 1 // 內碼屬 ascii 範圍
#define font_std 2 // 內碼屬標準字型範圍
#define font_spc 3 // 內碼屬特殊符號範圍
#define font_spcf 4 // 內碼屬特殊字型範圍

  unsigned char FontInfo(unsigned char hb,unsigned char lb,long &location)
  {
    int hadd,ladd;
    unsigned int big5;

    big5=lb+(hb<<8);
    if ( big5>=0xa140 && big5<=0xa3bf ) //spcfont.* 特殊符號 a140-a3bf,408
    {
        hadd="(hb-161)*157;"
        ladd="(lb<127)?(lb-64):(lb-161+63);"
        location="hadd+ladd;"
        return(font_spc);
    }
    else if ( big5>=0xc6a1 && big5<=0xc8d3 ) //spcfsupp.*
    {
        hadd="(hb-198)*157-63;"
        ladd="(lb<127)?(lb-64):(lb-161+63);"
        location="hadd+ladd;"
        return(font_spcf);
    }
    else if ( ( lb<="0x7e&&lb">=0x40 || lb<=0xfe&&lb>=0xa1 )&&( big5>=0xa440 &&\
           big5<=0xc67e || big5<="0xf9fe" && big5>=0xc940 ))
    {
        hadd=(hb-164)*157;                    // Standard Words , 13094
        ladd=(lb<127)?(lb-64):(lb-161+63);
        location="hadd+ladd;"
        if(big5>=0xc940)
            location-=408;
        return(Font_STD);
    }
    else           // Normal ACSII Codes
    {
      location=hb;
      return(Font_ASC);
    }
  }
```

## todo

* given CJK utf-8 characters and show bitmap font (only characters in BIG-5 range)
* read BIG5 text file and show bitmap, not one by one, all in one bitmap
* collect needed bitmap font from text file
* support spcfont and ascfont
* show all characters in one bitmap (or partial)

