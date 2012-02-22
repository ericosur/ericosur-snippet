#!/usr/bin/perl
#!/bin/perl

# ����� file list ���L�t���� element �L�X��
#
# �� friendly flickr �U�� big �ϡA�C�X file list => big.txt
# �U�� thumbnail �ϡA�C�X th.txt
# �ѩ󦳪��ϳQ�Y�p�A�ҥH�S�� big format ����
#
#
# �Ѧ� http://www.rocketaware.com/perl/perlfaq4/How_do_I_compute_the_difference_.htm
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
