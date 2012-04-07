#!/usr/bin/perl
=pod

=head1 DESCRIPTION

demo to use Data::UUID to generate UUID

=cut

use strict;
use warnings;
use 5.010;
use Data::UUID;

my $ug = new Data::UUID;
my $uuid1 = $ug->create();
my $uuid2 = $ug->create_from_name("home", "ericosur");
my $res = $ug->compare($uuid1, $uuid2);
say "compare uuid1 and uuid2: $res";
my $str = $ug->to_string($uuid1);
say $str;
my $uuid = $ug->from_string($str);

say $ug->to_string($uuid2);

