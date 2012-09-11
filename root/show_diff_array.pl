#!/usr/bin/perl
#!/bin/perl

# 比對兩個 file list 把其他差異的 element 印出來
#
# 用 friendly flickr 下載 big 圖，列出 file list => big.txt
# 下載 thumbnail 圖，列出 th.txt
# 由於有的圖被縮小，所以沒有 big format 的圖
#
#
# 參考 http://www.rocketaware.com/perl/perlfaq4/How_do_I_compute_the_difference_.htm
#
# 2007/10/03 by ericosur

use strict;
use warnings;


open TH, "th.txt" or die;
open BIG, "big.txt" or die;

my @th = <TH>;		# more items
my @big = <BIG>;	# less items
my @union,;
my @intersection;
my @difference;
my %count;
my $element;

    @union = @intersection = @difference = ();
    %count = ();

    foreach $element (@th, @big) { $count{$element}++ }
    foreach $element (keys %count) {
        push @union, $element;
        push @{ $count{$element} > 1 ? \@intersection : \@difference }, $element;
    }

close TH;
close BIG;

foreach (@difference)
{
	print $_;
}
