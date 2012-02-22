#!/usr/bin/env perl
use strict;
use warnings;
use utf8;
use encoding 'utf8';

sub 馬  { "馬函式" }

print 馬(),"\n";

*鹿 = *馬;
print "call deer...\n";
print 鹿(),"\n";

