#!/usr/bin/perl
# test write a binary file with sys*()
# Jun 14 2005 by ericosur
#
# $Id$
# $Source$
# $Author$
#

use strict;
use warnings;

use Fcntl qw(SEEK_END SEEK_CUR SEEK_SET);

my $file = 'out.bin';

print "output file: $file\n";
open FILE, "> $file" or die;
binmode FILE;

my $buf;

for my $elem (1..1024)
{
	$buf = $buf . chr($elem % 0xFF);
}

print length($buf), "\n";

syswrite FILE, $buf, 800 ;
sysseek FILE, 0x64, SEEK_SET;
syswrite FILE, $buf, 256;

close FILE;
