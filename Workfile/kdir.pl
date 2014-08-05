#!/usr/bin/perl
use strict;
use warnings;

use DateTime;
#use DateTime::Format::Strptime;
use DateTime::Duration;

my $dt_today = DateTime->now();
my $interval = DateTime::Duration->new(months => 1);

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

	if ($dt_check < $dt_today - $interval)  {
		return 1;
	}
	else  {
		return 0;
	}
}


sub main()
{
#    my $dirn = "Proj_*";
    my $dirn = "*";
	my @arr_dir = glob($dirn);
	my $ofile = 'killolddir.bat';
    my $rmcmd = 'rd /s /q';	# it's similar to 'rm -rf' for DOS

	printf STDERR "list dir (%s) are older than one month:\n", $dirn;
    if (scalar @arr_dir == 0)  {
        print STDERR "no matched dirs, exit...\n";
        return;
    }

	open my $ofh, "> $ofile" or die;
	foreach (@arr_dir)  {
        if (-d $_)  {
			my $dt = DateTime->from_epoch( epoch => my_ftime($_) );
			if ( is_older_than_one_month($dt) )  {
				#print "===> ".$_.": ".$dt->ymd . ' ' . $dt->hms."\n";
            	my $cmd = sprintf("%s %s\n", $rmcmd, $_);
				print $cmd;
				print $ofh $cmd;
			} else  {
				#print $_.": ".$dt->ymd . ' ' . $dt->hms."\n";
			}
		}
	}
	close $ofh;

	print STDERR "TIP: may run $ofile directly to clear old directories\n";
}

main;

