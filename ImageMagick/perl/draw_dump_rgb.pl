#!/usr/bin/perl

# draw a image with random rgb value

use strict;
use warnings;

use Image::Magick;

my $img_width = 128;
my $img_height = 160;
my $img_size = sprintf("%dx%d", $img_width, $img_height);
my $ofile = 'out.bmp';

sub draw_img()
{
	my $im;

	$im = Image::Magick->new;
	$im->Set(size=>$img_size);
	$im->ReadImage('xc:black');

	for (my $xx = 0; $xx < $img_width; ++$xx)  {
		for (my $yy = 0; $yy < $img_height; ++$yy)  {

			my $cmd = sprintf "pixel[%d,%d]", $xx, $yy;
			my $color = sprintf("#%02x%02x%02x",
				int(rand(255)), int(rand(255)), int(rand(255)));
			$im->Set($cmd => $color);

		}
	}

	$im->Write($ofile);
}

sub main
{
	draw_img();
	print "output image: $ofile\n";
}

main;
