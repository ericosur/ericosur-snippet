#!/usr/bin/perl
#!/bin/perl

#
# 2006/12/27 by ericosur
#


use Image::Magick;

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
@$img = ();
$img->Set(size => '100x600');
$rc = $img->Read('gradient:#000000-#3f3f3f');
warn $rc if $rc;
# $img->Rotate(degrees => -90);
$rc = $img->Write('whiteTile.bmp');
warn $rc if $rc;
