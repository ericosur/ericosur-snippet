#!/usr/bin/perl

use strict;
use warnings;

use Image::Magick;

my $debug_out_image = 0;
my $CORRECT_RESOLUTION = "9991";

# compose imagick geometry string
sub get_crop_center($$$$)
{
	my ($width, $height, $new_width, $new_height) = @_;

	my $x_offset = ($width - $new_width)/2;
	my $y_offset = ($height - $new_height)/2;
	my $geo;

	$geo = sprintf("%dx%d+%d+%d", $new_width, $new_height, $x_offset, $y_offset);

	return $geo;
}


#
# [in]: image magick object
# [in]: geometry for cropping
# [in]: target width
# [in]: target height
# [in]: output file name
#
sub crop_and_resize($$$$$)
{
	my ($im, $geo, $target_w, $target_h, $ofile) = @_;
	my $rc;

	print "geo: $geo\n";
	$rc = $im->Crop(geometry => $geo);
	warn $rc if $rc;
	$rc = $im->Resize(width => $target_w, height => $target_h);
	warn $rc if $rc;

	if ($debug_out_image)  {
		$im->Write($ofile);
		warn $rc if $rc;
	}

	return $im;
}



# try to crop & resize to 8:5
# [in] input file
# [in] output file
sub make_8v5($$)
{
	my ($ifile, $ofile) = @_;
	my ($imgw, $imgh) = (0, 0);
	my ($target_w, $target_h) = (1440, 900);
	my $geo;
	my $im = Image::Magick->new();
	my $rc;

	if ( -f $ifile )  {
		($imgw, $imgh) = $im->Ping($ifile);
		$im->Read($ifile);
	}

	my $newh = 0;
	if ( ($imgw == 1024 && $imgh == 768)
		|| ($imgw == 1280 && $imgh == 960 )
		|| ($imgw == 1600 && $imgh == 1200)
		|| ($imgw == 1280 && $imgh == 1024) )
	{
		$newh = $target_h * $imgw / $target_w;	# keep image width
		$geo = get_crop_center($imgw,$imgh,$imgw,$newh);
		return crop_and_resize($im, $geo, $target_w, $target_h, $ofile);
	}
	elsif ($imgw == $target_w && $imgh == $target_h )
	{
		return $im;
	}
	else  {
		print "size ($imgw, $imgh) not implement yes!\n";
	}
}



# load list file, and randomly pick two file names
# [in] list file name
sub get_fname_from_list($)
{
	my $flist = shift;
	my @lines = ();

	open my $fh, $flist or die;
	while (<$fh>)  {
		s/[\r\n]//;
		push @lines, $_;
	}
	close $fh;

	my $size = scalar @lines;
	return ($lines[int(rand($size))], $lines[int(rand($size))]);
}

sub main()
{
	my ($leftimg, $rightimg) = ();
	my $list = 'list.txt';
	my @imgs = ();

	if ( scalar @ARGV == 0 )  {
		if ( -f $list)  {
			print "use list file to compose wallpaper\n";
			@imgs = get_fname_from_list($list);
		}
		else  {
			die "need specify file name of one image";
		}
	}
	else  {
		@imgs = ($ARGV[0]);
	}

	if (-f $imgs[0])  {
		print "in: $imgs[0]\n";
		$leftimg = make_8v5($imgs[0], 'lhs.jpg');
	}

	$leftimg->Write('out.jpg');
}

main;
