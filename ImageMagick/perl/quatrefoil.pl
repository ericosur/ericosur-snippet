#!/usr/bin/perl

#
# a prototype script to make a quatrefoil image from input
#
# result sample:
# http://www.flickr.com/photos/ericosur/3398418498/
#
#
#

use strict;
use warnings;

use Image::Magick;

my $scale_factor = 0.7;


sub get_crop_rightupper($$)
{
	my ($width, $height) = @_;
	my $new_width = $width * $scale_factor;
	my $new_height = $height * $scale_factor;

	my $x_offset = $width - $new_width;
	my $y_offset = 0;
	my $geo;

	$geo = sprintf("%dx%d+%d+%d", $new_width, $new_height, $x_offset, $y_offset);

	return $geo;
}

sub get_crop_leftlower($$)
{
	my ($width, $height) = @_;
	my $new_width = $width * $scale_factor;
	my $new_height = $height * $scale_factor;

	my $x_offset = 0;
	my $y_offset = $height - $new_height;
	my $geo;

	$geo = sprintf("%dx%d+%d+%d", $new_width, $new_height, $x_offset, $y_offset);

	return $geo;
}

sub get_crop_center($$)
{
	my ($width, $height) = @_;
	my $new_width = $width * $scale_factor;
	my $new_height = $height * $scale_factor;

	my $x_offset = ($width - $new_width)/2;
	my $y_offset = ($height - $new_height)/2;
	my $geo;

	$geo = sprintf("%dx%d+%d+%d", $new_width, $new_height, $x_offset, $y_offset);

	return $geo;
}

sub quatrefoil($$)
{
	my $img_file = shift;
	my $out_file = shift;
	my $im = Image::Magick->new();
	my $rc;
	my $new_file;
	my $geo;

	my ($width, $height) = $im->Ping($img_file);

	$rc = $im->Read($img_file);
	warn $rc if $rc;

	# 2nd Right/upper
	my $im2 = $im->Clone();
	$geo = get_crop_rightupper($width, $height);
	$rc = $im2->Crop(geometry =>  $geo);
	warn $rc if $rc;
	$rc = $im2->Resize(width => $width/2, height => $height/2);
	warn $rc if $rc;
	# 3rd Left/lower
	my $im3 = $im->Clone();
	$geo = get_crop_leftlower($width, $height);
	$rc = $im3->Crop(geometry =>  $geo);
	warn $rc if $rc;
	$rc = $im3->Resize(width => $width/2, height => $height/2);
	warn $rc if $rc;
	# 4th center
	my $im4 = $im->Clone();
	$geo = get_crop_center($width, $height);
	$rc = $im4->Crop(geometry =>  $geo);
	warn $rc if $rc;
	$rc = $im4->Resize(width => $width/2, height => $height/2);
	warn $rc if $rc;
	# 1st resize
	my $im1 = $im->Clone();
	$rc = $im1->Resize(width => $width/2, height => $height/2);
	warn $rc if $rc;
	# composition
	$rc = $im->Composite(image => $im1, x => 0, y => 0);
	$rc = $im->Composite(image => $im2, x => $width/2, y => 0);
	$rc = $im->Composite(image => $im3, x => 0, y => $height/2);
	$rc = $im->Composite(image => $im4, x => $width/2, y => $height/2);
	$rc = $im->Write($out_file);
}


sub main()
{
	my $file = $ARGV[0] || 'all.jpg';
	my $ofile = $file;

	if (! -e $file)  {
		print $file, " not found!\n";
		exit;
	}

	$ofile =~ s/^(.*)\.(.*)/$1_qrt\.$2/;
	print "output to: ", $ofile, "\n";
	quatrefoil($file, $ofile);
}

main;
