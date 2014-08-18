#!/usr/bin/perl

use strict;
use v5.10;

my $file = 'patch-ec.txt';

sub do_patch($$)
{
	my $f = shift;
	my $l = shift;

	my $fpath = "res/" . $f;
	my $opath = "res/" . $f . ".new";
	my $bpath = "res/" . $f . ".bak";
	if (-e $fpath) {
		say "ok";
		open my $ifh,$fpath or die;
		open my $ofh,"> $opath" or die;
		while ( <$ifh> ) {
			if ( m/<\/resources>/ ) {
				print $ofh "    ",$l,"\n";
				print $ofh "</resources>\n";
			} else {
				print $ofh $_;
			}
		}
		close $ifh;
		close $ofh;	
		rename $fpath, $bpath;
		rename $opath, $fpath;
	} else {
		say "not found: $fpath";
	}
}

sub main()
{
	my $cnt = 0;
	open my $fh, $file or die;
	while (<$fh>) {

		if (m/^([^:]+):\d+:\s+(.*)$/) {
			my $f = $1;
			my $l = $2;
			
#			say "file: $f";
#			say "line: $l";
			do_patch($f, $l);
			++$cnt;
		}

	}

	close $fh;
}

main;

