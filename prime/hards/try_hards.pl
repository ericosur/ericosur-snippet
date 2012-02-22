#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

my @hards = ();

sub test_num($)
{
    my $num = shift;
    my $res = $num % 6;
    if ( ($res == 5) || ($res == 1) )  {
        print "?";
        return 1;
    }
    else {
        return 0;
    }
}

sub load_hards()
{
    my $cnt = 0;
    open my $fh, "hards.txt" or die;
    while (<$fh>)  {
        next if ( m/^#/ );
        next if ( m/^$/ );
        s/[\r\n]//;
        die "$_ not a number!" unless ( m/\d+/ );
        push(@hards,$_);
        ++ $cnt;
    }
    say "cnt: $cnt";
}

sub main()
{
    my $cnt = 0;
    load_hards();
    foreach (@hards)  {
        my $res = test_num($_);
        ++$cnt if $res == 1;
    }
    say "true cnt: $cnt";
}

main;
