#!/usr/bin/perl

#
# �p��Y�r���b�r�ꤤ���X�{����
#

$str = q(aaaagggddeedkdkdkslsllllaxjdjslaald);

# �}�a��
$_ = $str;
printf "count a = %d\n", $cnt = tr/a//;

# �D�}�a��
$cnt{$_}++ for split //,$str;
printf "count a = %d\n", $cnt{'g'};

