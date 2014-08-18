#!/usr/bin/perl
#
# generate a file list from network drives
#
use strict;
use Benchmark ':hireswallclock';

my $debug = 0;

sub get_today()
{
	my (undef,undef,undef,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $today = sprintf "%04d%02d%02d", ($year+1900), ($mon+1), $mday;	# like 20071225

	return $today . 'list.txt';
}

sub main
{
	my $ofile = get_today();
	my @drive = qw(o q s u);	# from network drive O: Q: ...
	my $t0 = new Benchmark;		# benchmark start...

	foreach my $dd (@drive)  {
		my $cmd = "cmd /c dir /s/b $dd:\\ >> $ofile";
		print $cmd,"\n";
		system $cmd if not $debug;
	}

	my $t1 = new Benchmark;		# benchmark end...
	my $td = timediff($t1, $t0);

	print STDERR "\nThis action took: ", timestr($td),"\n";
}

main;
