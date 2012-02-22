#!/usr/bin/perl

use strict;
use 5.010;

sub check($)
{
    my $val = shift;
    if ( ($val - 1) % 6 == 0 )  {
        return '-';
    }
    if ( ($val + 1) % 6 == 0 )  {
        return '+';
    }
    return 0;
}

sub main()
{
    my $file = "prime_100k.txt";
    open my $fh, $file or die;

    my $cnt = 0;
    while ( <$fh> )  {
        s/[\r\n]//;
        if ( m/^(\d+)\s+(\d+)/ )  {
            ++ $cnt;
            last if ($cnt > 2000);
            next unless $2;
            my $prime = $2;
            my $ret;
            $ret = check($prime);
            print $ret;
        }
    }
    close $fh;
}

main;
