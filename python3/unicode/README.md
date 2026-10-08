# Unicode Notes

`apple_logo.py` was removed because its Apple logo example used U+F8FF, a code point in the Unicode Private Use Area (U+E000..U+F8FF). The Unicode Standard does not assign private-use code points a meaning; interpretation depends on private agreements and supporting fonts, so U+F8FF is not a standardized Apple logo character.

Source: [Unicode Consortium, Private-Use Characters FAQ](https://www.unicode.org/faq/private_use.html)
