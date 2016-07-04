#!/usr/bin/env perl
#
# convert time stamp into elapsed seconds
# search for:
# [21:00:06.808] W: yoseui starting...
# replace to:
# [12345678] W: yoseui starting...
#

use strict;

my ($hh,$mm,$ss) = ();
my $sec;

# use STDIN
while (<STDIN>) {
    s/[\r\n]//;
    if ( m/\[
        (\d\d):         # hour
        (\d\d):         # minute
        (\d\d\.\d\d\d)  # seconds
        \]/x
    ) {
        $sec = 0.0;
        ($hh, $mm, $ss) = ($1, $2, $3);
        $sec = ($hh*60.0 + $mm)*60.0+$ss;
        printf("[%.3f]%s\n", $sec,$');
    }
}
