# README

If you want to update emoji related data, just see section about **UPDATE**.

This README describes how to translate emoji icons into unicode sequence for maximum compatability without losing any code. Normally using utf-8 encoding could keep most of information and ok to exchange. But emoji are not always perfectly editable in the editor. Currently I suggest that use **unicode escape sequence** to represent unicode characters.

## UPDATE

- May check the latest release tag from <https://github.com/unicode-org/cldr.git>

- and then run this script ```./runme.sh```

### relation between scripts and data files

- ```read_enxml.py``` vs ```wtf.csv```
- ```parse_enxml.py``` vs
  - en_emoji.py
  - zh_emoji.py

## basics

For example the test string ```❤️🇧🇴🙋‍♀️🏈😃```

For newer version of ubuntu and text editors. This string token could be displayed and edited correctly. You need up-to-date emoji font and text rendering system.

### scripts

Run ```u8u16.py ❤️```, you will get:

```text
         input: ❤️
unicode-escape: \u2764\ufe0f
      utf16-be: \u2764\ufe0f
       to_utf8: e29da4efb88f
```

Run ```u8u16.py 😃```, will get:

```text
         input: 😃
unicode-escape: \U0001f603
      utf16-be: \ud83d\ude03
       to_utf8: f09f9883
```

### json & qml

json and qml using javascript sytle string literals, so using utf16-be would be good.

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

- CLDR

  - table for all [CLDR Releases/Downloads](http://cldr.unicode.org/index/downloads)

  - specify release file to download (manually), look for file like: [CLDR common](http://unicode.org/Public/cldr/37/cldr-common-37.0.zip)

- emoji data files

  - 2023-08-30 [emoji 15.1](https://unicode.org/Public/emoji/15.1/)
    - ReadMe.txt
    - emoji-sequences.txt
    - emoji-test.txt
    - emoji-zwj-sequences.txt

    - [emoji 15.0](https://unicode.org/Public/emoji/15.0/)
      - ReadMe.txt
      - emoji-sequences.txt
      - emoji-test.txt
      - emoji-zwj-sequences.txt

    - [emoji 13.1](https://unicode.org/Public/emoji/13.1/)
      - ReadMe.txt
      - emoji-sequences.txt
      - emoji-test.txt
      - emoji-zwj-sequences.txt

## history

- 2021-11-09
  - [CLDR40](http://unicode.org/Public/cldr/40/)
