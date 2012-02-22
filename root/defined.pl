#!/usr/bin/perl
#
#
# defined vs undef
#
# 2007/03/21 by ericosur

use strict;
use warnings;


sub test_func($)
{
	my $str = shift;

	if ( defined $str ) {
		print "str = $str\n";
	} else  {
		print "str is undef\n";
	}
}

my $foo;
my $bar = "bar";

test_func($foo);
test_func($bar);

