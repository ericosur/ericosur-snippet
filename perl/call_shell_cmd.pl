#!/usr/bin/perl
#
# demo for using package 'Shell'
#
# 2007/01/10 by ericosur

use Shell qw(cal bc);

# call cal
my $cal = cal();
print $cal;

# call bc
my $bc = bc();
print $bc;
