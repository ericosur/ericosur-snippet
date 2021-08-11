#!/usr/bin/perl -w

BEGIN {push @INC, '/bs2/Image-ExifTool-12.29/lib'}

use Image::ExifTool ':Public';
my $file = $ARGV[0] // "sample.jpg";
my $info = ImageInfo($file);
foreach (keys %$info) {
    print "$_ : $info->{$_}\n";
}
