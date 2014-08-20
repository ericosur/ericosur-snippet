#!/usr/bin/perl

# make a file list
# count all .ext
# to know each number of each .ext

use strict;
use warnings;

sub main()
{
	my $iff = "fl.txt";
    my $cmd = "find -type f > $iff";
	my $cnt = 0;
	my %hh = ();

	system $cmd;

	open my $fh, $iff or die;
    while (<$fh>) {
        if ( m/\.(\w+)$/ ) {
			my $ext = lc($1);
			$hh{$ext} ++;
		}
		$cnt ++;
	}
    close $fh;
    print "line_cnt: $cnt\n";

    foreach my $kk (sort(keys(%hh))) {
		printf("%s,%d\n", $kk, $hh{$kk});
	}

    unlink $iff;
}

main;

