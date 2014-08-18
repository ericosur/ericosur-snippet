#!/usr/bin/perl

use strict;
use warnings;
use utf8;

#
# 因為 $ifile 所有資料都擠在一行裡面，這個 script把這個
# 資料作一行一筆的切割，產出 gb2312-normalized-pinyin.txt
#
my $ifile = 'gb2312_pinyin.txt';
my $ifh;

open $ifh, $ifile or die "$!";

while (<$ifh>)  {
	next if m/^#/;
	s/(([a-z0-9]+\s))+/$1\n/g;
	print;
}

close $ifh;
