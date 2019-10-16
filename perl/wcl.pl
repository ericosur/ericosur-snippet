#!/usr/bin/perl
#
# wcl.pl
#
#
# July 17 2002 by ericosur
#   from <stdin>
#   計算有幾行 (包括空白行)
#

use strict;

print STDERR "simulate 'wc -l' behavior, input from stdin\n";

my $line = 0;

while ( <STDIN> )  {
    $line ++;
}

print STDERR "total lines: $line\n";
