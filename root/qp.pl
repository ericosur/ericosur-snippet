#!/usr/bin/perl

#@ qp.pl
#@ translate plain text into quoted print format
#@
#@ usage: qp.pl <infile> <outfile>
#@
#@ Oct 11 2004 by ericosur

use MIME::QuotedPrint;

my $infile;
my $outfile;

($infile, $outfile) = @ARGV;
die "$0 <infile> <outfile>\n" unless ($infile && $outfile);

printf "infile = [%s], outfile = [%s]\n", $infile, $outfile;

open INFILE, "< $infile" or die "open error\n";
open OUTFILE, "> $outfile" or die "write error\n";

while (<INFILE>)
{
	my $tmp = encode_qp($_);
	print OUTFILE "$tmp";
}

close INFILE;
close OUTFILE;

