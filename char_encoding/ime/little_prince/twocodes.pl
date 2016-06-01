#!/usr/bin/env perl

use strict;
use Storable;
use utf8;
use Encode qw(from_to);

my %ime = ();

sub find_twocodes()
{
    my $f = "table.txt";
    open my $fh, $f or die;
    while ( <$fh> ) {
        s/[\r\n]//g;
        if ( m/^([a-zA-Z]{2})\s+(\S+)$/ ) {
            my ($kk, $vv) = ($1, $2);
            #printf("%s<--->%s\n", $kk, $vv);
            if ($ime{$kk}) {
                my $ra = $ime{$kk};
                push @$ra, $vv;
            } else {
                my @wds = ($vv);
                $ime{$kk} = \@wds;
            }
        }
    }
    close $fh;

    #printf("size: %d\n", scalar(keys(%ime)));
}

sub mydump($)
{
    my $rh = shift;
    my $total = 0;
    my @freq = ();

    for my $kk (sort keys(%$rh)) {
        ++$total;
        if ( ref $rh->{$kk} eq 'ARRAY' ) {
            $freq[0] ++;
            my $rarr = $rh->{$kk};
            my $code = scalar(@$rarr);
            $freq[$code] ++;
            if ($code) {   # list char has more than 12 combination
                from_to($kk, "UTF8", "BIG5");
                print $kk," ";
                foreach (@$rarr) {
                    print $_," ";
                }
                print "\n";
            }
        } else { # scalar
            $freq[0] ++;
            # print keydef > 1
            my $len = length($kk);
        }
    }

    if ($freq[0] > 0) {
        for (my $i=0; $i<scalar(@freq); $i++)  {
            my $out = sprintf("freq[%d]: %d\n", $i, $freq[$i]);
            print STDERR $out;
        }
    }
}

sub main()
{
    find_twocodes();
    mydump(\%ime);
}

main;
