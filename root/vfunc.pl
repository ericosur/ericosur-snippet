#!/usr/bin/perl
=pod

=head1 NOTE

similar to grep -in PATTERN
2006/12/27 by ericosur

=cut

use strict;
use warnings;

sub mygrep($$);

my $source;
my $line_num = 0;
my $count = 0;
my $pattern;

	die "vfunc.pl <source file>" unless ($ARGV[0]);
	$source = $ARGV[0];
#	$source =~ s(\\)(/)g;

	# change regex pattern if needed
	$pattern = qr(ARGV\[0\]);
#	$pattern = '^\w\s*' .
#		'([[A-Za-z0-9_]+\s+\**)' .
#		'([A-Za-z0-9_ \*]+)\s+([a-zA-Z0-9_]+)(\(.*\))\s*;$';


	open FH, "< $source" or die "cannot open $source: $!\n";

LINE:
while ( <FH> )
{
	$line_num ++;

	next LINE if ( /^\/\// );
#	next LINE if ( /^\s*$/ );

	mygrep($_, $pattern);

	last LINE if ($count >= 5);
}

print "\n$count matched\n";
close FH;

#print "function counted: " . $count . "\n";

sub mygrep($$)
{
	my $line = shift;
	my $pattern = shift;

	$line =~ s/\t+/ /g;

	if ( $line =~ /$pattern/ )
	{
		print $line_num . ": " . $line;

		print "\t(1)$1\t" if ($1);
		print "(2)$2\t" if ($2);
		print "(3)$3\t" if ($3);
		print "(4)$4\n" if ($4);

		#print $line_num . ": " . $1 . "\n";
		$count ++;
	}
}
