#!/usr/bin/perl
#!/bin/perl

# pattern to match a multi-line
#	A = B \
#		C
#
# 2006/12/27 by ericosur

use strict;
use warnings;

my $line =<<EOF;
File List = \\
	array.c builtin.c kernel.c field.c gawkmisc.c io.c main.c \\
	missing.c
EOF

# remember to use 'qr' to quote a regex pattern
my $ptn = qr{
	(.*?)\s*=
		\s*
		(
			[^\n\\]*
			(\\\n[^\n\\]*)*
		)
}x;

my @array = (
	$ptn,
	qr{(.*?)\s*=(.*)(\n*.*)*}
);


print $line . "\n";

my $i = 0;
for my $x (@array)  {
	print "###" . $i . "\n";
	if ( $line =~ $x )  {
		print "1:<$1>\n2:<$2>\n3:<$3>\n4:<$4>\n";
	}
	$i ++;
}

