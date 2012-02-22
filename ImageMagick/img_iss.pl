#!/usr/bin/perl
#!/bin/perl

#
# report the file name which pixel size is smaller than $size_condition
# take wildcard filenames and list file from command line
# you may build a list file contains full path to image files into
# list file and issue command like:
#
#     img_iss.pl  @img_list.txt
#
# It gets slow while process large image file.
#
#
# Sep 8 2006 add progress info by ericosur
#

use strict;
use warnings;

use Image::Magick;

my $count = 0;
my $size_condition = 640*480;

sub get_filename_from_list($);
sub test_image_size($);

sub main
{
	#
	# most completely glob / argv here
	#
	if (@ARGV)  {
		foreach (@ARGV)  {
			if ( /\*|\?/ )  {			# if contains '*' or '?'
				#print "glob...'$_'\n";
				my @filelist = glob($_);
				foreach ( @filelist )  {
					test_image_size($_) if ( -f $_ );	# file only
				}
			}
			elsif ( /@/ ) {
				s/@//;
				get_filename_from_list($_);
			}
			else  {		# without wildcard
				test_image_size($_);
			}
		}
		printf "%d files checked\n", $count;
	}
	else  {
		printf "\n%s <filename> [\@list file] [filenames...] \n", $0;
	}
}

##############################################################################

sub get_filename_from_list($)
{
	my $list_file = shift;

	open FH, $list_file or die;

	while (<FH>)
	{
		s/\r//;
		s/\n//;

		test_image_size($_);
	}

	close FH;
}

# just take one argument and print it out
sub test_image_size($)
{
	my $img_file = shift;

	if ( -f $img_file )
	{
		my $im = Image::Magick->new();
#		my $rc = $im->Read($img_file);

#		die "Cannot read $img_file: $rc" if $rc;
#		my ($width, $height) = $im->Get('width', 'height');

		my ($width, $height, $size, $format) = $im->Ping($img_file);

		if ( $width * $height < $size_condition )
		{
			printf "%s: %d, %d\n", $img_file, $width, $height;
		}
		$count ++;
		# progress update info
		print STDERR "$count ...\n" if ($count % 20 == 0);
	}
	else
	{
		printf "%s not found\n", $img_file;
	}
}

main();

__END__;
