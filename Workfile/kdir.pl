#!/usr/bin/perl
use strict;
use warnings;

use DateTime;
#use DateTime::Format::Strptime;
use DateTime::Duration;

sub my_ftime($)
{
	my $file = shift;

	my ($atime,$mtime,$ctime) = (stat($file))[8..10];
	my $a_time = localtime($atime);
	my $m_time = localtime($mtime);
	my $c_time = localtime($ctime);

	return ($mtime);
}

sub is_older_than_one_month($)
{
	my $dt_check = shift;
	my $dt_today = DateTime->now();
	my $interval = DateTime::Duration->new(months => 1);

	if ($dt_check < $dt_today - $interval)  {
		return 1;
	}
	else  {
		return 0;
	}
}


sub main()
{
	my @arr_dir = glob("Proj_*");
	my $ofile = 'killolddir.bat';

	open my $ofh, "> $ofile" or die;

	print STDERR "list directories are older than one month:\n";
	foreach (@arr_dir)  {
		my $dt = DateTime->from_epoch( epoch => my_ftime($_) );
		if ( is_older_than_one_month($dt) )  {
			#print "===> ".$_.": ".$dt->ymd . ' ' . $dt->hms."\n";
			print "rd /s/q $_\n";
			print $ofh "rd /s/q $_\n";
		}
		else {
			#print $_.": ".$dt->ymd . ' ' . $dt->hms."\n";
		}
	}

	close $ofh;

	print "you may run $ofile directly to clear old directories\n";
}

main;

