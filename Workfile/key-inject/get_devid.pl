#!/usr/bin/perl

# parse original XML style widevine keybox to to DeviceID field

use strict;
use v5.10;

# turn to 1 to see all id
my $verbose = 0;

# default input file
my $ifile = "test.keybox";

# default output file
my $ofile = "out-device_id.txt";


sub parse_file($)
{
	my $inf = shift;
	my ($first_id, $last_id);

	say "input from: ", $inf;
	say "output  to: ", $ofile;

	open my $ofh, ">$ofile" or die;
	open my $fh, $inf or die;
	while (<$fh>) {
		if ( m/<Keybox DeviceID=\"([^\"]+)\">/ ) {
			my $id = $1;
			print $id,"\n" if $verbose;
			print $ofh $id, "\n";
			if (!$first_id) {
				$first_id = $id;
			}
			$last_id = $id;
		}
	}
	close $fh;
	close $ofh;

	say "first: ", $first_id, " len: ", length($first_id);
	say " last: ", $last_id, " len: ", length($last_id);
}

sub main()
{
	my $iff = $ARGV[0] // $ifile;
	parse_file($iff);
}

main;
