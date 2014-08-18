#!/usr/bin/perl
#
# get registry data demo
# list all the tips of the day from registry
#
# 2007/01/10 by ericosur

use Win32::TieRegistry;

$Registry->Delimiter("/");
my $tips= $Registry->{"HKEY_LOCAL_MACHINE/Software/Microsoft/"
		. 'Windows/CurrentVersion/Explorer/Tips/'};

foreach ( keys %$tips )
{
	print "$_: ", $tips->{$_}, "\n";
}
