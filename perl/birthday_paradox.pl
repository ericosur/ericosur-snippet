#!/usr/bin/perl

# use brute-force to try brithday paradox

use strict;
use warnings;
use v5.10;

# birthday from 1 to 365
my $min = 1;
my $max = 365;

# $rr is reference of array
# $cnt is the size to fill random numbers
sub gen_rand($$)
{
    my ($rr, $cnt) = @_;

    @$rr = ();
    # fill @$rr with ($min, $max)
    for (my $i = 0; $i < $cnt; ++$i)  {
        push @$rr, (int(rand($max)) + $min);
    }

    return @$rr;
}

# $rr: reference of array
# return 0 if not found, 1 if found duplicated value
sub check_dup($)
{
    my $rr = shift;
    my %check = ();
    my $found_dup = 0;

    foreach my $n (@$rr)  {
        $check{$n} ++;
    }

OUTTER:
    foreach my $k (keys(%check))  {
        if ($check{$k} > 1)  {
            $found_dup = 1;
            last OUTTER;
        }
    }

    return $found_dup;
}

# in: $target_possibility
sub try_group_size($)
{
    my $target_possibility = shift;
    my $group_size = 2;  # size of group start from
    my $largest_size = 100;
    my $repeat = 100000;    # repeat times
    my $collide = 0;    # total number to found duplicated birthday
    my @arr;

GROUP_LOOP:
    for (my $size = $group_size; $size < $largest_size; ++$size)  {
        $collide = 0;
        for (my $i=0; $i<$repeat; ++$i)  {
            gen_rand(\@arr, $size);
            my $match = check_dup(\@arr);
            if ($match > 0)  {
                $collide ++;
            }
        }
        my $poss = ($collide/$repeat)*100.0;
        printf("%d,%d,%d,%f\n", $collide, $repeat, $size, $poss);
        if ($poss >= $target_possibility)  {
            last GROUP_LOOP;
        }
    }

}

sub main()
{
    printf("collide,total,size,percentage\n");
    try_group_size(100); # how large of the group size to get 50% collision?
}

main;
