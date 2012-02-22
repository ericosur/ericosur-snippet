#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

sub main()
{
	my @files = glob("*.jpg *.JPG");


	foreach my $ff (@files)  {
		my $oldfn = $ff;
		my $newfn = lc($ff);
		
		if ($oldfn ne $newfn)  {
			say "rename $oldfn to $newfn";

			# not really rename here
			#rename $oldfn, $newfn;
		}
	}
}

main;

