#!/usr/bin/perl
#
# demo how to use 'eval' in regex
#
# 2007/03/21 by ericosur

$_=<<EOL;
35
24
97
16
EOL


foreach (split /\n/, $_)
{
	# postfix e for eval the result string
	s/^(\d+)$/printf "%d\t%d\n", $1, $1*5+5000/e;
}
