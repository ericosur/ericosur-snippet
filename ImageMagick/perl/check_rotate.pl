#!/usr/bin/perl

#
#  first script using Image::ExifTool package
#  using ppm to install
#
# 2007/03/27 by ericosur

use strict;
use warnings;

use Image::ExifTool qw(:Public);
use Image::Magick;

sub process($);
sub get_orientation($);
sub get_image_size($);

my $verbose = 0;

#
# start main procedure
#
sub main()
{

    my $file = 'list.txt';

    open my $fh, $file or die "file list needed\n";

    print '@echo off\n';
    print "rem brutely rotated image list:\n";

    while (<$fh>)  {
        s/\r//;
        s/\n//;

        process($_);
    }

    close $fh;
}

sub process($)
{
    my $file = $_;
    my $result1 = 0;
    my $result2 = 0;
    my $total_file = 0;
    my $found_file = 0;

    printf "%s:\n", $_ if $verbose == 1;
    $result1 = get_orientation($file);
    $result2 = get_image_size($file);

    if ($result1 == 1 && $result2 == 1)  {
        my $cmd = sprintf "exiftool -exiftool -Orientation=Horizontal \"%s\"", $file;

        print $file, "\n";
        system $cmd;
    }
}


sub get_orientation($)
{
    my $img_file = $_;
    my $is_rotate = 0;

    if ( -f $img_file )  {
        my $info = ImageInfo($img_file);
        my ($orient, $rotate) = (
            $$info{'Orientation'},
            $$info{'Auto Rotate'},
        );

        if ( $orient =~ /rotate/i )  {
            $is_rotate = 1;
        }

        if ($verbose == 1)  {
            print $orient;
            print "\t", $rotate if $rotate;
            print "\n";
        }
    }
    return $is_rotate;
}


sub get_image_size($)
{
    my $img_file = $_;
    my $result = 0;

    if (-f $img_file)  {
        my $im = Image::Magick->new();

        if ( -f $img_file )  {
            my ($width, $height) = $im->Ping($img_file);
            printf "%d, %d\n", $width, $height if $verbose == 1;
            if ($width < $height)  {
                $result = 1;
            }
        }
        undef $im;
    }
    return $result;
}

main;

