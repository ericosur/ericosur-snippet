#!/usr/bin/env perl

use strict;
use Data::Dump qw(dump);

my $str = qq(pack my box with five dozen liquor jugs);
my %h = ();
foreach (split //,$str)  {
	$h{$_} ++;
}

for ('a' .. 'z')  {
	unless ( $h{$_} )  {
		print $_, " missed\n";
	}
}

dump(%h);
