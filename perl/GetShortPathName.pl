#!/usr/bin/perl
# use the  GetShortPathName / GetLongPathName
#
# 2006/12/27 by ericosur

use Win32;

my $arg;

my $userprofile = $ENV{"USERPROFILE"};

$arg = $ARGV[0] || $userprofile;

my $short = Win32::GetShortPathName($arg);
my $long = Win32::GetLongPathName($arg);

printf "arg(%s)\nshort(%s)\nlong(%s)\n", $arg, $short, $long;
