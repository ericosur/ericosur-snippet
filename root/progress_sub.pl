#!/usr/bin/perl

use strict;
use warnings;


#
# demo a text animation while a long operatoin
#
sub print_process_status($)
{
    my $i = shift;
    my $j = $i % 4;
    SWITCH :
    {
		$j == 0 && do { print STDERR " (|)\r";  last SWITCH; };
		$j == 1 && do { print STDERR " (/)\r";  last SWITCH; };
		$j == 2 && do { print STDERR " (-)\r";  last SWITCH; };
		$j == 3 && do { print STDERR " (\\)\r"; last SWITCH; };
    }
}

sub main
{
	my $upper_limit = 10;
	my $delay = 1;

	for (0 .. $upper_limit)  {
		sleep($delay);
		print_process_status($_);
	}
}

main;
