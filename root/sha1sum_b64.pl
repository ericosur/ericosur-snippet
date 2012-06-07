#!/usr/bin/perl

=pod

=head1 DESCRIPTION
Got one piece of base64 encoded string. Decode it and translate to
string form.

=cut

use strict;
use MIME::Base64;
use 5.010;

my $cmd;

# base64 encoded string
my $b64 = q(OAWJ/s2REfKhP6ysjVtVFyCGCO8=);
say "b64: ", $b64;
# after decoding, it would be binary form
my $b64_decode = decode_base64($b64);
$cmd = 'H' . (length($b64_decode) * 2);
# translate to array as string form
my @hex = unpack($cmd, $b64_decode);
say "in: ", join('',@hex);

my $sha1sum = q(380589fecd9111f2a13facac8d5b5517208608ef);
$cmd = 'H' . length($sha1sum);
# pack this string into binary form
my $binary = pack($cmd, $sha1sum);

# compare in binary form
if ( $binary eq $b64_decode ) {
	say "it's matched";
} else {
	say "not match";
}
