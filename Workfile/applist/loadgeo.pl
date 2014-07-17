#!/usr/bin/perl

use strict;

#my $geo = "geo43r1.csv";
my $geo = "geo44r1.csv";

sub load_geo($)
{
    my $f = shift;
    my ($apk, $pkg) = ();
    my $cnt = 0;

    open my $fh, $f or die;
    while (<$fh>) {
        s/[\r\n]//g;
        if ( m/^([^,]+),([^,]+)/ ) {
            ++ $cnt;
            ($apk, $pkg) = ($1, $2);
            printf("%s - %s\n", $apk, $pkg);
        }
    }
    close $fh;
    print "cnt: $cnt\n";
}

sub main()
{
    load_geo($geo);
}

main;

