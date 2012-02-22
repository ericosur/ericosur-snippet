#!/usr/bin/env perl

=pod

=head1 NOTE

To calculate a power modulus.
Use bigint is unbelievable slow to calculate.
Use C<Math::BigInt> instead;

=cut

use bigint lib => 'Math::BigInt';

$vv = 104857 ** 32768 % 4294;
print $vv;
