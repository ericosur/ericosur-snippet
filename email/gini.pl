#!/usr/bin/perl
#
# a simple demo about Config::Simple
#

use strict;
use Config::Simple;

my $ini_file = q(gmail.ini);

if (not -e $ini_file)  {
	die "cannot found [$ini_file]\n";
}

my %config = ();
Config::Simple->import_from($ini_file, 'user');
Config::Simple->import_from($ini_file, \%config);

foreach my $k (sort keys %config)  {
	printf("%s => %s\n", $k, $config{$k});
}
