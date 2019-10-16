#!/usr/bin/perl
# print the hostname
#
# 2006/12/27 by ericosur

use Sys::Hostname;

my $host = hostname();
print "machine name is $host\n";
