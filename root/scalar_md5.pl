#!/usr/bin/perl

# demo how to take MD5 value in a scalar
#
# 2006/12/27 by ericosur

# Functional style
use Digest::MD5  qw(md5 md5_hex md5_base64);

$data = $ARGV[0] // "The quick smart fox jumps over the lazy dog";

# MD5 in hex value
$digest[0] = md5_hex($data);

# MD5 value into base64 format
$digest[1] = md5_base64($data);

#$digest[2] = md5($data);	# it is numeric value

foreach (@digest)  {
	print $_, "\n";
}
