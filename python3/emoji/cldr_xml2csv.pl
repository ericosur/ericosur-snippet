#!/usr/bin/env perl
#
# read en.txt which tailored from en.xml
# and output to stdout (as cldr.csv)
#


use strict;

my $fn = 'en.xml';
my $ofn = 'cldr.csv';
open my $fh, $fn or die;
open my $ofh, "> $ofn" or die;
my $cp;
my $an;
my $tc = 0;
my $mc1 = 0;
my $mc2 = 0;
while (<$fh>) {
    s/[\r\n]//;
    $tc ++;
    if ( m/^\s+<annotation cp="([^"]+)">(.+)<\/annotation>$/ ) {
        $mc1 ++;
        $cp = $1;
        printf $ofh "\"%s\",\"%s\",", $cp, $2;
    }
    if ( m/^\s+<annotation cp="([^"]+)" type="tts">(.+)<\/annotation>$/ ) {
        $mc2 ++;
        printf $ofh "\"%s\"\n", $2;
    }

}

close $fh;
printf STDERR "read from %s, write to %s\n", $fn, $ofn;
printf STDERR "tc: %d\nmc1: %d\nmc2: %d\n", $tc, $mc1, $mc2;