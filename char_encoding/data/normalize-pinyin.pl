#!/usr/bin/perl

use strict;
use warnings;
use utf8;

#
# �]�� $ifile �Ҧ���Ƴ����b�@��̭��A�o�� script��o��
# ��Ƨ@�@��@�������ΡA���X gb2312-normalized-pinyin.txt
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
