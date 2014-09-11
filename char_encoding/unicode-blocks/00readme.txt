draw_unicode_blocks.pl
======================

This script will read/parse unicode-7.0.0-Blocks.txt.
Output a color map which represents each char block with different
color. Output file name is "map.png". May use

$ convert -resize

to make it larger.

For unicode 7.0.0, the char space is 0x10FFFF (dec 1114112).
There is a huge gap between 0x2F800 to 0xE0000.
I suggest to draw blocks for 248 blocks only.


unicode-7.0.0-Blocks.txt
========================
This data file comes from:
http://www.unicode.org/Public/UNIDATA/Blocks.txt

There are 252 blocks totally.


palette.txt
===========
Data file comes from:
https://gist.github.com/ldvd/5875400#file-pimg-sh-L44

Defines 256 colors in HTML color code.
