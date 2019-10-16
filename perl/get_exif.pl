#!/usr/bin/perl
#
# 2006/12/27 by ericosur
#

#
# use external utility 'exif' to get exif info
#

package Rasmus;

{
	return TRUE;
}

sub get_exif()
{
	my $cmd = shift;

	$cmd = 'exif ' . $cmd;
	print $cmd;

	my $result = `$cmd`;
	my @lines = split /\n/, $result;
	my $fnumber;
	my $exposure;
	my $focal;
	my $flash = 0;

	$result = undef;
	foreach (@lines)
	{
		# Exposure Time
		if ( /^Exposure Time\s+\|(.*) sec./ )
		{
			$exposure = $1;
#			print "<$exposure>";
			$result .= $exposure . "s ";
		}
		# FNumber
		elsif ( /^FNumber\s+\|(.*?)\s+$/ )
		{
			$fnumber = $1;
#			print "<$fnumber>";
			$result .= $fnumber . ' ';
		}
		# Focal Length        |35.0 mm
		elsif ( /^Focal Length\s+\|(.*?)\s+$/ )
		{
			$focal = $1;
#			print "<$focal>";
			$result = $result . '@' . $focal;
		}
		# flash status
		elsif ( /^Flash\s+\|(\d+)\s+/ )
		{
			$flash = $1;
#			print "<$flash>";
		}
	}

	if ($flash > 0)
	{
		$result .= " flash fired";
	}

	printf "%s: %s\n", $cmd, $result;
	return $result;
}
