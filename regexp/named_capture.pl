#!/usr/bin/perl

use strict;
use warnings;

# to demo named captures of perl 5.10
# reference from http://perltraining.com.au/tips/2009-04-30.html

my $name = qr/
				(?<varname>\w+)	# captured token would be named ''varname''
			/x;
my $sep = qr/[\/:]/;
my $value = qr/
				(
					?<val>	# named captured token
					\d+$sep\d+$sep\d+
				)
			/x;

while (<DATA>)  {
	if ( /$name=$value/ )  {
		printf("<%s> => <%s>\n", $-{varname}[0], $-{val}[0]);
	}
}

__DATA__
date=2009/05/04
time=14:30:00
