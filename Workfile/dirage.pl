#!/usr/bin/perl
use strict;
use warnings;
use 5.010;

#use DateTime;
use Date::Calc qw(:all);

sub get_file_date($)
{
	my $file = shift;

	my ($atime,$mtime,$ctime) = (stat($file))[8..10];
	#my $a_time = localtime($atime);
	my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($mtime);
	#my $c_time = localtime($ctime);

	$year += 1900;
	$mon += 1;
	return ($mday,$mon,$year);
}


# in: (year, month, day)
sub get_date_delta($$$)
{
	my ($dy,$dm,$dd) = @_;
	my ($ty, $tm, $tday) = Today();

	#say $dy, $dm, $dd;
	my $delta = Delta_Days($ty, $tm, $tday, $dy, $dm, $dd);

	#print $delta,"\n";
	return $delta;
}


sub main()
{
	my @arr_dir = glob("proj_*");

	foreach my $dd (@arr_dir)  {
		my ($mday, $mon, $year) = get_file_date($dd);
		printf("%s: %d-%d-%d\t", $dd, $mday, $mon, $year);
		print get_date_delta($year,$mon,$mday),"\n";
	}

}

main;

