#!/usr/bin/perl
#
# use "convert" to resize image
#

use strict;

my @flist = glob('*.pbm');
my ($oldf, $newf, $bakf);
my $cmd;

for $oldf (@flist)  {
	$newf = $oldf . '.pbm';
	$bakf = $oldf . '.bak';
	$cmd = sprintf "convert %s -resize 15X15 %s", $oldf, $newf;
	print $cmd,"\n";
	system $cmd;
	rename $oldf, $bakf;
	rename $newf, $oldf;
}
