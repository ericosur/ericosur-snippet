#!/usr/bin/env perl
# note: this file saved as UTF-8 format
use Data::Dump qw(dump);

$word = "test中asd文asd字as到底asd有幾asd個?";

@aaa = split /[\u4e00-\u9fa5]/, $word;
dump(@aaa);
$n = (scalar @aaa) + 1;
print "cht cnt = ", $n;

# should be 8
