#!/usr/bin/perl
#
# wildcards supported
#

use strict;
use warnings;

use Image::Magick;

sub scale_image($);

my $proc = \&scale_image;

sub main()
{
	process_arg();
}


# process command line file names and wildcards
sub process_arg()
{
	exit (2) if not @ARGV;

	for (@ARGV)  {
		# wildcards file names
		if ( m/\*|\?/ )  {		# if contains '*' or '?'
			#print "glob...'$_'\n";
			my @filelist = glob($_);
			for ( @filelist )  {
				&$proc($_) if ( -f $_ );	# file only
			}
		}
		# file list from command line
		elsif ( m/^@/ )  {
			s/^@//;
			get_filename_from_list($_);
		}
		# file names from command line without wildcards
		else  {
			&$proc($_) if ( -f $_ );	# file only
		}
	}
}


# read file name from list file
sub get_filename_from_list()
{
	my $list_file = shift;
	open my $fh, $list_file or die;

	while (<$fh>)  {
		s/\r//;
		s/\n//;

		&$proc($_);
	}

	close $fh;
}


# just take one argument and print it out
sub scale_image($)
{
	my $img_file = shift;
	my $im = Image::Magick->new();
	my $out_file = $img_file;
	my $rc;

	#print STDERR $img_file,"\n";
	$out_file =~ s[(.*?)\.jpg][$1_resized\.jpg]i;

	my $ref_img = test($img_file);

	print $ref_img,"\n";
	$im->BlobToImage($$ref_img);

#	if ( -f $img_file )  {
		#my ($width, $height, $size, $image_format) = $im->Ping($img_file);
		my ($width, $height, $size, $image_format) = $im->Ping(blob => $img_file);
		printf "%s: %d, %d, %s\n", $img_file, $width, $height, $image_format;
#	}
#
#	$rc = $im->Read($img_file);
#	return $rc if $rc;
#

#	$rc = $im->Scale(geometry => '320x240>');
#	warn $rc if $rc;

#	$rc = $im->Write($out_file);
#	warn $rc if $rc;

	undef $im;
}

sub test($)
{
	my $file = shift;
	open my $ff, $file or die;
	binmode $ff;
	my $image_data = <$ff>;
	close $ff;

	die if not $image_data;
	return \$image_data;
}

main();
