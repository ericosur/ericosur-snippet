#!/usr/bin/perl

=pod

My galaxy nexus uses a very wierd  wallpaper ratio.
This script will composite the original image into a very large black background.
So I could crop my image for android wallpaper.

=cut

use strict;
use warnings;

use Image::Magick;
use File::Basename;
use Data::Dump qw(dump);
use v5.10;

my $debug = 0;


# try to crop & resize to specified size
# [in] input file name
# [in] output file name
sub make_size($$$$)
{
    dump(@_);
	my ($ifile, $ofile, $target_w, $target_h) = @_;
	my ($imgw, $imgh) = (0, 0);
	my $ori = 0; 	# 0: landscape, 1: portrait
	my $geo;
	my $rc;

	my $im1 = Image::Magick->new();
	if ( -f $ifile )  {
		$im1->Read($ifile);
		($imgw, $imgh) = $im1->Ping($ifile);
		if ($imgw > $imgh) {
			$ori = 0;
		} else {
			$ori = 1;
		}
	} else {
	    say "invalid input file";
	    return;
	}

	printf("w / h = %.3f", $imgw / $imgh);

    if ($target_w < $target_h) {
        ($target_w, $target_h) = ($target_h, $target_w);
    }

	# must large enough to make android wallpaper corp algorithm happy
	# galaxy nexus is 9:16 (720:1280)
	# xperia XL is 9:16 (1080:1920)
	#my ($target_w, $target_h);

	if ($ori == 1) {
		# for portrait
		($target_w, $target_h) = ($target_h, $target_w);
    }

	my $im = Image::Magick->new();
	my $size = sprintf("%dx%d", $target_w, $target_h);
	say "size: $size";
	$rc = $im->Set(size => $size);
	$rc = $im->Read('xc:black');

	my ($newx, $newy) = ();
	$newx = ($target_w - $imgw) / 2;
	$newy = ($target_h - $imgh) / 2;
	say "new: $newx, $newy";

	$rc = $im->Composite(image => $im1, x => $newx, y => $newy);
	$im->Write($ofile);
}

# try to crop & resize to 8:5
# [in] input file
# [in] output file
sub make_8v5($$)
{
	my ($ifile, $ofile) = @_;
	my ($imgw, $imgh) = (0, 0);
	my $ori = 0; 	# 0: landscape, 1: portrait
	my $geo;
	my $rc;

	my $im1 = Image::Magick->new();
	if ( -f $ifile )  {
		$im1->Read($ifile);
		($imgw, $imgh) = $im1->Ping($ifile);
		if ($imgw > $imgh) {
			$ori = 0;
		} else {
			$ori = 1;
		}
	}

	# must large enough to make android wallpaper corp algorithm happy
	# galaxy nexus is 9:16 (720:1280)
	my ($target_w, $target_h);

	if ($ori == 0) {
		# this ratio is for landscape
		($target_w, $target_h) = (6400, 3600);
	} else {
		# for portrait
		($target_w, $target_h) = (3600, 8000);
	}

	my $im = Image::Magick->new();
	my $size = sprintf("%dx%d", $target_w, $target_h);
	say "size: $size";
	$rc = $im->Set(size => $size);
	$rc = $im->Read('xc:black');

	my ($newx, $newy) = ();
	$newx = ($target_w - $imgw) / 2;
	$newy = ($target_h - $imgh) / 2;
	say "new: $newx, $newy";

	$rc = $im->Composite(image => $im1, x => $newx, y => $newy);
	$im->Write($ofile);
}

# get output image file name
sub get_ofn($$)
{
    my $in = shift;
    my $append = shift // "-ext";
    my $jpg = ".jpg";
    my $bsn = basename($in, qw(.jpg .png));
    my $res = $bsn . $append . $jpg;

    # if file name exists, increase suffix
    my $num = 0;
    while (-e $res) {
        $num ++;
        $res = sprintf("%s%s-%d%s", $bsn, $append, $num, $jpg);
    }

    #say "ofn: in: $in";
    #say "ofn: res: $res";
    return $res;
}

sub doit($)
{
    my $im = shift;
    my @comb = (
        #{'n', q(85.jpg), 'w', 8000, 'h', 5000},
        {'n', q(845.jpg), 'w', 8000, 'h', 4494},
        #{'n', q(84.jpg), 'w', 8000, 'h', 4000},
    );

    #dump(%comb);
    foreach my $e (@comb) {
        #printf("n(%s), w(%d), h(%d)\n",
        #    $e->{'n'}, $e->{'w'}, $e->{'h'});
        make_size($im, $e->{'n'}, $e->{'w'}, $e->{'h'});
    }

}

sub main()
{
    my $im = $ARGV[0] // "tong.jpg";
	if ($im && -f $im)  {
		say "in: $im";
        doit($im);
	} else {
	    say "err: please specify input image name";
	}
}

main;
