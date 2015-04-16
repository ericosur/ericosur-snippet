#!/usr/bin/env perl

# call nmap -sP and filter out unnecessary lines

use strict;
use v5.010;

sub main()
{
    my $range = $ARGV[0] // "192.168.43.1-253";
    my $cmd = sprintf("sudo nmap -sP %s", $range);
    print $cmd,"\n";
    my $ret = `$cmd`;   # take a while to scan

    my @arr = split(/\n/, $ret);
    foreach (@arr) {
        s/[\r\n]//;
        if (m/^Host is/ || m/^Starting/ || m/^Nmap done/) {
            next;
        } else {
            if (m/^Nmap/) {
                s/Nmap scan report for/ip: /;
                print $_;
            } else {
                print "    $_\n";
            }
            #print "\n";
        }
        print "\n";
    }
    #print @arr;
}

main;
