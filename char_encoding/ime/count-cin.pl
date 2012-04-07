#!/usr/bin/perl

#
# 顯示 cin 表格內：
#    cname 欄位
#    chardef 的數量
#    不重複的鍵值數量
#    不重複出字的數量
#

use strict;
use File::DosGlob 'glob';

my $arg = $ARGV[0] || "*.cin";
my $flag;
my $cnt;
my (%left, %right) = ();

my @files = glob $arg;
#foreach my $fname (@files)  {
#    print "$fname\n";
#}

foreach my $ff (@files)  {
	next if not -e $ff;
	print "read from $ff\n";
	open my $ifh, $ff or die "$!";
	$flag = 0;
	$cnt = 0;
	%left = ();
	%right = ();
	while (<$ifh>)  {
		next if m/^#/;
		my $line = $_;
		if ( $line =~ m/%cname\s+(.*)/ )  {
			print "ime name: $1\t";
		}
		if ( $line =~ m/%chardef\s+begin/ )  {
			$flag = 1;
#			print "begin\n";
			next;
		}
		if ($flag == 1)  {
			++ $cnt;
			$line =~ m/^(\w+)\s(.*)/;
			$left{$1} ++ if $1;
			$right{$2} ++ if $2;
			next;
		}
		if ( $line =~ m/%chardef\s+end/ )  {
			$flag = 0;
#			print "end\n"
			next;
		}
	}
	close $ifh;
	print "char def: $cnt\n";
	print "unique in: ", scalar keys %left, "\t";
	print "unique out: ", scalar keys %right, "\n";
	print '-'x40,"\n";
}
