#!/usr/bin/perl

=pod

=head1 DESCRIPTION

Try to use binary try-and-error to get the minimal valid epoch
from utime under windows.

Use C<utime 0, 0, 'file'> works fine under linux (it would set file
date to Jan 1 1970).
Under win32, the earliest date you could set would be C<Jan 1st 1980>.

=head1 NOTE

=over

=item *
dos, fat16, fat32 epoch from Jan 1st 1980

=item *
unix, java epoch from Jan 1st 1970

=back

=head1 SEE ALSO

http://en.wikipedia.org/wiki/Epoch_(reference_date)
=cut

use strict;
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

sub try_error($$)
{
	my ($lower, $upper) = @_;
	my $ret = 0;	# 0 failed, 1 successful
	my $mid;
	my $max_failed = $lower;
	my $min_success = $upper;

	#print "upper($upper)lower($lower) = ", $upper - $lower, "\n";
	$mid = int(($lower + $upper) / 2);
	my $cnt = 0;
	while ($min_success - $max_failed > 1 )  {
		print "${cnt}\t${max_failed}\t${min_success}\t", $min_success-$max_failed, "\n";
		if ( try($mid) )  {	# successful
			if ($mid < $min_success)  {
				$min_success = $mid;
			}
		}
		else  {	# failed
			if ($mid > $max_failed)  {
				$max_failed = $mid;
			}
		}
		$mid = int(($max_failed + $min_success) / 2);
		$cnt ++;
		#if ($cnt > 99)  {
		#	last;
		#}
	}

	return ($max_failed, $min_success);
}

sub main()
{
	my @arr = ("1975:06:17 12:34:56",
		"2009:06:17 14:30:23");
	my $ep = 0;

	foreach my $ee (@arr)  {
		$ep = get_epoch_from_str($ee);
		print $ep,"\n";
	}

	my ($ll, $uu) = try_error(get_epoch_from_str($arr[0]), get_epoch_from_str($arr[1]));

	show_epoch_in_str($ll);
	show_epoch_in_str($uu);
}

main;
