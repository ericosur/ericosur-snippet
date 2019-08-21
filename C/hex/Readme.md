# readme

convert LATIN1 (ISO8859-1 subset) to UTF-8 encoding by myself

## how to use

at main.cpp

```cpp
    char str[STRING_LEN] = "C0c1C7cBD3d7DA";
```

assign a string which represents a hex byte array, in the sample,
it would be

```
C0 C1 C7 CB D3 D7 DA
```

and calling _**_iso88591_to_utf8()_**_ to translate iso8859-1 to utf-8
you need to prepare buffer before calling it

## new: add a validate function

add calling function _**_g_utf8_validate()_**_ from glib-2.0 to validate
translated utf-8 string is ok

