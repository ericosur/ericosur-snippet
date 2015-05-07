#!/usr/bin/env perl

# shuffle name of mp3

use strict;

sub get_rand()
{
    my $n = 200;
    # 0 to n-1
    my $prefix = sprintf("%04d", int(rand($n)));
    return $prefix;
}

sub main()
{
    my @ar = glob("*.mp3");
    my %hh = ();

    foreach (@ar) {
        my $ofn = $_;
        my $nfn = "";
        my $base_fn = "";

        s/^\d{4}_(.*)$/$1/;
        $base_fn = $_;

        my $rn = 0;
        while (1) {
            $rn = get_rand();
            if (defined($hh{$rn})) {
                printf("<%d>\n", $rn);
                next;
            } else {
                last;
            }
        }
        $hh{$rn} ++;

        $nfn = sprintf("%s_%s", $rn, $base_fn);
        printf("rename \"%s\" \"%s\"\n", $ofn, $nfn);
        rename $ofn, $nfn;
    }
}

main;
