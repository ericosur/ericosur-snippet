#!/usr/bin/env perl

# shuffle name of mp3

use strict;

sub get_rand()
{
    my $n = 399;
    # 0 to n-1
    my $prefix = sprintf("%04d", int(rand($n)));
    return $prefix;
}

sub main()
{
    my @ar = glob("*.mp3 *.MP3");
    my %hh = ();

    foreach (@ar) {
        my $ofn = $_;
        my $base_fn = "";

        if ( m/^\d{4}_.*$/ ) {
            s/^\d{4}_(.*)$/$1/;
            $base_fn = $_;
            printf("rename \"%s\" \"%s\"\n", $ofn, $base_fn);
            rename $ofn, $base_fn;
        }
    }
}

main;
