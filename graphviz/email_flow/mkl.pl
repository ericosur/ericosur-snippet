#!/usr/bin/perl

$files = `cmd /c dir /b *.dot`;
@array = split /\n/,$files;

foreach (@array)  {
	s/dot$/gif/;
}

print "FILES = \\\n";
print "\t";
print join(" \\\n\t", @array);
print "\n";
