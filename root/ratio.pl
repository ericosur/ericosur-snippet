#!/usr/bin/perl

# use 'exif' to obtain the EXIF info from JPG files
# and get the resolution of picture
# try to get 3:2, 4:3 ratio
# Jan 18 2005 by ericosur
#
# Jun 9 2005 reviewed by ericosur

# main procedure
use strict;
use warnings;

require "gcd.pl";

sub get_exif($);
sub parse_exif($);
sub get_aparture_exposure($);

my @files;

if (@ARGV)  {
	@files = @ARGV;
}
else {
	@files = glob("*.jpg");
	#@files = ('IMG_5391.JPG' );
}

foreach (@files)  {
	my $res = get_exif($_);

	print "$_:\n";	# filename

	parse_exif($res);
	get_aparture_exposure($res);
}

#
# functions
#
sub get_exif($)
{
	my $cmd = shift;

	$cmd = 'exif ' . $cmd;
	my $result = `$cmd`;

	return $result;
}


sub parse_exif($)
{
	my $res = shift;
	my $X = 0;
	my $Y = 0;

	my @lines = split /\n/, $res;
	#my $cnt = 0;
	foreach (@lines)  {
		#$cnt ++;
		# match: PixelXDimension  |3072
		if ( /^Pixel([X|Y])Dimension\s+\|(\d+)/ )  {
			#print "($cnt)($1)__($2)\n";
			my $assign = "\$$1 = $2";	# $[X|Y] = nnnn
			#print "\t$assign\n";
			eval($assign);
		}
	}
	#print "cnt = $cnt\n";
	#print "($X, $Y)\n";
	if ($X * $Y == 0)  {
		print "incorrect exif data\n";
	}
	else  {
		# swap
		#if ($X < $Y)  {
		#	my $tmp = $X;	$X = $Y;	$Y = $tmp;
		#}
		# get the ratio
		my $gcd = Rasmus::gcd($X, $Y);
		printf "\t%dx%d (%d:%d)\n",
			$X, $Y, $X/$gcd, $Y/$gcd;
	}
}


# parse Tv, Av, Model from EXIF result
sub get_aparture_exposure($)
{
	my $res = shift;
	my @lines = split /\n/, $res;

#Exposure Time       |1/100 sec.
#FNumber             |f/7.1

	foreach (@lines)  {
		if ( /Model\s+\|(.*)\s+/ )  {
			print "\t", $1, "\n";
		}
		if ( m[^Exposure Time\s+\|(.*)\s+sec\.] )  {
			print "\tTv: ", $1, "\n";
		}
		if ( m[^FNumber\s+\|(.*)\s+] )  {
			print "\tAv: ", $1, "\n";
		}
	}
}
