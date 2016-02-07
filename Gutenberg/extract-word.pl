#!/usr/bin/env perl

use strict;

sub parse_file($)
{
	my $file = shift;
	my $ofile = $file;
	my %dict = ();
	my $debug = 0;

	$ofile =~ s/nobomb/extracted/;

	open my $fh, $file or die;
	while (<$fh>) {
	    s/[\$=_#@~%!&*()\[\];.,:?^`\\\/\"\+0-9]+/ /g;
		s/(\w+)(--)?/$1/; # TODO: here -- not removed correct
	    my @ar = split(/\s+/);
		foreach my $wd (@ar) {
			if ($debug) {
				if ($wd =~ m/^yo*/) {
					printf("<%s>\n", $wd);
				}
			}
			$wd = lc($wd);
			$wd =~ s/--//;
			$wd =~ s/^\'//;	# remove single ' at beginning of word
			$wd =~ s/\'$//; # remove signle ' at end of word
		    if ( length($wd) ) {
				$dict{$wd} ++;
			}
		}
	}
	close($fh);

	open my $ofh, "> $ofile" or die;
	foreach my $kk (sort keys(%dict)) {
		if ( length($kk) ) {
			if ($debug && $kk =~ m/^yo/ ) {
				print $ofh $kk,"\n";
			} else {
				print $ofh $kk,"\n";
			}
		}
	}
	close($ofh);
}

sub main()
{
	my @far = glob("nobomb*.txt");
	foreach my $ff (@far) {
		parse_file($ff);
	}
}

main;
