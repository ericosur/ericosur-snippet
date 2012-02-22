#!/usr/bin/perl
#
# getprotobyname()
#

use strict;
#use warnings;

my @protocol = qw(tcp ip udp pop3 smtp imap4);

print "demo for getprotobyname()\n";
for my $pro (@protocol)  {
	my $ret = getprotobyname($pro);
	print "$pro - $ret\n";
}
