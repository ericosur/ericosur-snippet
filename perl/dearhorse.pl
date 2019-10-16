#!/usr/bin/env perl

# demo utf-8 function name and function pointer

use strict;
use warnings;
use utf8;
use encoding 'utf8';

# sub horse()
sub 馬()  { "馬函式" }

# call horse()
print "call horse()...\n";
print 馬(),"\n";

# 指鹿為馬
*鹿 = *馬;
print "call deer()...\n";
print 鹿(),"\n";
