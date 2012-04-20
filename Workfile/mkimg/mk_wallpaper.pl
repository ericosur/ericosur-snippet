#!/usr/bin/perl

use strict;
use warnings;

use Image::Magick;

my $debug_out_image = 0;
my $CORRECT_RESOLUTION = "9991";
my $maxx = 2720;
my $maxy = 1024;

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


# try to crop & resize to 5:4
# [in] input file
# [in] output file
sub make_5v4($$)
{
	my ($ifile, $ofile) = @_;
	my ($imgw, $imgh) = (0, 0);
	my ($target_w, $target_h) = (1280, 1024);
	my $geo;
	my $im = Image::Magick->new();
	my $rc;

	if ( -f $ifile )  {
		($imgw, $imgh) = $im->Ping($ifile);
		$im->Read($ifile);
	}

	my $neww = 0;
	if ( ($imgw == 1024 && $imgh == 768)
		|| ($imgw == 1280 && $imgh == 960 )
		|| ($imgw == 1600 && $imgh == 1200) )
	{
		$neww = $target_w * $imgh / $target_h;	# keep image height
		$geo = get_crop_center($imgw,$imgh,$neww,$imgh);
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

# test white image
sub make_white_image($)
{
	my $oimg = shift;
	my $im = Image::Magick->new(size => "$maxx x $maxy");
	my $rc;

	$rc = $im->Read('xc:white');
	warn $rc if $rc;

#1440x900
	$rc = $im->Draw(
		primitive => 'rectangle',
		points => "0,0 1440,900",
		stroke => 'black',
		fill => 'grey',
		strokewidth => 2
	);
	warn $rc if $rc;
#1280x1024
	$rc = $im->Draw(
		primitive => 'rectangle',
		points => "1440,0 2720,1024",
		stroke => 'red',
		fill => 'grey',
		strokewidth => 2
	);
	warn $rc if $rc;

	$im->Write($oimg);
}

# [in] output file name
# [in] left hand side image
# [in] right hand side image
sub compose_wallpaper($$$)
{
	my ($oimg, $im_left, $im_right) = @_;

	my $im = Image::Magick->new(size => "$maxx x $maxy");
	my $rc;

	$rc = $im->Read('xc:black');
	warn $rc if $rc;

#1440x900
	if ($im_left)  {
		$rc = $im->Composite(image => $im_left, x => 0, y => 0);
		warn $rc if $rc;
	}
#1280x1024
	if ($im_right)  {
		$rc = $im->Composite(image => $im_right, x => 1440, y => 0);
		warn $rc if $rc;
	}

	$im->Write($oimg);
	warn $rc if $rc;
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


# compose date/time string for subject
sub get_date()
{
	my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $date = sprintf "%04d/%02d/%02d_%02d:%02d", $year+1900, $mon + 1, $mday, $hour, $min;
	#print "$date\n";
	return $date;
}


sub write_log($)
{
	my $file = "wallpaper.log";
	my $date = get_date();
	my $msg = shift;

	open my $fh, ">>", $file or die;
	print $fh $date, "\t", $msg, "\n";
	close $fh;
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
			die "need specify two images";
		}
	}
	else  {
		@imgs = ($ARGV[0], $ARGV[1]);
	}

	if (-f $imgs[0])  {
		print "in: $imgs[0]\n";
		$leftimg = make_8v5($imgs[0], 'lhs.jpg');
	}
	if (-f $imgs[1])  {
		print "in: $imgs[1]\n";
		$rightimg = make_5v4($imgs[1], 'rhs.jpg');
	}
	# suggest using bitmap format for wallpaper
	compose_wallpaper('myngc.bmp', $leftimg, $rightimg);

	# write log to record used images
	my $msg = $imgs[0] . "\t" . $imgs[1];
	write_log($msg);
}

main;
