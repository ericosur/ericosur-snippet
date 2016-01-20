#!/usr/bin/perl

use strict;
my $file = "bztime.txt";

#16°20'S / 48°57'W Anápolis

sub dm2dd($)
{
    my ($dms) = @_;
    # print "dms=$dms\n";
    # 48 deg 17' 33.39"
    $dms =~ /(\d+)°(\d+)'(.)/;
    my ($degrees, $minutes, $heading) = ($1, $2, $3);
    my $dd = $degrees + $minutes/60.0;
    if ($heading eq "S" or $heading eq "W") {
        $dd = -$dd;
    }
    #print "$dd\n";
    return $dd;
}

sub test()
{
    my ($lat, $lng, $cty) = ();
    open my $fh, $file or die;
    while (<$fh>) {
        if ( m/(\S+) \/ (\S+) (\S.+)$/ ) {
            $lat = $1;
            $lng = $2;
            $cty = $3;
            printf("\"%s\",\"%s\",\"%s\"\n",dm2dd($lat),dm2dd($lng),$cty);
        }
    }
    close $fh;
}

sub main()
{
    test();
}

main;
