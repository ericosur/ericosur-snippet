#!/usr/bin/perl

=pod

=head1 DESCRIPTION

Input a big image (i.e. 3288x2952). This script will crop it into
multiple 320x240 small images.

=head1 NOTE

Should run 'exif -r input.jpg -o output.jpg' first to remove EXIF
thumbnail within ''input.jpg''.

=cut


use strict;
use v5.22;
use warnings;
use Image::Magick;

my ($cut_width, $cut_height) = (320, 240);

sub get_crop_cmd($$)
{
	my ($xx, $yy) = @_;

	my $cmd = sprintf("%dx%d+%d+%d", $cut_width, $cut_height,
		$xx*$cut_width, $yy*$cut_height);
	return $cmd;
}

sub process($)
{
	my $ifile = shift;
	my $im = Image::Magick->new();
	my ($width, $height) = $im->Ping($ifile);
	my ($px, $py) = (int($width/$cut_width), int($height/$cut_height));
	my $rc;

	$rc = $im->Read($ifile);
	warn $rc if $rc;

	#printf("%d x %d => %d x %d\n", $width, $height, $px, $py);

	for (my $ii = 0; $ii < $px; $ii++)  {
		for (my $jj = 0; $jj < $py; $jj++)  {
			my $im2 = $im->Clone();
			my $geo = get_crop_cmd($ii, $jj);
			my $ofile = sprintf("cr%02dx%02d.jpg", $ii, $jj);
			say "$geo";
			$rc = $im2->Crop(geometry =>  $geo);
			warn $rc if $rc;
			say "writing $ofile...";
			$rc = $im2->Write($ofile);
			warn $rc if $rc;
			undef $im2;
		}
	}
}

sub main()
{
	my $ifile = $ARGV[0] || die "specify image file name";
	process($ifile);
}

main;
