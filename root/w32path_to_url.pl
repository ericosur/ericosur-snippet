#!/usr/bin/perl

#
# D:\download\STQB64.BAS
# file:///D:/download/STQB64.BAS
#

use 5.010;

my $path = $ARGV[0] || q(D:\\test.txt);
$path =~ s/\\/\//g;
$path = "file:///" . $path;

say $path;
