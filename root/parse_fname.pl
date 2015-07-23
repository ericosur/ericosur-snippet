#!/usr/bin/perl
#
# demo of File::Basename
# demo of fileparse()
#

use strict;
use warnings;

use File::Basename;

my $file = $ARGV[0] // "/opt/local/lib/libpcre32.a";
print "$file\n";

my ($base, $path, $type) = fileparse($file, qw(.a));

printf "base: <%s>\npath: <%s>\ntype: <%s>\n", $base, $path, $type;
