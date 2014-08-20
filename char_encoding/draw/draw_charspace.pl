#!/usr/bin/perl

#
# read from four tables and draw the relationship for these charset table
#

use strict;
use warnings;

use Image::Magick;
use Compress::Zlib;

my %ioff = (
    "big5_widechar.txt" => "big5w.png",
    "gb2312_widechar.txt" => "gb2312w.png",
    "ucs2_in_big5.txt" => "ucs2big5.png",
    "ucs2_in_gb2312.txt" => "ucs2gb2312.png"
);

my $image;
my $ifh;

# draw yellow dot in 4e00 ~ 9fff
sub draw
{
    return if not $image;

    my $cmd;
    my ($xx, $yy);
    my @pixels;

    for $yy (0x4e..0x9f)  {
        for $xx (0x00..0xff)  {
            $cmd = sprintf "pixel[%d,%d]", $xx, $yy;
            $image->Set($cmd => 'yellow');
        }
    }
}

sub main
{
    my $cmd;
    my ($xx, $yy);
    my $cnt;
    my ($iff, $off);

    foreach $iff (keys %ioff)  {
        if (not $iff =~ m/\.gz$/)  {
            $off = $ioff{$iff};
            $iff .= '.gz';
        }
        print "input from ", $iff,"\n";
        my $gz = gzopen($iff, "rb")
            or (print "Cannot open $iff: $gzerrno\n"
                && next);

        $cnt = 0;
        $image = Image::Magick->new;
        $image->Set(size=>'255x255');
        $image->ReadImage('xc:lightgrey');

        draw() if $iff =~ m/^ucs2/;

        LINE:
        while ($gz->gzreadline($_))  {
            next LINE if /^#/;
            m/^([0-9A-F]{2})([0-9A-F]{2})\s?/;
            $yy = hex('0x' . $1) if $1;
            $xx = hex('0x' . $2) if $2;
            $cmd = sprintf "pixel[%d,%d]", $xx, $yy;
            $image->Set($cmd => 'red');
            ++ $cnt;
            #print $cmd,"\n";
            #last if $cnt > 3;
            print STDERR "$cnt\r";
        }

        die "Error reading from $iff: $gzerrno\n"
            if $gzerrno != Z_STREAM_END ;

        $gz->gzclose() ;

        print "$cnt characters\n";
        if ( -f $off )  {
            print "unlink $off\n";
            unlink $off;
        }
        print "output to $off\n";
        $image->Write($off);
        undef $image;
    }
}

sub readgz
{
    my $pattern = shift;

    foreach my $file (@ARGV) {
        my $gz = gzopen($file, "rb")
            or die "Cannot open $file: $gzerrno\n" ;

        while ($gz->gzreadline($_) > 0) {
            print if /$pattern/ ;
        }

        die "Error reading from $file: $gzerrno\n"
            if $gzerrno != Z_STREAM_END ;

        $gz->gzclose() ;
    }
}

main;
