#!/usr/bin/perl

use strict;
use v5.10;

my $ifile = '1.txt';
my %cmd;

sub read_cmd();
sub dump_cmd($);
sub do_cmd($);

sub read_cmd()
{
	my $ifh;
	open $ifh, $ifile or die;
	# exp: 0 / 32		line: 2156	from 32 to 8
	while ( <$ifh> ) {
		if ( m/\s+line: (\d+)\s+from (\d+) to (\d+)/ ) {
			if ($2 == $3) {
				# skip it if value not change
				next;
			} else {
				my @val = ($2, $3);
				$cmd{$1} = \@val;
			}
		}
	}
	close $ifh;

	#dump_cmd(\%cmd);
}

sub dump_cmd($)
{
	my $rr = shift;

	foreach my $kk ( sort(keys(%$rr)) ) {
		if ( ref $rr->{$kk} eq 'ARRAY' ) {
			print $kk, "->", $rr->{$kk}->[0], " ", $rr->{$kk}->[1], "\n";
		} else {
			print $kk, "->", $rr->{$kk}, "\n";
		}
	}
}

sub do_cmd($)
{
	my $rr = shift;
	my $ln = 0;
	my $pn = 0;

	open my $ifh, "fuck" or die;
	open my $ofh, "> shit" or die;
	while ( <$ifh> ) {
		++ $ln;
		if ( $rr->{$ln} ) {
			print "line: $ln ==> ";
			print "cmd: ", $ln, "->", $rr->{$ln}->[0], " ", $rr->{$ln}->[1], "\n";
			my ($from, $to) = @{ $rr->{$ln} };
			#printf "from(%d),to(%d)", $from, $to;
			s/$from/$to/;
			print $ofh $_;
			++ $pn;
		} else {
			print $ofh $_;
		}
	}
	close $ifh;
	close $ofh;

	print "processed: $pn\n";
}

sub main()
{
	read_cmd();
	do_cmd(\%cmd);
}

main;
