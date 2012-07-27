#!/usr/bin/env perl

use strict;
use v5.10;

my $home = $ENV{'HOME'};
my $file = $home . "/Dropbox/Private/Pegatron.txt";
my $pat = qr(([a-fA-F0-9]{2}[:-]){5});

open my $fh, $file or die;

my $ln = 0;
while (<$fh>)  {
	$ln ++;
	if (m/$pat/)  {
		s/[\r\n]//;
		say "$ln: $_";
	}
}


close $fh;

