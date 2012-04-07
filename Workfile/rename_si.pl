#!/usr/bin/perl

use strict;
use File::Glob ':glob';

my @list = glob("Munich_????.*");

my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime;
my $today = sprintf "%02d%02d", ($mon+1), $mday;

my $prefix = $ARGV[0] || 'Munich_';

print "today($today)\n";
print "you might set the prefix through command line\n";

my $oldf;
my $newf;
for (@list)  {
	$oldf = $_;
	m/(\.\w+)/;
	$newf = $prefix . $today . $1 ;
	print "$oldf -> $newf\n";
	rename $oldf, $newf;
}
