#!/usr/bin/perl
#!/bin/perl

#
# get the size of JPG file by using Image::Magick
# take wildcard filenames from command line
#
# Jun 23 2006	add wildcards support by ericosur
#


use strict;
use warnings;

use Image::Magick;

sub show_image_size($);

if (@ARGV)  {
	foreach (@ARGV)  {
		if ( /\*|\?/ )  {			# if contains '*' or '?'
			#print "glob...'$_'\n";
			my @filelist = glob($_);
			foreach ( @filelist )  {
				show_image_size($_) if ( -f $_ );	# file only
			}
		}
		else  {		# without wildcard
			show_image_size($_);
		}
	}
}
else  {
	printf "Usage: %s <filename> [filename...] \n", $0;
}

#
# just take one argument and print it out
#
sub show_image_size($)
{
	my $img_file = shift;
	my $im = Image::Magick->new();
	my $rc = $im->Read($img_file);

	die "Cannot read $img_file: $rc" if $rc;
	my ($width, $height, $format) = $im->Get('width', 'height', 'magick');

	printf "%s: %d, %d, %s\n", $img_file, $width, $height, $format;
}
