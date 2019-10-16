#!/usr/bin/perl
#
# get local ip and write to remote file
#
# 2005/08/17	add by rasmus
#
use strict;
use warnings;

use Sys::Hostname;

#
# get local ip with 'ipconfig'
#
sub get_ip
{
	if ($^O eq 'linux')  {
		return "no ipconfig in linux";
	}

	my $res = `ipconfig`;
	my $ip;

	return if not $res;
	$res =~ /^\s+IP Address.*:\s+(.*)$/m;
	$ip = $1;
	#print "ip = $ip\n";
	return $ip;
}

#
# get the hostname
#
sub get_hostname
{
#	my $hostname = `hostname`;
#	chomp $hostname;
#	return $hostname;

	my $host = hostname();
#	print "machine name is $host\n";
	return $host;
}

#
# get the current date/time to compose filename
#
sub get_date
{
	my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime;
	my $date = sprintf "%04d-%02d-%02d", $year+1900, $mon + 1, $mday;
	#print "$date\n";
	return $date;
}

sub main
{
	printf "host: %s\nip: %s\ndate: %s\n",
		get_hostname(),
		get_ip(),
		get_date();
}

main;
