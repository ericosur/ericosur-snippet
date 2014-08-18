#!/usr/bin/perl
#
# a very simple demo how to use Crypt::RC4
#
# first time is to encrypt, the 2nd time would decrypt
#

use strict;
use warnings;

use Crypt::RC4;

my $passphrase = "The quick brown fox jumps over the lazy dog.";
my $in_file = $ARGV[0] || "in.txt";
my $out_file = $ARGV[1] || "out.bin";

if (not -f $in_file)  {
	print "$in_file not exists\n";
	exit 1;
}
open my $infh, $in_file or die;
open my $outfh, "> $out_file" or die;
binmode $infh;
binmode $outfh;

# process an entire file, one line at a time
# (Warning: Encrypted file leaks line lengths.)
my $ref3 = Crypt::RC4->new( $passphrase );
my $read_in = 0;
my ($in_buffer, $out_buffer) = (0, 0);
my $cnt_read = 0;

do  {
	$read_in = read($infh, $in_buffer, 10240);
	print $outfh $ref3->RC4($in_buffer);


	$cnt_read += $read_in;
} while ($read_in > 0);

close $infh;
close $outfh;

print $cnt_read, "\n";
