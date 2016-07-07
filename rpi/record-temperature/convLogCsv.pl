#!/usr/bin/env perl

=pod

one record as:

0707 090012,1467853212,
Temp=27.0*  Humidity=58.0%

convert to:

1467853212,27.0,58.0

=cut

# input from STDIN
my $str;
my $now;
while (<STDIN>) {
    $now = "";
    $str = "";
    s/[\r\n]//;
    if ( m/^(\d+ \d+),(\d+),/ ) {
        $now = $2;
        print $now;
    }
    if ( m/^Temp=(\d+\.\d+)\*\s+Humidity=(\d+\.\d+)%/ ) {
        printf(",%s,%s\n", $1, $2);
    }
}
