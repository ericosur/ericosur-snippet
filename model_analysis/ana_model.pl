#!/usr/bin/perl
#
# ana_model.pl
#
# take result from get_exif_model.pl and output a model statistics
#

use strict;

my $list = $ARGV[0] || "model.txt";
my %data = ();
my $count = 0;

open FH, $list or die;
print STDERR "input file: $list\n";

LINE:
while (<FH>)  {
	s/\n//;
	next LINE if m/^#/ or m/^$/;
	m["(.+)","(.+)"];

	my $camera = $2;

#	printf "%s\n", $2;
	++ $data{$camera};
	++ $count;
	print STDERR $count, "\r";
}
#print STDERR "\n";
close FH;

my $check_count = 0;	# to see whether I get through the whole list
sep();

# to sort the keys of hash and then output
my @sort_data = sort { $a cmp $b } keys %data;
for (@sort_data)  {
	printf "%s: %d\n", $_, $data{$_};
	$check_count += $data{$_};
}
sep();

printf "count: %d, check: %d\n", $count, $check_count;

sub sep
{
	print '-' x 40, "\n";
}
