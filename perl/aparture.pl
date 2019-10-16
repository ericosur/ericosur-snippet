#!/usr/bin/perl
=pod

=head1 NOTE

列出光圈值

使用幾個 re 來作截斷數字的動作

2007/03/21 by ericosur
=cut

use strict;
use warnings;


my $val = sqrt(2);
my $f = 1.0;

my $p1 = qr{
		^(\d+)\.00\d*
#		(?{ print "p1: [$`<$&>$']\t" })
	}x;

my $p2 = qr{
		^(\d\.[^0])\d+
#		(?{ print "p2: [$`<$&>$']\t" })
	}x;

my $p3 = qr{
		^(\d{2,})\.\d+
#		(?{ print "p3: [$`<$&>$']\t" })
	}x;

for (my $i = 0.0; $i < 14; $i += 1)
{
	$f = $val ** $i;
	my $g = sprintf "%.2f", $f;
	#$g =~ s/(\d+\.\d\d)\d+/$1/;
	print "$i => [$g]\t";

	my $tmp = $g;
	print $1 if ( $tmp =~ $p3 or $tmp =~ $p1 or $tmp =~ $p2 );
	print "\n";
}

exit 1;
