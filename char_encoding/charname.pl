#!/usr/bin/perl

use Unicode::CharName qw(uname ublock);

$str = "\x{5b57}";
print $str,"\n";


print uname("\x{5AD6}"), "\n";
print ublock(0x5AD6), "\n";
