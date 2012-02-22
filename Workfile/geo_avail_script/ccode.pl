#!/usr/bin/perl

use strict;
use 5.010;

sub read_iso3166()
{
	my $ff = 'iso-3166-2.txt';
	my %ccode = ();

	open my $fh, $ff or die;
	while (<$fh>) {
		next if /^$/;
		next if /^#/;
		if (m/^(..)\t(\w+)\s+/)  {
			my $two = $1;
			my $full = $2;
			print("($full) => ($two)\n");
		}
	}
	close $fh;
}

