#!/usr/bin/perl

# useless ?

use Unicode::String qw(utf8 latin1 utf16);
use utf8;


$a = "abc";

printf "length = %d\n", length($a);

for ($i = 0; $i < length($a); $i++)  {
	printf "%x ", ord(substr($a, $i, 1));
}

print utf8::is_utf8($a) ? "yes" : "no", "\n";
