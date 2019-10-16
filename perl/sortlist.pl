#!/usr/bin/perl
#
# a demo to sort a random string list
#

=pod

=head1 NAME

sortlist.pl

=head1 SYNOPSIS

sortlist.pl
And result output to STDOUT.

=head1 DESCRIPTION

This script generates a list of random strings, and
demo how to sort it by using C<sort()> and C<cmp>.

B<Text::Lorem> would be ultilized if installed. Otherwise,
a simple string generator function would be called.

=cut

use strict;
use warnings;

# max number for string list
my $str_number = 8;

#
# To test Text::Lorem installed or not
#
my $no_lorem;
eval { require Text::Lorem };
$no_lorem = 1 if $@;

#
# generated data would be stored into array
#
# [in] ref to array
sub generate_test_data($)
{
	my $aref = shift;
	my $lower = ord('a');
	my $range = ord('z') - ord('a');
	my $str_len;

	my $str;

	#printf "%d\t%d\t", $lower, $range;
	for (my $i = 0; $i < $str_number; ++ $i)
	{
		$str = "";
		$str_len = int(rand(15))+3;	# random length
		for (my $j = 0; $j < $str_len; ++ $j)
		{
			my $ch = chr(int(rand($range)+$lower));
			#print $ch;
			$str = $str . $ch;
		}
		#printf "<%s>\n", $str;
		push @$aref, $str;
	}
}

sub generate_lorem_data($)
{
	my $aref = shift;
	my $text = Text::Lorem->new();
	my $words;

	$words = $text->words($str_number);
	@$aref = $words =~ m/\w+/g;
}

#
# main procedure here
#

my @array = ();

if ($no_lorem)  {
	generate_test_data(\@array);
}
else  {
	generate_lorem_data(\@array);
}
#print join("\n", @array), "\n" if @array;

my @sorted = sort {$a cmp $b} @array;
print join("\n", @sorted), "\n" if @sorted;
