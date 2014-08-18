#!/usr/bin/perl
#
# 2006/12/27 by ericosur
# 2008/01/27 edited by ericosur
#

#
# print the random numbers
#
# tags: const constant random rand

use strict;
use warnings;


use constant NUMBER_RANDOM => 15;
use constant UPPER_LIMIT_RANDOM => 100;

my @array;
my $str;

for (1..NUMBER_RANDOM)  {
	my $ch = int(rand(UPPER_LIMIT_RANDOM));
	push @array, $ch;
}

$str = join ', ', @array;
print $str,"\n";
