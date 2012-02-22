#!/usr/bin/perl

use strict;

# calculate the total size from filesize.txt
#
# use 'dir /s/b filenames > file.txt
# use ttgo.pl file.txt filesize.txt
#
# the content of filesize.txt would be:
# 1736	"D:\Project\Dusseldorf_20071114\Dusseldorf_20071114\j2me\vm\jblendia\include\ksi\kjava_sys_data.h"
#

my $file = $ARGV[0] || "filesize.txt";
my $total = 0;
my $line = 0;
my $size = 0;

printf STDERR "input file: %s\n", $file;

open FH, $file or die;
while (<FH>)  {
	s/\r?\n?//;
	next if /^$/;
	$line ++;

	if ( /(\d+)\t\"(.+)\"/ )  {
		$size = $1;
	}
	elsif ( -f $_ )  {
		$size = -s $_;
	}
	else  {
		$size = 0;
	}

#	print STDERR $size, "\n";
	$total += $size;

	print STDERR "$line\r";
}
close FH;

print STDERR "\n";

my $disp = $total;
# also demo a complex regular express to add ',' into every three digits
$disp =~ s/(?<=\d)(?=(\d\d\d)+$)/,/g;
print STDERR $disp, " bytes \n";

show($total);

sub show()
{
	my $num = shift;
	my @unit = qw(B KB MB GB TB invalid error what nocanbe);
	my $idx = 0;
	my $qu = 0;

	do  {
		$qu =  $num / 1024;
		$idx++ if ($qu >= 1);
		goto OUT if ($qu <= 1);
		$num = $qu;
	} while ( $num >= 1 );
OUT:

#	print "idx = $idx\n";
	print STDERR $num, " ", $unit[$idx], "\n";
}
