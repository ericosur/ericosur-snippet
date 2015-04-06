#!/usr/bin/env perl

use strict;

my %all = ();

sub combine_words($)
{
	my $iff = shift;

	open my $ifh, $iff or die;
	while (<$ifh>) {
		s/[\r\n]//;
		$all{$_} ++;
	}
	close($ifh);
}

sub main()
{
    my @ar = glob("extracted*.txt");
    my $ofile = "combined.txt";

    foreach my $ff (@ar) {
        combine_words($ff);
    }

    open my $ofh, ">$ofile" or die;
    for my $wd (sort keys(%all)) {
    	print $ofh $wd,"\n";
    }
    close($ofh);
}

main;
