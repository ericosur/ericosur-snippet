#!/usr/bin/perl

#
# compose a command to call exiftool to extract thumbnail image from JPEG images
# and then use Image::Magick to get the size of thumbnail
#
# 2007/02/27 by ericosur
#

use strict;
use warnings;

use Image::Magick;

sub process($);
sub show_image_size($);

if (@ARGV)  {
	foreach (@ARGV)  {
		if ( /\*|\?/ )  {			# if contains '*' or '?'
			#print "glob...'$_'\n";
			my @filelist = glob($_);
			foreach ( @filelist )  {
				process($_) if ( -f $_ );	# file only
			}
		}
		else  {		# without wildcard
			process($_);
		}
	}
}
else  {
	print "no argument, please specify JPEG filenames\n";
}


###############################################################
#
# process sub function
#
###############################################################
sub process($)
{
	my $in = shift;
	my $out = $in;
	my $cmd;
	my $cmd_fmt = "exiftool -b -ThumbnailImage \"%s\" > \"%s\"";
	my $postfix = "-thumb";

	$out =~ s/(.+)\.(.*)/$1$postfix\.$2/i;
	$cmd = sprintf $cmd_fmt, $in, $out;
	print STDERR $cmd, "\n";
	system $cmd;

	show_image_size($out);
}

# just take one argument and print it out
sub show_image_size($)
{
	my $img_file = shift;
	my $im = Image::Magick->new();

	if ( -f $img_file )
	{
		my ($width, $height, $size, $image_format) = $im->Ping($img_file);
		printf "%s: %d, %d, %s\n", $img_file, $width, $height, $image_format;
	}

	undef $im;
}
