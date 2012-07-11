#!/usr/bin/perl

use strict;
use warnings;

sub show_size($);
sub fill_block;

#
# constants
#
my $MB = 1024 * 1024;
my $GB = 1024 * 1024 * 1024;
#
# here to define the output range
#
my $upper = 0xff;
my $lower = 0;
my $block_size = 16 * $MB;
my $file_size = 1 * $GB;
my $file_name = 'prng.bin';

sub main()
{
	open my $fh, "> $file_name" or die;
	binmode($fh);
    if ($file_size < $block_size)  {
    	$block_size = $file_size;
    }

    my $left_size = $file_size;
    my $out_size = 0;

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

	for (1 .. $block_size)  {
		$block .= chr(int(rand($range)+$lower));
	}

	return $block;
}

main;

