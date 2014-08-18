#!/usr/bin/perl
#
# tr_test.pl
#
#
# 2007/12/04 by ericosur
# some tr/a/b/ demo
#

use strict;
use warnings;

sub printl($)
{
	my $str = shift;
	$str =~ s/\n$//g;		# kill the last '\n' of string
	printf "%s\n", $str;
}

sub sep()
{
	print '-' x 35, "\n";
}


my $orig =<<EOL;
once upon a time, there was a trivia question
are told to every traveller in this land.
there was a lion who would ask everyone passed by.
EOL

sep();

my $foo = $orig;
$foo =~ tr/e/*/;				# replace 'e' to '*'
printl($foo);

my $cnt = $foo =~ tr/*/*/;		# count the '*' in $foo
print "there are $cnt stars\n";

sep();

my $bar = $orig;
$bar =~ tr/the/*/;	# notice, char [t|h|e] are replaced, not like ''s///''
printl($bar);

sep();

my $foba = $orig;
$foba =~ s/the/*/g;
printl($foba);

sep();

my $bafo = $orig;
$bafo =~ s/[the]/*/g;	# same as ''tr/the/*/''
printl($bafo);

sep();

my $abab = $orig;
$abab =~ tr/aeiou/AEIOU/;
printl($abab);

sep();

my $url = "http://tw.yahoo.com:8080/cgi-bin/test.pl";
my ($host, $port, $file) = ($url=~m|http://([^/:]+):{0,1}(\d*)(\S*)$|);
printf "(%s)(%s)(%s)\n", $host, $port, $file;

