#!/usr/bin/perl

=pod

=head1 DESCRIPTION

A simple demo of strftime()

=head1 NOTE

The strftime() output will be various from locale settings.
=cut

use strict;
use warnings;
use POSIX qw(strftime);


my $local_str = strftime "%a %b %e %H:%M:%S %Y", localtime;
# or for GMT formatted appropriately for your locale:
my $gm_str = strftime "%a %b %e %H:%M:%S %Y", gmtime;
# julian date
my $doy = strftime "%j", localtime(time);

printf "localtime:\n%s\n   gmtime:\n%s\n", $local_str, $gm_str;
printf "day of year:\n%s\n", $doy;

#
# print ''Sun Mar 16 20:47:57 2008''
#
print "scalar localtime:\n";
print scalar localtime,"\n";
