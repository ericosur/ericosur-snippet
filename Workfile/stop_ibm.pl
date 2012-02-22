#!/usr/bin/perl

use strict;

my $arg = $ARGV[0] || "stop";

my @ibms = (
   "IBM HTTP Server 6.0",
   "IBM Rational ClearQuest Registry Server",
   "IBM Rational Lock Manager",
   "IBM WebSphere Application Server V6 - RWP servlet",
   "Atria Location Broker",
);

my $cmd;
foreach (@ibms)  {
	$cmd = sprintf "net %s \"%s\"", $arg, $_;
	print $cmd,"\n";
	system $cmd;
}

