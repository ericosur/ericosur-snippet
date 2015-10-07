#!/usr/bin/env perl

use strict;

# '09' + '12345678'

sub gen_one()
{
    my $str = sprintf("%08d", int(rand(99999999)));
	return '09' . $str;
}

sub main()
{
	for (1..100) {
		print gen_one() . "\n";
	}
}

main();
