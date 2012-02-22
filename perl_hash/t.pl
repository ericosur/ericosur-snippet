#!/usr/bin/perl

# problematic
# cannot run???

use Unicode::String qw(ucs4 utf7 utf8 latin1 utf16 ucs2);

#$u = utf8("The Unicode Standard is a fixed-width, uniform ");
#$u .= utf8("encoding scheme for written characters and text");

$u = "\x{fffeb48c}";

# convert to various external formats
printf "uscs4: %s\n", $u->ucs4;      # 4 byte characters
printf "utf16: %s\n", $u->utf16;     # 2 byte characters + surrogates
printf "utf8: %s\n", $u->utf8;      # 1-4 byte characters
printf "utf7: %s\n", $u->utf7;      # 7-bit clean format
printf "latin1: %s\n", $u->latin1;    # lossy
printf "hex: %s\n", $u->hex;       # a hexadecimal string
