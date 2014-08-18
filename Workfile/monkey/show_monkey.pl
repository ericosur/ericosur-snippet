#!/usr/bin/perl

use strict;

sub main()
{
    my $cmd;

    my @files = glob("*_monkey.txt");
    foreach my $ff (@files) {
        # show file name
        printf("==========> %s:\n", $ff);
        # show fingerprint
        $cmd = sprintf("grep -A1 \"ro.build.fingerprint\" %s", $ff);
        system $cmd;
        # grep number of sending events
        print "event number:\t";
        $cmd = sprintf("grep \"^:\" %s | wc -l", $ff);
        #print $cmd,"\n";
        system $cmd;
        # grep if monkey finished
        print "if monkey finish?\n";
        $cmd = sprintf("grep \"Monkey finished\" %s", $ff);
        system $cmd;
    }
}

main;
