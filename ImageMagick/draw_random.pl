#!/usr/bin/perl

use strict;
use warnings;
use 5.010;
use Image::Magick;

my ($maxx, $maxy) = (640, 640);
my $pix_name = 'test.bmp';

sub draw_bitmap()
{
	my $im = Image::Magick->new(size => "$maxx x $maxy");
	my $rc;
	my $debug = 0;

	$rc = $im->Read('xc:black');
	warn $rc if $rc;
	my $color_hex;
	for (my $ii=0; $ii<$maxx; ++$ii)  {
		for (my $jj=0; $jj<$maxy; ++$jj)  {
			my $rr = int(rand(100));
			#say $rr;
			if ( $rr < 50 )  {
				$color_hex = "#FFFFFF";
			} else {
				next;
			}

			$im->Set("pixel[$ii,$jj]"=>$color_hex);
		}
	}

	$im->Write($pix_name);
}

sub main()
{
	# if you specify the same seed number all the time
	# you will get the same one random pattern
	srand(100);
	draw_bitmap();
}

main;
