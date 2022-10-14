# readme

[TOC]

This readme describes how to translate emoji icons into unicode sequence for
maximum compatability without losing any code. Normally using utf-8 encoding
could keep most of information and ok to exchange. But emoji are not always
perfectly editable in the editor. Currently I suggest that use **unicode
escape sequence** to represent unicode characters.

## basics

### flow

for example I got a test string:
```
❤️🇧🇴🙋‍♀️🏈😃
```

Such string could be safely displayed and edited with **sublime text 3**
in ubuntu 18.04. But it is not properly displayed nor edited at windows and
ubuntu 16.04.
UPDATE: with proper emoji fonts and later version of **sublime text 3**, it
could be shown as B/W color.

To avoid losing information, transfrom such string into unicode sequence could be a safe way to keep such string.

```
$ ./u8u16.py ❤️
❤️
unicode-escape: \u2764\ufe0f
      utf16-be: \u2764\ufe0f
utf-8: e29da4efb88f

$ ./u8u16.py 😃
😃
unicode-escape: \U0001f603
      utf16-be: \ud83d\ude03
utf-8: f09f9883
```

### json or qml

json and qml using javascript sytle string literals, so using utf16-be would be
good.

```json
{
    "smile": "\ud83d\ude03"
}
```

```qml
    readonly property string smile: "\ud83d\ude03"
```

### c++11

for c++11, using unicode escape sequence by ```\u``` and ```\U``` like python3

```c++
void unicode_char()
{
    using namespace std;
    string str =
        "\u2764\ufe0f"
        "\U0001f1e7\U0001f1f4"
        "\U0001f64b\u200d\u2640\ufe0f"
        "\U0001f3c8\U0001f603";
    cout << str << endl;
}
```

### howto

> utf-16 surrogate characters ranges from U+D800 to U+DFFF

- script **surgg.py** demos how to translate utf-16 characters to a string
- may put it into a json file, and use **jq** to view

## unicode definition data files

* CLDR

    * table for all [CLDR Releases/Downloads](http://cldr.unicode.org/index/downloads)

    * specify release file to download (manually), look for file like: [CLDR common](http://unicode.org/Public/cldr/37/cldr-common-37.0.zip)

* emoji data files

    * [emoji 13.1](https://unicode.org/Public/emoji/13.1/)
        - ReadMe.txt
        - emoji-sequences.txt
        - emoji-test.txt
        - emoji-zwj-sequences.txt

    * [emoji ucd 13.0.0](https://unicode.org/Public/13.0.0/ucd/emoji/)
        - emoji-data.txt
        - emoji-variation-sequences.txt

### 2021-11-09

http://unicode.org/Public/cldr/40/


### auto download and do the rest

execute mkcldrtable.sh and do all the rest
```
$ ./mkcldrtable.sh
```

replace the __output.csv__ to __emoji.csv__

