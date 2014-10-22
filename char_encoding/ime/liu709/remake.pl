#!/usr/bin/perl

use strict;

sub process_file($$)
{
    my $ifn = shift;
    my $ofn = shift;
    my $cnt = 0;

    print STDERR ">>>>>>>>>> in: $ifn\n";
    open my $ifh, $ifn or die "$!";
    open my $ofh, "> $ofn" or die;
    binmode($ifh, ":utf8");	# read it as utf8 encoding
    binmode($ofh, ":utf8"); # output it as utf8

    while (<$ifh>) {
        if (m/(\S+)\s+(\S+)/) {
            print $ofh "$1\t$2\n";
            ++ $cnt;
            print "$cnt\r";
        }
    }

    print "\n";
    close $ifh;
    close $ofh;
}

sub main()
{
    process_file('liu-uni.txt', 'out/liu-uni.lime');
    process_file('liu-uni2.txt', 'out/liu-uni2.lime');
    process_file('liu-uni3.txt', 'out/liu-uni3.lime');
    process_file('liu-uni4.txt', 'out/liu-uni4.lime');
}

main;
