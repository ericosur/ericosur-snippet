#!/usr/bin/perl

# nonsense for-loop for constructing lots hash pair
#
# 2006/12/27 by ericosur

for $i (0 .. 600-1)  {
	%x = ();
	for $j (0 .. 100-1)  {
		$x{$j} = $i;
		print $x{$j};
	}
}
