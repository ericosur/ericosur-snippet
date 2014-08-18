#!/usr/bin/perl

# $str is a big-5 encoding string
$str = "¤¤¤å¦r";

print "$str\n";
print length($str)."\n";
print ord($str)."\n";
