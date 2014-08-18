#!/usr/bin/perl
#
# extract big5 items from:
# http://www.unicode.org/Public/UNIDATA/Unihan.zip
#
# nonsense script, use ''grep kGB?'' to extract

use strict;
use warnings;

#use utf8;

my $search_tag = 'kGB0';
my $ifile = q(Unihan.txt);
my $ofile = q(extract_gb0.txt);

#
# input the gb0 code
#
sub write_char($)
{
	my $in = shift;
	my $rr;

	my ($hh, $ll) = ( $in =~ m/(..)(..)/ );
	$hh += 0xa0;
	$ll += 0xa0;

	$rr = sprintf "0x%02x%02x", $hh, $ll;
	return $rr;
}


my $ifh;
my $ofh;

open $ifh, "<:utf8", $ifile or die;
open $ofh, ">", $ofile or die;

binmode $ofh;
binmode STDERR;

my $found = 0;
my $total = 0;

while (<$ifh>)  {
	next if ( m/^#/ or m/^$/ );
	++ $total;
	s/\n//;
	#last if $total > 500000;
	#print STDERR;
	if ( m/(.*)\t($search_tag)\t(.*)/ )  {
		++ $found;

		my ($a, $b, $c) = ($1, $2, $3);
		print $ofh $1, "\t", $3, "\t";
		print $ofh write_char($3),"\n";
	}
	print STDERR "$found / $total\r";
}

close $ifh;
close $ofh;

print STDERR "\n";
print STDERR "total = $found\n";
