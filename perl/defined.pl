#!/usr/bin/perl
#
#
# defined vs undef
#
# 2007/03/21 by ericosur

use strict;
use warnings;
use v5.10;

sub test_str($)
{
	my $str = shift;

	if ( defined $str ) {
		say "str = <$str>";
	} else  {
		say "str is undef";
	}
}

sub main()
{
	my $foo;
	my $bar = "bar";

	test_str("");
	test_str($foo);
	test_str($bar);
}

main;

