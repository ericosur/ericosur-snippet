#!/usr/bin/env perl

#
# get the size of JPG file by using Image::Magick
# take wildcard filenames from command line
#

use strict;
use warnings;

use Graphics::Magick;
use Config::JSON;

sub load_setting($)
{
    my $file = shift;
    my $cfg = Config::JSON->new($file);

    my $rp = $cfg->get("img_size.pl");
    my $data = $rp->{'data'};

    #print $data,"\n";
    return $data;
}

#
# just take one argument and print it out
#
sub show_image_size($)
{
    my $img_file = shift;
    my $im = Graphics::Magick->new();
    my $rc = $im->Read($img_file);

    die "Cannot read $img_file: $rc" if $rc;
    my ($width, $height, $format) = $im->Get('width', 'height', 'magick');

    printf "%s: %d, %d, %s\n", $img_file, $width, $height, $format;
}

sub main()
{
    if (@ARGV)  {
        foreach (@ARGV)  {
            if ( /\*|\?/ )  {           # if contains '*' or '?'
                #print "glob...'$_'\n";
                my @filelist = glob($_);
                foreach ( @filelist )  {
                    show_image_size($_) if ( -f $_ );   # file only
                }
            }
            else  {     # without wildcard
                show_image_size($_);
            }
        }
    }
    else  {
        printf "Usage: %s <filename> [filename...] \n", $0;

        printf("\ndemo if no argument provided:\n");
        my $data = load_setting('setting.json');
        show_image_size($data);
    }
}

main;
