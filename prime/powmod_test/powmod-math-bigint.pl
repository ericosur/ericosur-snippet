#!/usr/bin/env perl

=pod

=head1 NOTE

Use C<Math::BigInt> to calculate power modulus.
Please compare it to C<powmod-bigint.pl>.

=cut

use Math::BigInt;

my $x = Math::BigInt->new('104857');
$x->bmodpow(32768, 4294);

print $x,"\n";
