#!/usr/bin/perl -w

# originated from
# cnhackTNT { a t } perlchina.org
# http://my.opera.com/pstgroup/blog/2007/03/15/tips-perl
#

#
# Exacting Unique Elements from a Array
# Just few tricks with perl's hash && grep
#

use strict;
use warnings;


sub main()
{
	my @data = ( 'This', 'is', 'a', 'array', 'with', 'a', 'duplicate','element' );
	my $return1 = unique_elem_from_array_unsort(\@data);
	my $return2 = unique_elem_from_array_sort(\@data);
	print join(',',@$return1),"\tby unique_elem_from_array_unsort()\n";
	print join(',',@$return2),"\tby unique_elem_from_array_sort()\n";
}

sub unique_elem_from_array_unsort(\@){
	# eliminate duplicate values from a array
	# and don't care about the order of @array's elements.
	my $array = shift;
	my %hash = ();
	@hash{@$array} = ();
	$array = [keys %hash];
	return $array;
}

sub unique_elem_from_array_sort(\@){
	# eliminate duplicate values from a array
	# and do care about the order of @array's elements.
	my $array=shift;
	my %hash = ();
	$array = [grep{!$hash{$_}++}@$array];
	return $array;
}

main();
