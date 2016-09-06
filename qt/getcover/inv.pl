#!/usr/bin/env perl

use strict;

my $MAX = 3;
my $fn = "list.txt";
open my $fh, $fn or die;
my $cmd;
my $rootdir = q(/home/rasmus/Music/);
my $cnt = 0;

while ( <$fh> ) {
    s/[\r\n]//;
    s/\.\//$rootdir/;
    my $fn = $_;
    if ( -e $fn) {
        my $cmd = sprintf("./getcover \"%s\"", $fn);
        system $cmd;
        $cnt ++;
    }
    last if ($cnt >= $MAX);
}
close $fh;
