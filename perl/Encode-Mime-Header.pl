#!/usr/bin/perl
# note this file is in UTF-8 encoding

# demo how to use Encode to encode/decode RFC2047 encoded email header

use strict;
use warnings;

use Encode qw/encode decode/;

#$utf8   = decode('MIME-Header', $header);
#$header = encode('MIME-Header', $utf8);


my $str;
my $dec_str;
my $enc_str;

$str = "中文輸入法";
$enc_str = encode('MIME-Header', $str);
printf ">>%s<<\n", $enc_str,"\n";
#$enc_str = encode('MIME-B', $str);
#printf ">>%s<<\n", $enc_str,"\n";
#$enc_str = encode('MIME-Q', $str);
#printf ">>%s<<\n", $enc_str,"\n";


$str = "=?big5?B?UkU6IFukdbDTqkGwyF0gpLWk6aTIwFwtqmu1WLzauHGmocBcsrA=?=";
$dec_str = decode('MIME-Header', $str);
printf ">>%s<<\n", $dec_str,"\n";	# it will croak if using print



my @list = Encode->encodings();
for (@list)
{
	print;
	print "\n";
}
