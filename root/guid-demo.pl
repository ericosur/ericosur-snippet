#!/usr/bin/perl
﻿use Data::GUID;

for (1..2)  {

my $guid = Data::GUID->new;

my $string = $guid->as_string; # or "$guid"
print $string,"\n";

my $other_guid = Data::GUID->from_string($string);
print $other_guid,"\n";

if (($guid <=> $other_guid) == 0) {
	print "They're the same!\n";
}

undef $guid;

}