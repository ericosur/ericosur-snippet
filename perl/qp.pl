#!/usr/bin/perl

#@ qp.pl
#@ translate plain text into quoted print format
#@
#@ usage: qp.pl <infile> <outfile>
#@
#@ Oct 11 2004 by ericosur

use strict;
use MIME::QuotedPrint;

sub main()
{
	my $infile;
	my $outfile;

	($infile, $outfile) = @ARGV;
	die "$0 <infile> <outfile>\n" unless ($infile && $outfile);

	printf "infile = [%s], outfile = [%s]\n", $infile, $outfile;

	open my $inf, "< $infile" or die "open error\n";
	open my $otf, "> $outfile" or die "write error\n";

	while (<$inf>)
	{
		my $tmp = encode_qp($_);
		print $otf "$tmp";
	}

	close $inf;
	close $otf;
}

main;

