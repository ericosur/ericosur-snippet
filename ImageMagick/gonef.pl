#!/usr/bin/perl

#
# to extract embedded jpeg from NEF raw files by calling exiftool
#

use strict;
use warnings;

my $flist = "~list~.txt";
my $cmd;

my $pwd = $ARGV[0] || ".\\";
unless ( $pwd =~ m/\\$/ )  {
	$pwd = $pwd . "\\";
}

$cmd = "cmd /c dir /s /b \"${pwd}*.nef\" > $flist";
print $cmd,"\n";
system $cmd;

open my $fh, $flist or die;

while (<$fh>)  {
	s/[\r\n]//;
	my $ff = $_;
	my $nf = $_;
	$nf =~ s/\.nef/.jpg/i;
	if (-e $ff)  {
		$cmd = sprintf("exiftool -b -JpgFromRaw \"$ff\" > \"$nf\"");
		print $cmd,"\n";
		system $cmd;
	}
}

close $fh;
unlink $flist;
