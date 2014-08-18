#!/usr/bin/perl
#
# example for Roman <-> arabic numbers
#

use Roman;

$arabic = 2009;

$roman = Roman($arabic);
#$roman = roman($arabic);
printf "%s => %s\n", $arabic, $roman;

$roman = "mcmxciii";
$arabic = arabic($roman) if isroman($roman);
printf "%s => %s\n", $roman, $arabic;
