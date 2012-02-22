#!/usr/bin/perl

use strict;

my $arg = $ARGV[0] || "stop";

my @vmwares = (
	"VMware Authorization Service",
	"VMware DHCP Service",
	"VMware NAT Service",
	"VMware Registration Service",
	"VMware Virtual Mount Manager Extended"
);

my $cmd;
foreach (@vmwares)  {
	$cmd = sprintf "net %s \"%s\"", $arg, $_;
	print $cmd,"\n";
	system $cmd;
}

