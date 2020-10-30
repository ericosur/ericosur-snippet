#!/usr/bin/env perl

use strict;
use utf8;

binmode(STDIN, ':encoding(utf8)');
binmode(STDOUT, ':encoding(utf8)');
binmode(STDERR, ':encoding(utf8)');


# refer to:
# https://www.perl.com/pub/2012/04/perlunicook-unicode-literals-by-number.html/
print("Lobster (U+1F99E): \x{1f99e}\n");
print("Cockroach (U+1FAB3): \x{1fab3}\n");

print('-' x 40, "\n");
print("read from __DATA__ =====>\n");
while (<DATA>) {
    print;
}

# reference: https://emojipedia.org/emoji-13.0/

__DATA__
❤️
🇧🇴
🙋‍♀️
🏈
😃
🪲
🐛
🦗
🐞
🦟
🕷️
