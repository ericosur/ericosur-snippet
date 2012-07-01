#!/usr/bin/perl

use strict;
use warnings;
use v5.10;
use Perl6::Junction qw(all any none one);
use Data::Dump qw(dump);

my @arr = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89);

if (any(@arr) >= 5) {
	my @rr = grep {$_ % 5 == 0} @arr;
	dump(@rr);
}

if (all(@arr) > 0)  {
	say "ok";
}

