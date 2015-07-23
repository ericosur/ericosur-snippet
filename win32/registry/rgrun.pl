#!/usr/bin/perl
#
# list the run key from HKLM
#
# 2007/01/10 by ericosur

use Win32::TieRegistry;

$Registry->Delimiter("/");
my $runs= $Registry->{"HKEY_LOCAL_MACHINE/Software/Microsoft/"
		. 'Windows/CurrentVersion/Run/'};

LOOP:
foreach ( keys %$runs )
{
	next LOOP if ( m[/$] );
	print "$_: ", $runs->{$_}, "\n";
}
