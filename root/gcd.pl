#!/usr/bin/perl
# gcd.pl
# provides gcd(), gcd2()
# use call_gcd.pl to call these functions
#
# 2005/06/08 reviewed by ericosur

package ericosur;

use warnings;
use strict;

sub gcd($$);
sub gcd2($$);

1;

# gcd: greatest common divisor
sub gcd($$)
{
	my ($a, $b) = @_;
	my $t = 0;

	return 1 if (0 >= $a || 0 >= $b);

	while ($a != 0)  {
		$t = $b % $a;
		$b = $a;
		$a = $t;
	}

	return $b;
}

# gcd2: recursive method
sub gcd2($$)
{
	my ($a, $b) = @_;

	if ( $b eq 0 )  {
		return $a;
	}
	else {
		return gcd2($b, $a % $b);
	}
}

# Shamelessy stolen from [MrNobo1024]'s node: [id://56906]
sub gcd_short($$)
{
    my($x,$y)=@_;
    ($x,$y)=($y,$x%$y) while $y;
    return $x;
}

