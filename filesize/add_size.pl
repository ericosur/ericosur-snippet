#!/usr/bin/perl

use strict;

#
# use 'dir /s/b > file.txt
# take the file.txt and add the size of file at column #1
#
# add file size into file list
#

my $infile = $ARGV[0] // "file.txt";		# file list
my $outfile = $ARGV[1] // "filesize.txt";	# file list with file size at column #1
my $count = 0;

printf STDERR "input file: %s\noutput file: %s\n", $infile, $outfile;

open my $ifh, $infile or die "cannot read";
open my $ofh, "> $outfile" or die "cannot write";

while (<$ifh>)
{
	my $size = -1;
	my $line;

	$count ++;
#	s/\r?\n?//;
	s/\n//;
	$line = $_;

	if (-f $line)  {
		$size = -s $line;
		printf $ofh "%d\t\"%s\"\n", $size, $line;
	}

	print STDERR "$count\r";
#	print STDERR "." if (($count % 10) == 0);
}

close $ifh;
close $ofh;

print STDERR "\n";
