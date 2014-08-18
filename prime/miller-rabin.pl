#!/usr/bin/env perl

package ericosur;

use strict;
use warnings;
use Math::BigInt try => "GWP";

my @smallPrimes = ( 2,   3,   5,   7,   11,  13,  17,  19,  23,
                    29,  31,  37,  41,  43,  47,  53,  59,  61,
                    67,  71,  73,  79,  83,  89,  97,  101, 103,
                    107, 109, 113, 127, 131, 137, 139, 149, 151,
                    157, 163, 167, 173, 179, 181, 191, 193, 197,
                    199, 211, 223, 227, 229, 233, 239, 241, 251,
                    257, 263, 269, 271, 277, 281, 283, 293 );

# return 1: pass the precheck, 0: fail the precheck, it's composite
sub precheck($)
{
    my $p = shift;
    for ( @smallPrimes )  {
        return 0 if 0 == $p % $_;
    }
    return 1;
}

sub mr_pass($$)
{
	my ($nn, $aa) = @_;
	my $n1 = $nn - 1;
	my $ss = 0;
	while ( $n1 % 2 == 0 )  {
		$n1 = $n1 >> 1;
		++ $ss;
	}

	my $ap = Math::BigInt->new($aa);
	$ap->bmodpow($n1, $nn);
	return 1 if ($ap->is_one());
	for (1..$ss-1)  {
		return 1 if ($ap == $nn - 1);
		$ap->bmodpow(2, $nn)
	}
	return $ap == $nn - 1;
}


sub miller_rabin($)
{
	my $n = shift;

	return 0 if ( ! precheck($n) );

	for (1 .. 20)  {
		my $aa = 0;
		$aa = int(rand($n)) while ($aa == 0);
		#$aa = $n-1 while ($aa == 0);
		return 0 if ( ! mr_pass($n, $aa) );
	}
	return 1;
}

sub main()
{
	my $lower = 1_000_000_000;
	my $upper = 1_005_000_000;
	my $ofile = "mlr.log";
	my $pc = 0;
	my $ofh;
	my $n = $lower;

	open $ofh, ">", $ofile or die;
	while (1)  {
		if ( miller_rabin($n) )  {
			++ $pc;
			print $ofh $n,"\n";
		}
		++ $n;
		last if ($n > $upper);
	}
	close $ofh;
	print "found $pc primes, and output to $ofile\n";
}

1;
