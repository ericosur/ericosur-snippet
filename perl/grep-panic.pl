#!/usr/bin/env perl
use strict;
use warnings;
use v5.10;
use Data::Dump qw(dump);

=pod

=head1 NOTE

Test code from http://gugod.org/2009/09/i-just-made-perl-panic.html

=cut

sub add3 { $_ + 3 };
dump( map { add3 } (1 .. 3) );
dump( map &add3, (1 .. 3) );

my $add2 = sub { $_ + 2 };
dump( map &$add2, (4 .. 6) );
dump( map $add2->($_), (4 .. 6) );
# map $add2 (1 .. 3);	# grep panic

