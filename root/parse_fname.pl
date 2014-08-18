#!/usr/bin/perl
#
# demo of File::Basename
# demo of fileparse()
#
# 2006/12/27 by ericosur
# 2008/02/19 add warning, argument and reviewed

use strict;
use warnings;

use File::Basename;
use Env qw(@PATHEXT);

my $file = $ARGV[0] || 'mnt.bat';
my $result = `which $file`;
chomp $result;

print "$result\n";

my ($base, $path, $type) = fileparse($result, @PATHEXT);

printf "base: <%s>\npath: <%s>\ntype: <%s>\n", $base, $path, $type;
