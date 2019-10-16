#!/usr/bin/perl

$str = "The brave one";
$str =~ s/([Tt]he)\s+(.*)/$2, $1/;
print $str,"\n";
