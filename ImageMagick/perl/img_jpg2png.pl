#!/usr/bin/perl

#
# 2006/12/27 by ericosur
#
# try to use Image::Magick to convert jpg to png
#

use strict;
use Image::Magick;

sub main()
{
	if (not $ARGV[0])
	{
		print "please specify a jpeg file\n";
		exit;
	}

	my $img_file = $ARGV[0];
	my $out_file = $img_file;
	$out_file =~ s/jpg/png/i;

	print $img_file, ' ', $out_file, "\n";

	my $img = Image::Magick->new();
	my $rc = $img->Read($img_file);
	warn $rc if $rc;
	$rc = $img->Write($out_file);
	warn $rc if $rc;
	#
	# draw a image - test
	#
	$out_file = q(whiteGrad.png);
	@$img = ();
	$img->Set(size => '1600x1200');
	$rc = $img->Read('gradient:#000000-#3f3f3f');
	warn $rc if $rc;
	# $img->Rotate(degrees => -90);
	print "write $out_file...\n";
	$rc = $img->Write($out_file);
	warn $rc if $rc;
}

main;
