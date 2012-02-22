#!/usr/bin/perl

#
# 計算某字元在字串中的出現次數
#

$str = q(aaaagggddeedkdkdkslsllllaxjdjslaald);

# 破壞性
$_ = $str;
printf "count a = %d\n", $cnt = tr/a//;

# 非破壞性
$cnt{$_}++ for split //,$str;
printf "count a = %d\n", $cnt{'g'};

