#!/usr/bin/env perl

#
# make a empty image with specified:
# width, height, color, file name
#
# refer to: https://www.imagemagick.org/script/perl-magick.php
#

use strict;
use warnings;
use Image::Magick;

my $debug = 0;

sub get_size($$)
{
    my $w = shift;
    my $h = shift;
    my $size = sprintf("%d x %d", $w, $h);
    if ($debug) {
        printf("return size: %s\n", $size);
    }
    return $size;
}

# [in] width
# [in] height
# [in] specified filled color
# [in] output file name
sub make_empty_image($$$$)
{
    my $width = shift;
    my $height = shift;
    my $color = shift;
    my $fname = shift;

    if ($debug) {
        printf("arg: %d,%d,%s,%s\n", $width, $height, $color, $fname);
    }

    my $im = Image::Magick->new(size => get_size($width, $height));
    my $rc;

    $rc = $im->Read('xc:black');
    warn $rc if $rc;

    $rc = $im->Color(color => $color);
    warn $rc if $rc;

    $im->Write($fname);
    printf("output to %s\n", $fname);
}

#
# main procedure starts here
#
sub main()
{
    my $color = q(gold);
    make_empty_image(640, 480, $color, $color . ".png");
    $color = q(#404040);
    make_empty_image(640, 480, $color, "dark.png");
}

main;
