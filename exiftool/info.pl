#!/usr/bin/perl -w
use Image::ExifTool ':Public';
my $file = $ARGV[0] // "sample.jpg";
my $info = ImageInfo($file);
foreach (keys %$info) {
    print "$_ : $info->{$_}\n";
}
