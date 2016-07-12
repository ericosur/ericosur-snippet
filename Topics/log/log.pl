#!/usr/bin/env perl

sub log10 {
    my $n = shift;
    return log($n)/log(10);
}

sub main()
{
    my @vals = (1, 2.7182818284, 10, 100, 300);
    for my $vv (@vals) {
        printf("%.5f: %.5f -- %.5f\n", $vv, log($vv), log10($vv));
    }
}

main;
