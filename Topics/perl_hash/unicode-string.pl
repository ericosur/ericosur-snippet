#!/usr/bin/perl

use strict;
use warnings;
use v5.10;
use Unicode::String;

# http://search.cpan.org/~gaas/Unicode-String-2.09/String.pm

my $us = Unicode::String->new("中文輸入法");
say "utf8: ", $us->utf8();
say "ucs4: ", $us->ucs4();
say "utf7: ", $us->utf7();
say "utf16: ", $us->utf16();
say "latin: ", $us->latin1();
say "hex: ", $us->hex();


