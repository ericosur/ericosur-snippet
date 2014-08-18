#!/usr/bin/perl
=pod

=head1 NAME

tips.pl

=head1 AUTHOR

2006/12/27 by ericosur

=head1 NOTE

in-place perl string assignment
=cut

$a =<<LONGSTRING;
a b c d e f g
h i j k l m n
o p q r s t u
LONGSTRING

print $a;

# print a random number from 0 to 255 integer
print "random: ", int(rand(256)) . "\n";

# file test -X may use _ to repeat
print "Can do $0\n" if -r $0 || -w _ || -x _;

=pod

use pl2bat to make a perl script into batch file
=cut
