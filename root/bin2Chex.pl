#!/usr/bin/perl
#
# binary to hex like hexdump
#
# 2007/11/14 by ericosur
#

use strict;
use warnings;

sub output_hex($);

###use Fcntl qw(SEEK_END SEEK_CUR SEEK_SET);

my $infile = $ARGV[0] or die "you need to specify a file";
my $buf;
my $bufsize = 1024;
my $ret;
my $count = 0;
my $fmt_str = "0x%02X, ";	# you may change to "0x%02X "

print STDERR "read from $infile\n";

open INFILE, $infile or die;
binmode INFILE;

OUTSIDE:
while (1)
{
	$ret = read(INFILE, $buf, $bufsize);
#	printf "ret = %d\n", $ret;
	last if ($ret eq 0);
	output_hex($buf);
}

close INFILE;

printf STDERR "\nbyte count = %d\n", $count;



sub output_hex($)
{
	my $buffer = shift;
	my $size = length $buffer;
	my $i;

	for ($i = 0; $i < $size; ++$i)  {
###		substr EXPR,OFFSET,LENGTH
		printf $fmt_str, ord(substr($buffer, $i, 1));
		++ $count;
		if (($count % 16) eq 0)  {
			print "\n";
		}
	}
}


=pod

=head1 NAME

bin2hex

=head1 DESCRIPTION

The script is a simple hex dump utility.

=head1 USAGE

	bin2hex.pl <infile>

	The result would be output to STDOUT.

=head1 EXAMPLE

	bin2hex.pl pushmsg.bin

	output:
	0x03, 0x0D, 0x6A, 0x00, 0x85, 0x07, 0x03, 0x72, 0x61, 0x73,

	<OR>

	bin2hex.pl pushmsg.bin > output.txt

=head1 NOTE

You might want to change the "$fmt_str" in the script to meet your
need.

=cut
