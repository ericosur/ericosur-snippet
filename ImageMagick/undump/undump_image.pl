#!/usr/bin/perl

# draw a image with random rgb value

use strict;
use warnings;

use Image::Magick;

my $img_width = 320;    # need match the dump.bin
my $img_height = 240;   # need match the dump bin
my $img_size = sprintf("%dx%d", $img_width, $img_height);
my $debug = 0;


sub draw_img($$)
{
    my $im;
    my $buf;
    my $ifn = shift;
    my $ofn = shift;

    $im = Image::Magick->new;
    $im->Set(size=>$img_size);
    $im->ReadImage('xc:black');

    printf("read from %s\n", $ifn);
    open my $ifh, $ifn or die;
    binmode $ifh;
    my $cnt = 0;
    my ($r,$g,$b) = ();
    my ($xx, $yy) = ();
    my $rgb888 = 0;

    while (read($ifh, $buf, 2))  {
        my $c = (ord(substr($buf, 0, 1))) | (ord(substr($buf, 1, 1)) << 8);

        $r = ((($c) << 16) >> 27);
        $g = ((($c) << 21) >> 26);
        $b = ((($c) << 27) >> 27);

        $rgb888 = ($b << 3) | ($b & 0x07);
        $rgb888 += (($g << 2) | ($g & 0x03)) << 8;
        $rgb888 += (($r << 3) | ($r & 0x07)) << 16;

        $xx = $cnt % $img_width;
        $yy = $cnt / $img_width;
        my $cmd = sprintf "pixel[%d,%d]", $xx, $yy;
        print $cmd,"\t" if $debug;
        my $color = sprintf("#%06x", $rgb888);
        print $color,"\t" if $debug;
        $im->Set($cmd => $color);
        ++$cnt;
    }

    close $ifh;
    print "cnt = $cnt\n";
    $im->Write($ofn);
    printf("output to %s\n", $ofn);
}

sub main
{
    my $ifile = do { my $arg = $ARGV[0]; defined($arg) ? $arg : 'gdidump.bin' };
    my $ofile = do { my $arg = $ARGV[1]; defined($arg) ? $arg : 'out.bmp' };

    draw_img($ifile, $ofile);
}

main;
