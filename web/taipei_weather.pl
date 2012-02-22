#!/usr/bin/perl
#
# -*- coding: utf-8 -*-
#
# use yahoo weather to get weather of taipei city
#

use strict;
use warnings;

use WWW::Mechanize;
use Encode qw(from_to encode decode);

# make string more beautiful
sub format_str($)
{
	my $str = shift;
	$str =~ s/&deg;/度/;	# change &deg; to ''度''
	$str =~ s/(\s+)/\t/g;
	$str =~ s/(\d+%)/降雨機率$1/;	# add description for percent
	return $str;
}

sub show_weather($)
{
	my $url = shift;
	my $mech = WWW::Mechanize->new();
	$mech->get($url);
	my $html = $mech->content();

#
# get rip off messy stuff
#
	$html =~ s/\r//g;
	$html =~ s/\n//g;	# 變成一長行
	$html =~ s/\<[^\<]+\>//g;	# 可以把大部份的 tag 都去掉

	#print STDERR $html;	# for debugging

	my ($ptime, $vtime, $t1, $t2);
	my $msg;

	$ptime = $1 if ($html =~ m/(發.*)有/);
	$vtime = $1 if ($html =~ m/(有[^\s]+)/);
	#print "$ptime\n$vtime\n";
	$msg = "$ptime\n$vtime\n";

	$t1 = $1 if ($html =~ m/(台北市.*)基/);
	$t2 = $1 if ($html =~ m/(台北地區.*)桃/);
	$t1 = format_str($t1);
	$t2 = format_str($t2);
	$msg = $msg . "$t1\n$t2\n";

	# if win32, transcode to big5 for poor cmd terminal
	if ( $^O eq 'MSWin32' )  {
		$msg = encode ("big5", decode("UTF-8", $msg));
	}

	return $msg;
}


sub twoday()
{
	my @url = ('http://tw.weather.yahoo.com/today.html',
			'http://tw.weather.yahoo.com/tomorrow.html');
	my $msg;

	foreach (@url)  {
		$msg = $msg . show_weather($_);
	}

	return $msg;
}

print twoday();
