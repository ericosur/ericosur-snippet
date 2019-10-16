#!/usr/bin/perl

#
# demo 'require'
#
# 2006/12/27 by ericosur

use warnings;
use strict;
require "gcd.pl";	# run-time load "gcd"

sub show($$$)
{
	my ($a, $b, $g) = @_;
	printf "gcd()#\t%d : %d = %d : %d\n", $a, $b, $a/$g, $b/$g;
}

# gcd.pl
if ( scalar @ARGV ne 2)  {
	print "gcd <value1> <value2>\n";
}
else  {
	my ($a, $b) = @ARGV;
	my $gcd = ericosur::gcd($a, $b);
	show($a, $b, $gcd);
	$gcd = ericosur::gcd2($a, $b);
	show($a, $b, $gcd);
	$gcd = ericosur::gcd_short($a, $b);
	show($a, $b, $gcd);
}

