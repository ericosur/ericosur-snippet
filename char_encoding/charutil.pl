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

1;
