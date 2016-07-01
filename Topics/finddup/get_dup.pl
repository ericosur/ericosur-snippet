#!/usr/bin/perl

#use diagnostics;
use strict;
use warnings;
use Getopt::Long;

my $ifile = "md5.txt";

sub main()
{
	my %dups = ();
	my ($digest, $filename, $verbose) = ();
	GetOptions("verbose" => \$verbose);

	print STDERR "input file: $ifile\n";
	print STDERR "verbose: $verbose\n" if $verbose;

	open my $fh, $ifile or die;

	my $total = 0;
	my $count = 0;

	$_ = <$fh>;			# read the first line
	if (m/^# file count = (\d+)/)  {
		$total = $1;
		print STDERR "total = $total\n";
	}
  LINE:
	while (<$fh>)  {
		chomp;
		next LINE if m/^#/;
		next LINE if m/^$/;
		++ $count;
		my ($digest, $filename) = /(.{32})\s+(.*)/;
		#print $filename, "\n";
		push(@{$dups{$digest}}, "\n");
		push(@{$dups{$digest}}, $filename);
		printf STDERR "progress: %02d\r", int($count * 100 / $total);
	}
	print STDERR "\n";

	close $fh;

	foreach $digest (sort keys %dups) {
		if (scalar(@{$dups{$digest}}) > 2) {
			print "$digest" if ($verbose);
			print @{$dups{$digest}}, "\n";
			print "\n" if ($verbose);
		}
	}
}

main;
