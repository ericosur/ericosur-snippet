#!/usr/bin/perl
#
# getopt_demo.pl
#
# Getopt::Std demo, getopts()
#
# 2007/12/04 by ericosur
#

use strict;
use warnings;

use Getopt::Std;

sub help
{
	print<<EOL;
***** help message *****
<o>ut	bool value
<i>n	bool value
<f>ile	string value
EOL
}

my %my_opt;
my $opt_cmd = 'oif:h';

if (!@ARGV)  {
	$my_opt{h} = 1;
	print "not @ARGV\n";
}

getopts($opt_cmd, \%my_opt);	# -o & -i are boolean value, -f take argument

if ($my_opt{h})  {
	help;
	exit 1;
}

my $out = $my_opt{o} || "undef";
my $in = $my_opt{i} || "undef";
my $file = $my_opt{f} || "undef";

printf "out: %s\nin: %s\nfile: %s\n", $out, $in, $file;

while (@ARGV)  {
	my $ii = shift @ARGV;
	print "$ii\n";
}

=pod

=head1 NAME

getopt_demo.pl

=head1 DESCRIPTION

simple demo for Getopt::Std

=head1 USAGE

getopt_demo.pl [-i] [-o] [-f string]

=cut
