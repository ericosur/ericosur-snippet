#!/usr/bin/perl

# print epoch time

use strict;
use Time::Local;
use Data::Dump qw(dump);

sub description()
{
	my @label = qw(sec min hours mday month year wday yday isdst);
	my %pair = ();
	my @loctime = localtime();
	my $i = 0;
	foreach (@label)  {
		$pair{$_} = $loctime[$i++];
	}
	foreach (@label)  {
		printf "%s => %s\n", $_, $pair{$_};
	}
}

sub main()
{
	my ($sec,$min,$hours,$mday,$month,$year,$wday,$yday,$isdst) = localtime;
	# translate localtime list into scalar
	my $time = timelocal($sec,$min,$hours,$mday,$month,$year+1900);

	print "timelocal = ", $time, "\n";
	print "time = ", time(), "\n";	# same as ''date +%s''
	print "call date +%s: ", `date +%s` if $^O eq "linux";

	description();
}

main;

