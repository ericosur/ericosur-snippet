#!/usr/bin/env perl

use strict;
use warnings;
use 5.010;
use Perl6::Junction qw(any none all one);
use Data::Dump qw(dump);

my @first = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144);
my @second = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37);

say "\@first";
dump(@first);
say "\@second";
dump(@second);

if (any(@first) == any(@second))  {
	say "yes, some elements is equal";
}

if (all(@first) > 0)  {
	say "yes, all element is bigger than 0";
}

if (none(@second) > 40)  {
	say "yes, none is bigger than 40";
}

if ( one(@first) > 100 )  {
	say "yes, only one is bigger than 100";
}

