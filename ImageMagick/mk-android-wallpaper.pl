#!/usr/bin/perl

=pod

My galaxy nexus uses a very wierd  wallpaper ratio.
This script will composite the original image into a very large black background.
So I could crop my image for android wallpaper.

=cut

use strict;
use warnings;

use Image::Magick;
use v5.10;

my $debug = 0;


# try to crop & resize to 8:5
# [in] input file
# [in] output file
sub make_8v5($$)
{
	my ($ifile, $ofile) = @_;
	my ($imgw, $imgh) = (0, 0);
	my $ori = 0; 	# 0: landscape, 1: portrait
	my $geo;
	my $rc;

	my $im1 = Image::Magick->new();
	if ( -f $ifile )  {
		$im1->Read($ifile);
		($imgw, $imgh) = $im1->Ping($ifile);
		if ($imgw > $imgh) {
			$ori = 0;
		} else {
			$ori = 1;
		}
	}

	# must large enough to make android wallpaper corp algorithm happy
	# galaxy nexus is 9:16 (720:1280)
	my ($target_w, $target_h);

	if ($ori == 0) {
		# this ratio is for landscape
		($target_w, $target_h) = (6400, 3600);
	} else {
		# for portrait
		($target_w, $target_h) = (3600, 8000);
	}

	my $im = Image::Magick->new();
	my $size = sprintf("%dx%d", $target_w, $target_h);
	say "size: $size";
	$rc = $im->Set(size => $size);
	$rc = $im->Read('xc:black');

	my ($newx, $newy) = ();
	$newx = ($target_w - $imgw) / 2;
	$newy = ($target_h - $imgh) / 2;
	say "new: $newx, $newy";

	$rc = $im->Composite(image => $im1, x => $newx, y => $newy);
	$im->Write($ofile);
}


sub main()
{
	my @imgs = ($ARGV) // qw(all.jpg);
	my $outimg = 'out.jpg';

	say @imgs;
	if (-f $imgs[0])  {
		say "in: $imgs[0]";
		say "out: $outimg";
		make_8v5($imgs[0], $outimg);
	}

}

main;
