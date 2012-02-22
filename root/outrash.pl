#!/usr/bin/perl
#!/bin/perl

# produce a trash file with specific size
#
# Nov 30 2006 by ericosur
# this script will generate temp file at cwd
# the default size is 1KB if no argument specified
#
# 2007/11/16 by ericosur

use strict;
use warnings;

use Cwd;
use File::Temp qw(tempfile tempdir);
use Getopt::Std;
use Benchmark ':hireswallclock';


sub help_message();
sub show_size($);
sub fill_block;


#
# constants
#
my $KB = 1024;
my $MB = 1024 * 1024;
#
# here to define the output range
#
#my $upper = ord('z');
#my $lower = ord('a');
my $upper = 0xff;
my $lower = 0;
my $block_size = 4 * $MB;


#
#
#

my %opts;
getopts("ho:s:", \%opts);	# -h: bool, -o & -s take argument

my $basedir = getcwd();
my($fh, $tmp_file) = tempfile('trashXXXX', DIR => $basedir);

my $file_size = $opts{s} || ($MB);
my $file_name = $opts{o} || undef;

help_message() if ($opts{h});

if ($file_size =~ m/(\d+)([kKmM])[bB]?/)  {
	#print STDERR "1: $1\n2: $2\n";
	my $foo = $1;
	if ($2 =~ m/m/i)  {
		$file_size = $foo * $MB;
	} elsif ($2 =~ m/k/i)  {
		$file_size = $foo * $KB;
	}
}

printf STDERR "Output to <%s>, %s (-h to see options)\n", $tmp_file, show_size($file_size);

if ($file_size < $block_size)  {
	$block_size = $file_size;
}

my $left_size = $file_size;
my $out_size = 0;
my $t0 = new Benchmark;		# benchmark start...

	while ($left_size)  {
		my $buffer = fill_block;
		if ($left_size < $block_size)  {
			print $fh substr($buffer, 0, $left_size);
			$out_size += $left_size;
			$left_size -= $left_size;
		}
		else  {
			print $fh $buffer;
			$out_size += $block_size;
			$left_size -= $block_size;
		}

		print STDERR "$out_size\r";
	}
	close $fh;
	print STDERR "$out_size\n";

my $t1 = new Benchmark;		# benchmark end...
my $td = timediff($t1, $t0);

	if ($td->[0] != 0)  {
		my $result = show_size($file_size / $td->[0]);
		print "throughput $result/sec\n";
	}

#
# rename the temp file to specified name if availible
#
if ( $file_name )
{
	if (-e $file_name)  {
		print "<$file_name> exists, not rename\n";
	}
	else  {
		print "rename <$tmp_file> to <$file_name>\n";
		rename $tmp_file, $file_name;
	}
}


sub help_message()
{
	print "\toutrash.pl [-s size] [-o output filename]\n\n";
	print "\tsize: like 2038 (byte), or 2k, 3M\n";
	print "\tif no specified, it would be ''trashXXXX''\n";
	exit;
}

sub show_size($)
{
	my @unit = qw(Bytes KB MB GB);
	my $cnt = 0;
	my $fsize = shift;

	while ($fsize > 1024)  {
		++ $cnt;
		$fsize /= 1024;
	}

	return $fsize . ' ' . $unit[$cnt];
}


sub fill_block
{
	my $range = $upper - $lower + 1;
	my $block;
	my $i;

	for (1 .. $block_size)  {
		$block .= chr(int(rand($range)+$lower));
	}

	return $block;
}


=pod

=head1 NAME

	outrash.pl

=head1 DESCRIPTION

	This script generates file with random bytes with specific range.

=head1 USAGE

	outrash [-s size] [-o output filename] [-h]

	"-s size" to specify the size of generated file in byte. You may use
	'k' or 'M' for postfix.

	"-o output filename" to specify the output file name.

	"-h" the help message

If no arguments specified, the file name would be ''trashXXXX'' and the
size would be 1024 bytes.

=head1 USAGE

	outrash.pl -s 2k -o foo.bin
	outrash.pl -s 1.44M -o floopy.bin

=cut
