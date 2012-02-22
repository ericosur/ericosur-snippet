#!/usr/bin/perl
#
# to show ascii code for a string
#

my $a = $ARGV[0] || '-';
#$a = "+886229122929-8432-6171 z";
print STDERR "USAGE: $0 <str>\tOR\nfrom STDIN\n" if $a eq '-';

$a = <> if ($a eq '-');

for (split //, $a)  {
	printf "%02x:", ord($_),"\n";
}
print "\n";
