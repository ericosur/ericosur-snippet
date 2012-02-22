#!/usr/bin/perl
#
# demo q, qq, qw, qx, qr
#
# 2006/12/27 by ericosur

my @name_list = (
	"mary joe maggie bob alice",		# same as qq
	qq(allen chris clive \nhorse jojo),	# double quote
	q(robin ob tom \nneil stanley sam),	# single quote
	qw(patty arthur patrick vincent),	# quote word
	qx(cmd /c date /t),					# the back quote
	qr(\d+.\d*)							# quote reqular expression
);

for (@name_list)
{
	s/\n$//;
	printf "_%s_\n", $_;
}
