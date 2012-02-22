#!/usr/bin/env perl

# a simple stupid fib recursive function in perl

use strict;
use warnings;
use 5.010;
use Data::Dump qw(dump);

sub fib($);

sub fib($)
{
	my $n = shift;
	if ($n <= 2)  {
		return 1;
	}
	else  {
		return fib($n-1) + fib($n-2);
	}
}

my @arr = ();
my $upper = 12;
for (1 .. $upper)  {
	push @arr, fib($_);
}
dump(@arr);

