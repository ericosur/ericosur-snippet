#!/usr/bin/perl

#
# take MD5 value in a scalar
#
# in RFC 1939, APOP command section
#
#	S: +OK POP3 server ready <1896.697170952@dbc.mtview.ca.us>
#	C: APOP mrose c4c9334bac560ecc979e58001b3e22fb
#	S: +OK maildrop has 1 message (369 octets)
#
#In this example, the shared  secret  is  the  string  `tanstaaf'.
#
#Hence, the MD5 algorithm is applied to the string
#<1896.697170952@dbc.mtview.ca.us>tanstaaf
#
#which produces a digest value of
#c4c9334bac560ecc979e58001b3e22fb
#

# Functional style
use Digest::MD5  qw(md5 md5_hex md5_base64);

$data = q(<1896.697170952@dbc.mtview.ca.us>tanstaaf);

# MD5 in hex value
$digest[0] = md5_hex($data);

# MD5 value into base64 format
$digest[1] = md5_base64($data);

#$digest[2] = md5($data);	# it is numeric value

foreach (@digest)  {
	print $_, "\n";
}
