#!/usr/bin/perl
# reverse key and value pair

%hh = ( "mark" => 10, "denny" => 20, "shelly" => 30 );

%rr = reverse %hh;
# now %rr would be (10 => "mark", 20 => "denny", 30 => "shelly")

foreach (keys %rr)  {
	print $_, "\t", $rr{$_},"\n";
}
