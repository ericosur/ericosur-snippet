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
	my $a = shift;
	my $b = shift;
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
	my $a = shift;
	my $b = shift;

	if ( $b eq 0 )  {
		return $a;
	}
	else {
		return gcd2($b, $a % $b);
	}
}
