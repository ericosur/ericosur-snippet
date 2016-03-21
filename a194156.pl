#!/usr/bin/env perl

# OEIS A194156
# a(4) .. a(15)
# 13,23,47,113,199,283,467,887,1627,2803,4297,6397

use strict;

my @oeis = (13,23,47,113,199,283,467,887,1627,2803,4297,6397);
my %val = ();
my $min = 13;
my $max = 65535;

sub count($)
{
	my $seed = shift;
	print $seed,"...\n";

	if ($seed < $min) {
		return;
	}
	my $nn = $seed;
	while ($nn < $max) {
		if ($val{$nn}) {
			;
		} else {
			$val{$nn} = 1;
		}
		$nn += $seed;
	}
}

sub main()
{
	foreach my $v (@oeis) {
		count($v);
	}
	my @kk = keys(%val);
	my $size = scalar(@kk);
	print $size, "\n";
}

main;

=cut
# output to file
	my $f = "a194156.txt";
	open my $fh, "> $f" or die;
	foreach my $v (sort { $a <=> $b } keys(%val)) {
		print $fh $v,"\n";
	}
	close $fh;

=pod
