#!/usr/bin/perl
# small demo of $` $& $'

local $_ = "abcdefghi";
/def/;
print "$`:$&:$'\n";
