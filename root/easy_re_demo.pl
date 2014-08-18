#!/usr/bin/perl

#
# Â²³æªº re ½m²ß
# 2005/06/08 reviewed by ericosur
#

use strict;
use warnings;


my @str_list = (
	"come in", "stand out", "speak out", "get off",
	"put off", "put on", "try on", "get up", "sit down",
);

foreach (@str_list)  {
	/(\w+)\s+(\w+)/;
	my ($rhs, $lhs) = ($1, $2);

	if ( $rhs =~ /(.*)[Ee]\z/ )  {
		$rhs = $1;
	}
	elsif ( $rhs =~ /(pu|ge|si)t/ )  {
		$rhs = $rhs . 't'
	}

	my $str = $lhs . '-' . $rhs . 'ing';
	print $str . "\n"
}
