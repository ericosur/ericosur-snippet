#!/usr/bin/perl
#
# wcl.pl
#
#
# July 17 2002 by ericosur
#   from <stdin>
#   �p�⦳�X�� (�]�A�ťզ�)
#

use strict;

print STDERR "simulate 'wc -l' behavior, input from stdin\n";

my $line = 0;

while ( <STDIN> )  {
    $line ++;
}

print STDERR "total lines: $line\n";
