#!/usr/bin/perl

use strict;

sub main()
{
    my $cmd;

    my @files = glob("*_monkey.txt");
    foreach my $ff (@files) {
        $cmd = sprintf("grep \"Sending\" %s | wc -l", $ff);
        print $cmd,"\n";
        system $cmd;
    }
}

main;

