#!/usr/bin/env perl

use strict;
use utf8;

binmode(STDIN, ':encoding(utf8)');
binmode(STDOUT, ':encoding(utf8)');
binmode(STDERR, ':encoding(utf8)');

# refer to:
# https://www.perl.com/pub/2012/04/perlunicook-unicode-literals-by-number.html/
print("\x{1f99e}\n");
print('-' x 40, "\n");
while (<DATA>) {
    print;
}
__DATA__
❤️
🇧🇴
🙋‍♀️
🏈
😃
