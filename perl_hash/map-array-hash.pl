#!/usr/bin/perl

# use map to associate two array into hash

@array = qw( 5 10 15 20 25 30 );

#@newarray = map { $_ => $_*2 } @array;
%hash = map { $_ => $_*2 } @array;
@newarray = map { $_*2 } @array;		# syntax error???

print "\n print out new array\n";
while ( ($k, $v) = each (%hash) )  {
	print "$k => $v\n";
}

print "\n print out new array\n";
foreach (@newarry) {
	print "$_\n";
}
