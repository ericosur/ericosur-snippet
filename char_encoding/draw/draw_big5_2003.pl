#!/usr/bin/perl
#
# draw relation bitmap table by using big5-2003 to ucs2 table
#

use strict;
use warnings;

use Image::Magick;
use Compress::Zlib;

my @ofiles = qw(big5-2003.png ucs2-b52003.png);
my $iff = q(big5_2003-b2u.txt.gz);

# draw yellow dot in 4e00 ~ 9fff
sub draw_common($)
{
	my $image = shift;

	my $cmd;
	my ($xx, $yy);
	my @pixels;

	for $yy (0x4e..0x9f)  {
		for $xx (0x00..0xff)  {
			$cmd = sprintf "pixel[%d,%d]", $xx, $yy;
			$image->Set($cmd => 'yellow');
		}
	}
}

sub draw_point($$$)
{
	my ($image, $yy, $xx) = @_;
	$yy = hex('0x' . $yy) if $yy;
	$xx = hex('0x' . $xx) if $xx;
	my $cmd = sprintf "pixel[%d,%d]", $xx, $yy;
	$image->Set($cmd => 'red');
}

sub main
{
	my ($im1, $im2);
	my $cnt = 0;

	$im1 = Image::Magick->new;
	$im1->Set(size=>'255x255');
	$im1->ReadImage('xc:lightgrey');

	$im2 = Image::Magick->new;
	$im2->Set(size=>'255x255');
	$im2->ReadImage('xc:lightgrey');

	print "read data from $iff\n";
    my $gz = gzopen($iff, "rb")
         or (print "Cannot open $iff: $gzerrno\n"
         	&& next);

	draw_common($im2);

	LINE:
	while ($gz->gzreadline($_))  {
		next LINE if /^#/;
		if ( m/^0x([0-9A-F]{2})([0-9A-F]{2})\s?0x([0-9A-F]{2})([0-9A-F]{2})/ )  {
			draw_point($im1, $1, $2);
			#print "$1,$2\n";
			draw_point($im2, $3, $4);
			#print "$3,$4\n";
			++ $cnt;
		}
		print STDERR "$cnt\r";
	}

    die "Error reading from $iff: $gzerrno\n"
    	if $gzerrno != Z_STREAM_END ;

    $gz->gzclose() ;
	print STDERR "$cnt\n";

	print "output to ", $ofiles[0],"\n";
	$im1->Write($ofiles[0]);
	undef $im1;
	print "output to ", $ofiles[1],"\n";
	$im2->Write($ofiles[1]);
	undef $im2;
}


main;
