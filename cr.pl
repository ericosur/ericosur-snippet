#!/usr/bin/env perl

use strict;

my @ar = glob("*.png");
my $cmd;
foreach my $f (@ar) {
	s/[\r\n]//;
	$cmd = sprintf("pngcrush -reduce -brute %s out/%s", $f, $f);
	print $cmd,"\n";
	system $cmd;
}
