#!/usr/bin/perl

# perl ghtm.pl <infile> [outfile] [-type]
# eg: perl ghtm.pl utf.txt out.html -utf8
#
# 2006/12/27 by ericosur

my $infile;
my $outfile = "out.html";
my $type = "utf-8";

foreach (@ARGV)  {
	if ( /^-(.+)/ )  {
		$type = $1;
	}
	elsif ( $infile eq "" )  {
		$infile = $_;
	}
	else {
		$outfile = $_;
	}
}

printf "type is [%s]\ninput from [%s], output to [%s]\n",
	$type, $infile, $outfile;

open INFH, "< $infile" or die "cannot open $!\n";
open OUTFH, "> $outfile" or die "cannot open $!\n";

my $embeddedfile;
while (<INFH>)  {
	$embeddedfile = $embeddedfile . $_;
}

close INFH;

my $out =<<MYEOF;
<html>
<head>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=$type">
<title>Rasmus Test Page</title>
</head>
$embeddedfile
</html>
MYEOF

print OUTFH $out;
close OUTFH;
