#!/usr/bin/perl
#
# demo the loop vs regexp the ''g'' option
#

$count = 0;
$_ = $line = 'The quick brown fox jumps over the lazy dog';
print;
while (/\s/g)  {
	$count++;
}
print "\nword count: $count\n";

# refer to split()
@data = $line =~ /\w+/g;
print join("\t", @data), "\n";
