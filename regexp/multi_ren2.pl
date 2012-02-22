#!/usr/bin/perl
use strict;

$_ =<<EOL;
D:\\tmp\\mms\\CIMG2335.JPG
EOL

	s/^((.*\\)[A-Z]+(\d+.JPG))$/ren \1 \2FOO\3/;
	print;

#
# result would be
# ren D:\tmp\mms\CIMG2335.JPG FOO2335.JPG
#
#
# the one-liner would be:
# > perl -ne "s/^(.*\\[A-Z]+(\d+.JPG))$/ren \1 FOO\2/;print;" list.txt
#
