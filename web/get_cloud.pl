#!/usr/bin/env perl
=pod

=head1 NOTE

Use b<curl> to fetch satellite cloud pictures from CWB.
Reference from http://gugod.org/2009/08/-curl.html

=cut

use strict;

sub clear_up()
{
	# remove files of which size is smaller than 1024
	my @fl = glob('*.jpg');
	foreach my $ff (@fl)  {
		my $sz = -s $ff;
		if ($sz < 1024)  {
			unlink $ff;
		}
#	printf "%s: %d\n", $ff, (-s $ff);
	}
}

sub compose_cmd()
{
	# get date of today
	my (undef,undef,undef,$day,$month,$year,undef,undef,undef) = localtime;
	$year += 1900;
	$month += 1;

my $lstr =<<EOL;
curl -O 'http://www.cwb.gov.tw/V6/observe/satellite/Data/HS1P/HS1P-%04d-%02d-%02d-[00-23]-{00,30}.jpg'
EOL

	# compose the cmd string
	my $cmd = sprintf($lstr, $year, $month, $day);
	print $cmd,"\n";
	return $cmd;
}

sub main()
{
	my $cmd = compose_cmd();
	system $cmd;
	clear_up();

	# TODO: make it into gif animation?
}

main;
