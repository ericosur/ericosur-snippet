#!/usr/bin/env perl

use strict;
use warnings;

require "miller-rabin.pl";

sub show($$)
{
	my ($p, $q) = @_;
	printf "%d: %s\n", $p, $q?"prime":"composite";
}

for (1 .. 100)  {
	my $vv = int(rand(10000000)) + 1;
	my $rr = ericosur::miller_rabin($vv);
	show($vv, $rr);
}
