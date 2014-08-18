#!/usr/bin/perl
#
#
package charutil;

use strict;
use warnings;

#
# input the double byte of char
#
sub write_char($)
{
	my $in = shift;

	my ($hh, $ll) = ( $in =~ m/(..)(..)/ );

	return chr(hex($hh)) . chr(hex($ll));
}


#
# input the gb0 code
#
sub write_hex($)
{
	my $in = shift;
	my $rr;

	my ($hh, $ll) = ( $in =~ m/(..)(..)/ );
	$hh += 0xa0;
	$ll += 0xa0;

	$rr = sprintf "0x%02x%02x", $hh, $ll;
	return $rr;
}

1;
