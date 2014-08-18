#!/usr/bin/perl

use strict;

my $infile = $ARGV[0] || "account.dat";
my $buf;
my $bufsize = 956;
my $offset = 8;
my $ret;
my $count = 0;
my $fmt_str = "0x%02x, ";	# you may change to "0x%02X "

print STDERR "read from $infile\n";

open INFILE, $infile or die;
binmode INFILE;
read INFILE, $buf, $offset;


OUTSIDE:
for my $tt (1..3)
{
	$ret = read(INFILE, $buf, $bufsize);
#	printf "ret = %d\n", $ret;
	last OUTSIDE if ($ret eq 0);
	printf "\n{	// #%d\n", $tt;
	output_hex($buf);
	printf "\n},	// #%d\n", $tt;
}

close INFILE;

printf STDERR "\nbyte count = %d\n", $count;



sub output_hex()
{
	my $buffer = shift;
	my $size = length $buffer;
	my $i;
	my $line_count = 0;

	for ($i = 0; $i < $size; ++$i)
	{
###		substr EXPR,OFFSET,LENGTH
		printf $fmt_str, ord(substr($buffer, $i, 1));
		++ $line_count;
		++ $count;
		if (($line_count % 16) eq 0)
		{
			print "\n";
		}
	}
	print STDERR ".";
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
