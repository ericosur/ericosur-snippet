#!/usr/bin/perl

#
# Sum up the time length of mp3 files with MP3-Info
#

use strict;
use MP3::Info;

my @files = glob("*.mp3");
my $total_min = 0;
my $total_sec = 0;

unless (@files)  {
	warn "empty ?";
	exit;
}

foreach my $ff (@files)  {
	my $mp3 = MP3::Info->new($ff);
	my $len = $mp3->time;
	printf "%s\t%s\n", $ff, $len;
	$len =~ m/(\d+):(\d+)/;
	my ($min, $sec) = ($1, $2);
	$total_min += $min;
	$total_sec += $sec;
}

# total time length in seconds
my $unified_sec = $total_min * 60 + $total_sec;
printf "total second = %d\nOr %d:%d\n", $unified_sec, $unified_sec/60, $unified_sec%60;
