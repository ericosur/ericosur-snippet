#!/usr/bin/perl
#
# demo for using package 'bigrat'
#
# 2007/01/10 by ericosur
# 2008/02/19 reviewed
# see git log for history

use strict;
use warnings;

use bigrat;

# you may see it does not work
sub demo()
{
    my $sum = 0;
    for my $ii (2..9) {
        my $v = 1/$ii;
        $sum += $v;
    }
    print "sum = ", $sum, "\n";
}

sub easy()
{
	print "1/2 + 1/3 + 3/4 = ", 1/2 + 1/3 + 3/4, "\n";

	my @a = (1/7, 1/8, 1/3);
	my $sum = 0;
	foreach (@a)  {
		$sum += $_;
	}
	print join(' + ', @a), " = ";
	print $sum,"\n";
}

sub main()
{
    easy();
    demo();
}

main;

