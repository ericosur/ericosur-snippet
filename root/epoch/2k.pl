#!/usr/bin/perl

#
# try to get 2000/01/01 0:0:0 UTC epoch
# and try to translate it to readable format
#

use strict;
use warnings;

use Time::Local;
use DateTime;

my $debug = 0;

sub get_epoch_from_str($)
{
	my $str = shift;
	my $epoch = 0;
	my ($yy, $mon, $dd, $hh, $mm, $ss) = ();

	if ( $str =~ m/(\d+):(\d+):(\d+) (\d+):(\d+):(\d+)/ )  {
		$yy = $1;
		$mon = $2;
		$dd = $3;
		$hh = $4;
		$mm = $5;
		$ss = $6;
		$epoch = timelocal($ss, $mm, $hh, $dd, $mon-1, $yy);
		if ($debug)  {
			print "epoch: ", $epoch, "\n";
		}
	}
	return $epoch;
}

sub show_epoch_in_str($)
{
	my $ep = shift || 0;

	my $dt = DateTime->from_epoch( epoch => $ep );
	my $ret = $dt->ymd . ' ' . $dt->hms;

	# we will get UTC time
	print $ret, " UTC\n";
}

sub try($)
{
	my $val = shift;
	my $rr;

	$rr = utime $val, $val, "foo";
	printf STDERR "try %d and %s...\n", $val, ($rr?"ok":"fail");
	return $rr;
}


sub main()
{
	# try to express 2000/01/01 00:00:00 UTC, here is +0800 time zone
	my $start = "2000:1:1 8:0:0";

	my $ep_start = get_epoch_from_str($start);
	print "epoch at start point: $ep_start\n";

	# value of $test is Feb 28 2009 13:30:56 UTC by using epoch reference
	# from 2000/01/01 00:00:00 UTC
	my $test = 1000000000;

	$test = $test + $ep_start;	# so we got the unix epoch time
	show_epoch_in_str($test);
}

main;

