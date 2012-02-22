#!/usr/bin/perl

# add-bom.pl
#
# add BOM for UTF-8 text file
#
# EF BB BF
#

use strict;
use warnings;

my $bom = "\xef\xbb\xbf";

my $ifile = $ARGV[0] || die "input file name must be specified";
my $bakfile = $ifile . '.bak';
my $ofile = $ifile . '.tmp';

open my $ifh, $ifile or die;
open my $ofh, "> $ofile" or die;

binmode $ofh;

print $ofh $bom;
while (<$ifh>)  {
	print $ofh $_;
}

close $ifh;
close $ofh;

