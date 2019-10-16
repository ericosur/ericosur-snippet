#!/usr/bin/perl
#
# Regex test
#
# 2006/12/27 by ericosur
#

use strict;
use warnings;


my $ip = "64.156.215.240";
while ($ip =~ m/(\d+)/g)
{
	printf "found '$1' ending at location %d\n", pos($ip);
}

my $data=<<EOL;
0x00960x00fa0x007f0x0035
0x004c0x00320x003c0x000d
0x000a0x00230x003a0x004d
EOL

my @array;

while ( $data =~ m/(0x[0-9a-f]{4})/g )
{
	push @array, $1;
}

for (@array)
{
	printf "%s\t", $_;
}
