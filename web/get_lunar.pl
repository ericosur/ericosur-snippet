#!/usr/bin/perl
#
# -*- coding: utf-8 -*-
#
# get lunar date of today

use strict;
use warnings;

use WWW::Mechanize;
use Encode qw(from_to encode decode);

sub show_lunar()
{
	my $url = 'http://tw.news.yahoo.com/';
	my $mech = WWW::Mechanize->new();
	$mech->get($url);
	my $html = $mech->content();
	my $msg = "null";
#
# get rip off messy stuff
#
	$html =~ s/[\r\n]//g;	# 變成一長行
	$html =~ s/\<[^\<]+\>//g;	# 可以把大部份的 tag 都去掉

# 農曆 (己丑) 三月十三日 09:30 更新
	if ( $html =~ m/(農曆.+日) \d+:/ )  {
		$msg = $1;
	}

	return $msg;
}

sub get_lunarday()
{
	my $msg = show_lunar();
	if ($^O eq 'MSWin32')  {
		from_to($msg, "utf-8", "big5");
		return $msg;
	}
}

print get_lunarday();
