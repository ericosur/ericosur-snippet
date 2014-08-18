#!/usr/bin/perl

#
# D:\download\STQB64.BAS
# file:///D:/download/STQB64.BAS
#

use v5.10;

my $path = $ARGV[0] || q(D:\\test.txt);
$path =~ s/\\/\//g;
$path = "file:///" . $path;

say $path;
