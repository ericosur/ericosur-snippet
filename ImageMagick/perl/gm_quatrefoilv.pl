#!/usr/bin/perl

#
# a prototype script to make a quatrefoil image from input
#
# result sample:
# http://www.flickr.com/photos/ericosur/3398405458/
# from:
# http://www.flickr.com/photos/ericosur/2392667216/
#


use strict;
use warnings;

use Config::JSON;
use Graphics::Magick;

my $scale_factor = 0.6;

sub show($)
{
    printf("geo = %s\n", shift);
}

sub get_crop_1st($$)
{
    my ($width, $height) = @_;
    my $new_width = $width * 0.2;
    my $new_height = $height * 0.75;

    my $x_offset = ($width - $new_width) / 2;
    my $y_offset = ($height - $new_height) / 2;;
    my $geo = sprintf("%dx%d+%d+%d", $new_width, $new_height, $x_offset, $y_offset);

    return $geo;
}

sub get_crop_2nd($$)
{
    my ($width, $height) = @_;
    my $new_width = $width / 4;
    my $new_height = $height;

    my $x_offset = ($width - $new_width) / 2;
    my $y_offset = 0;
    my $geo = sprintf("%dx%d+%d+%d", $new_width, $new_height, $x_offset, $y_offset);

    return $geo;
}

sub get_crop_3rd($$)
{
    my ($width, $height) = @_;
    my $new_width = $width * 0.2;
    my $new_height = $height * 0.7;

    my $x_offset = ($width - $new_width)/2 - ($width / 10);
    my $y_offset = ($height - $new_height) / 2;
    my $geo = sprintf("%dx%d+%d+%d", $new_width, $new_height, $x_offset, $y_offset);

    return $geo;
}

sub get_crop_4th($$)
{
    my ($width, $height) = @_;
    my $new_width = $width * 0.3;
    my $new_height = $height * 0.9;

    my $x_offset = ($width - $new_width)/2 + ($width / 10);
    my $y_offset = ($height - $new_height) / 2;
    my $geo = sprintf("%dx%d+%d+%d", $new_width, $new_height, $x_offset, $y_offset);

    return $geo;
}

sub quatrefoil($$)
{
    my $img_file = shift;
    my $out_file = shift;
    my $im = Graphics::Magick->new();
    my $rc;
    my $new_file;
    my $geo;

    my ($width, $height) = $im->Ping($img_file);

    $rc = $im->Read($img_file);
    warn $rc if $rc;

    # 1st
    my $im1 = $im->Clone();
    $geo = get_crop_1st($width, $height);
    show($geo);
    $rc = $im1->Crop(geometry =>  $geo);
    warn $rc if $rc;
    $rc = $im1->Resize(width => $width/4, height => $height);
    warn $rc if $rc;
    # 2nd Right/upper
    my $im2 = $im->Clone();
    $geo = get_crop_2nd($width, $height);
    show($geo);
    $rc = $im2->Crop(geometry =>  $geo);
    warn $rc if $rc;
    $rc = $im2->Resize(width => $width/4, height => $height);
    warn $rc if $rc;
    # 3rd Left/lower
    my $im3 = $im->Clone();
    $geo = get_crop_3rd($width, $height);
    show($geo);
    $rc = $im3->Crop(geometry =>  $geo);
    warn $rc if $rc;
    $rc = $im3->Resize(width => $width/4, height => $height);
    warn $rc if $rc;
    # 4th center
    my $im4 = $im->Clone();
    $geo = get_crop_4th($width, $height);
    show($geo);
    $rc = $im4->Crop(geometry =>  $geo);
    warn $rc if $rc;
    $rc = $im4->Resize(width => $width/4, height => $height);
    warn $rc if $rc;
    # composition
    $rc = $im->Composite(image => $im1, x => 0, y => 0);
    $rc = $im->Composite(image => $im2, x => $width/4, y => 0);
    $rc = $im->Composite(image => $im3, x => $width/2, y => 0);
    $rc = $im->Composite(image => $im4, x => $width*3/4, y => 0);
    $rc = $im->Write($out_file);
}

sub load_setting($)
{
    my $file = shift;
    my $cfg = Config::JSON->new($file);

    my $rp = $cfg->get("gm_quatrefoilv.pl");
    my $data = $rp->{'data'};

    #print $data,"\n";
    return $data;
}


sub main()
{
    my $file;
    my $ofile;

    if (@ARGV) {
        $file = $ARGV[0];
    } else {
        $file = load_setting('setting.json');
    }

    $ofile = $file;

    if (! -e $file)  {
        print $file, " not found!\n";
        exit;
    }

    $ofile =~ s/^(.*)\.(.*)/$1_qrt\.$2/;
    print "output to: ", $ofile, "\n";
    quatrefoil($file, $ofile);
}

main;
