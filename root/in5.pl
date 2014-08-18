#!/usr/bin/perl

#@ in5.pl
#@ just another stupid test for inputting strings from stdin
#@ oct 21 2004 by rasmus
#
#
print STDERR "input from stdin...\n";

for (1..5)  {
	<>;
	chomp;
	#print $_;
	print "$_ \\\n";
	#print "\n";
}
print "only the first 5 lines\n";

#
# maybe use ``head 5 -'' to replace it?
#
