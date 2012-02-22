#!/usr/bin/perl

use strict;
use warnings;

=pod
    * pos SCALAR
    * pos

      Returns the offset of where the last m//g search left off for the
      variable in question ($_ is used when the variable is not specified).
      Note that 0 is a valid match offset. undef indicates that the search
      position is reset (usually due to match failure, but can also be
      because no match has yet been performed on the scalar). pos directly
      accesses the location used by the regexp engine to store the offset,
      so assigning to pos will change that offset, and so will also influence
      the \G zero-width assertion in regular expressions. Because a failed
      m//gc match doesn't reset the offset, the return from pos won't change
      either in this case. See perlre and perlop.
=cut

my $str = "01234here1111122222there33333";
my $pat = qr([a-z]+);
print "str: $str\n";
print "pat: $pat\n";

while ( $str =~ m/($pat)/g )  {
	my $ss = $1;
	my $pp = pos($str);
	my $ll = length($1);
	my $beg = $pp - $ll;
	printf "match: (%s) at beg(%d) pos(%d) len(%d)\n", $ss, $beg, $pp, $ll;
	#print $',"\n";
}
