#!/usr/bin/env perl

# in combined.txt (as a rough dictionary)
# search [a-fo]{4}
# o will be replace by 0
#

use strict;

sub main()
{
	my $file = "combined.txt";
	my $cnt = 0;
	open my $fh, $file or die;
	while (<$fh>) {
		if ( m/^[a-fo]{4}$/ ) {
		    $cnt++;
			s/o/0/g;
			print;
		}
	}
	print "cnt: ", $cnt, "\n";
}

main;
