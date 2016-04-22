#!/usr/bin/env perl
#
# alog.pl
# read all fisher*.log and output a csv for digit counts
# should run fisher tester first
#
use strict;

my %hh = ();

sub read_log($)
{
    my $f = shift;
    open my $fh, $f or die;
    %hh = ();
    while (<$fh>) {
        s/[\r\n]//;
        $hh{$_} ++;
    }
    close $fh;

    foreach my $kk (sort { $a<=> $b} keys %hh) {
        printf("\"%s\", ", $hh{$kk} );
    }
}

sub main()
{
    print<<EOL;
"position", "digit0", "digit1", "digit2", "digit3", "digit4", "digit5", "digit6", "digit7", "digit8", "digit9",
EOL

    my @arr = glob("fisher*.log");
    foreach my $ff (@arr) {
        printf("\"%s\", ", $ff);
        read_log($ff);
        printf("\n");
    }
}

main;
