#!/usr/bin/env perl

use strict;
use utf8;

sub listChar($)
{
    my $f = shift;
    open my $fh, $f or die;
    while (<$fh>) {
        s/[\r\n]//g;
        my $r = $_;
        while ( $r =~ m/(\S+)\s*=\s*(\S+)/g ) {
            print $1;
        }
    }
    close $fh;
}

sub sep
{
    my $title = shift;
    if ($title) {
        print '-' x 20, $title;
        print '-' x 40, "\n";
    } else {
        print '-' x 70, "\n";
    }

}

sub main()
{
    #my @tables = ("t1.txt", "t2.txt", "t3.txt");
    my @tables = ("t7.txt");

    for my $f (@tables) {
        sep($f);
        listChar($f);
        sep();
    }
}

main;
