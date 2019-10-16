#!/usr/bin/perl

use strict;

my ($sec, $km) = ();

while (<DATA>) {
	if (m/(\d+) (\d+\.\d+)/) {
		($sec, $km) = ($1, $2);
		#printf("%d %f\n", $sec, $km);
		printf("speed: %f\n", $km / ($sec / 3600));
	}
}

__DATA__
sec km
137 3.7
348	8.4

317	8.4
143	3.6

127 3.7
337 8.4

314 8.4
141 3.6
