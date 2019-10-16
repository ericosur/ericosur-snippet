#!/usr/bin/env perl
#
# from:
# https://perlmaven.com/how-to-sort-a-hash-in-perl
#

use strict;


my %planets = (
   Mercury => 0.4,
   Venus   => 0.7,
   Earth   => 1,
   Mars    => 1.5,
   Ceres   => 2.77,
   Jupiter => 5.2,
   Saturn  => 9.5,
   Uranus  => 19.6,
   Neptune => 30,
   Pluto   => 39,
   Charon  => 39,
);

print '-' x 20, " original hash\n";
foreach my $name (keys %planets) {
    printf "%-8s %s\n", $name, $planets{$name};
}
print '-' x 20, " sort by keys\n";
foreach my $name (sort keys %planets) {
    printf "%-8s %s\n", $name, $planets{$name};
}
print '-' x 20, " sort by values\n";
# sort hash by values, 2nd by keys
foreach my $name (sort { $planets{$a} <=> $planets{$b} or $a cmp $b } keys %planets) {
    printf "%-8s %s\n", $name, $planets{$name};
}
