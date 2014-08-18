#!/usr/bin/perl

use strict;

my @titles = (
#"Complete name",
"Format     ",
"Video",
"Format profile",
"Width",
"Height",
"Display aspect ratio",
"Audio",
"Format version",
"Bit rate     ",

);

sub sep()
{
    print '-' x 80, "\n";
}

sub grep_lines($)
{
    my $fn = shift;
    my $lcnt = 0;
    my $fcnt = 0;
    my $ln;
    open my $fh, $ofn or die;

    LOOP:
    while (<$fh>) {
        $lcnt ++;
        $ln = $_;
        foreach my $str (@titles) {
            #print $str;
            if ($ln =~ m/^Complete name   /) {
                sep();
                printf("%d: %s", $lcnt, $ln);
                $fcnt ++;
                next LOOP;
            } elsif ($ln =~ m/^$str/) {
                printf("%d: %s", $lcnt, $ln);
                next LOOP;
            }
        }
        #print "next.\n";
    }

    close $fh;
    print "fcnt: $fcnt\n";
}

sub main()
{
    my $fn = "1.txt";
    grep_lines($fn);
}

main;
