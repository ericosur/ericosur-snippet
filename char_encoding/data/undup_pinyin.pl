#!/usr/bin/perl
use strict;

#
# 讀入 pinyin 的資料表
#
my $ifile = q(gb2312-normalized-pinyin.txt);
my $ifh;
my %pinyin = ();
my $cnt = 0;

open $ifh, $ifile or die;
LINE:
while (<$ifh>)  {
	if (m/^$/ or m/^#/)  {
		next LINE;
	}
	if (m/\s+([a-z]+)/)  {
		$pinyin{$1} ++;
		++ $cnt;
	}
}
close $ifh;

my $foo = keys %pinyin;
print "number of unique keys from $ifile ==> $foo\n";
print "total read items ==> $cnt\n";
my @k1 = sort keys %pinyin;

#
# 這個表格從香萃 utility 找出來的 (似乎不全？)
#
my $if2 = q(pinyin-keys.txt);
my $ifh2;
my %pk = ();

open $ifh2, $if2 or die;
while (<$ifh2>)  {
	m/^([a-z]+)\|/;
	$pk{$1} ++;
}
close $ifh2;

my $bar = keys %pk;
print $bar,"\n";
print "number of unique keys from $if2 ==> $bar\n";
my @k2 = sort keys %pk;

#
# 取得聯集，交集及差集
#
	my (@union, @intersection, @difference);
    @union = @intersection = @difference = ();

    my %count = ();

    foreach my $elm (@k1, @k2)  {
    	$count{$elm}++
    }
    foreach my $element (keys %count) {
        push @union, $element;
        push @{ $count{$element} > 1 ? \@intersection : \@difference }, $element;
    }

foreach (@difference)  {
	print $_,"\n";
}

print "union: ", scalar @union,"\n";
