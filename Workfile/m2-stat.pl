#!/usr/bin/env perl

use strict;
use Term::ANSIColor;

my $file = '/tmp/m2status.txt';
my ($prj, $brh, $lne, $str) = ();
my $autogen = 0;

unless ( -e $file ) {
    my $cmd = "repo forall -p -c git status > " . $file;
    system $cmd;
    $autogen = 1;
}

open my $fh, $file or die;
while (<$fh>) {
    s/[\r\n]//;
    $lne = $_;
    next if ( m/^\s/ );
    if ( m/^project (\S+)$/ ) {
        $prj = $1;
        next;
    }
    if ( m/On branch (\S+)$/ ) {
        $brh = $1;
        if ($brh ne 'lc-200') {
            print color 'bold red';
            printf "AWARE! not at lc-200\n";
            print color 'reset';
        }
        printf "[%s] is on branch %s\n", $prj, $brh;
    }
    if ( m/(ahead|behind)/ ) {
        print color 'bold red';
        printf "[%s]: %s\n", $prj, $lne;
        print color 'reset';
        next;
    }
    if ( m/^(Changes|Untracked)/ ) {
        print color 'bold red';
        $str = $1;
        printf "[%s]: has %s\n", $prj, $str;
        print color 'reset';
        next;
    }

}
close $fh;

if ($autogen) {
    unlink $file;
}