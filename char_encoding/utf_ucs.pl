#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;

package myutf8;

# http://www.unicode.org/Public/PROGRAMS/CVTUTF/

# [in] unicode value
# [in] reference to utf8 array
# reference: http://csourcesearch.net/package/aart/0.0.7/aart-0.0.7a/src/util.c/function/ucs2_to_utf8/52,1
sub ucs_to_utf8($$) # /* uses max 4 chars from utf (including the trailing 0) */
{
	my $c = shift;
	my $utf = shift;

	if ($c < 0x80)  {
		$$utf[0] = $c;  # 0*******
		$$utf[1] = 0;
	}
	elsif ($c < 0x800)  {
		$$utf[0] = 0xc0 | ($c >> 6);  # 110***** 10******
		$$utf[1] = 0x80 | ($c & 0x3f);
		$$utf[2] = 0;
	}
	elsif ($c <= 0xffff)  {
		$$utf[0] = 0xe0 | ($c >> 12);  # 1110**** 10****** 10******
		$$utf[1] = 0x80 | (($c >> 6) & 0x3f);
		$$utf[2] = 0x80 | ($c & 0x3f);
		$$utf[3] = 0;
	}
	elsif ($c <= 0x10FFFF)  {
		$$utf[0] = 0xF0 | ($c >> 18);	# 11110*** 10****** 10****** 10******
		$$utf[1] = 0x80 | (($c >> 12) & 0x3f);
		$$utf[2] = 0x80 | (($c >> 6) & 0x3f);
		$$utf[3] = 0x80 | ($c & 0x3f);
		$$utf[4] = 0;
	}
	# UTF-8 is defined for words of up to 31 bits,
	# but we need only 16 bits here
	#print Dumper(@$utf);
}

#
# [in] reference to utf8 array
# [in/out] reference to ucs value
# return unicode value
# It could handle up to 6 bytes UTF-8 sequence
# reference: http://plan9.cs.bell-labs.com/sources/plan9/sys/src/cmd/aux/antiword/utf8.c
sub utf8_to_ucs($$)
{
	my ($utf, $c) = @_;
	my $len = 0;

	if ($$utf[0] < 0x80) {
		$len = 1;
		$$c = $$utf[0];
		return $$c;
	}
	$$c = $$utf[0];
	if ($$c < 0xe0){
		$len = 2;
		$$c &= 0x1f;
	} elsif ($$c < 0xf0){
		$len = 3;
		$$c &= 0x0f;
	} elsif ($$c < 0xf8){
		$len = 4;
		$$c &= 0x07;
	} elsif ($$c < 0xfc){
		$len = 5;
		$$c &= 0x03;
	} else {
		$len = 6;
		$$c &= 0x01;
	}
	for (my $ii = 1; $ii < $len; $ii++) {
		$$c <<= 6;
		if ( $ii < $len) {
			$$c |= $$utf[$ii] & 0x3f;
		}
	}
	return $$c;
}



sub sep($)
{
	my $rr = shift;

	#print Dumper(@$rr);
	foreach (@$rr)  {
		printf "%02x ", $_;
	}
	print "\n", '-' x 40,"\n";
}

sub demo($)
{
	my $val = shift;
	my @utf = ();
	my $c;

	ucs_to_utf8($val, \@utf);
	sep(\@utf);
	utf8_to_ucs(\@utf, \$c);
	printf "0x%X", $c;
	print "\n", '-' x 40,"\n";
}

#
# main procedure here
#
sub demo_main
{

	demo(0x6c);
	demo(0x732);
	demo(0x6789);
	demo(0x10ffff);

	my @u8 = qw(e5 b7 b2);
	for (my $ii = 0; $ii < $#u8+1; $ii++ )  {
		$u8[$ii] = hex($u8[$ii]);
		printf "v=>%02x ", $u8[$ii];
	}
	my $cc;
	utf8_to_ucs(\@u8, \$cc);
	printf "0x%X", $cc;
}

#uncomment if want to see the demo
#demo_main;

1;

__END__
my $ustring1 = "Hello \x{263A}!\n";
binmode DATA, ":utf8";
my $ustring2 = <DATA>;

binmode STDOUT, ":utf8";
print "$ustring1$ustring2";

sub get_utf8_byte_seq($)
{
	my $uni = shift;
	my $ret;
	my $tmp;

	if ($uni >= 0 && $uni <= 0x7F)  {
		$ret = sprintf "%02X", $uni;
	}
	elsif ($uni >= 0x80 && $uni <= 0x7FF)  {
		$ret = sprintf "%02X %02X",
			(((0x07C0 & $uni) >> 6) | 0xC0),	# 110 - 5
			(( 0x003F & $uni) | 0x80);			# 10 - 6
	}
	elsif (($uni >= 0x800 && $uni <= 0xD7ff) || ($uni >= 0xE000 && $uni <= 0xFFFF)) {
		$ret = sprintf "%02X %02X %02X",
			(((0xF000 & $uni) >> 12) | 0xE0),	# 1110 - 4
			(((0x0FC0 & $uni) >> 6) | 0x80),	# 10 - 6
			(( 0x003F & $uni) | 0x80);			# 10 - 6
	}
	elsif ($uni >= 0x010000 && $uni <= 0x10FFFF)  {
		$ret = sprintf "%02X %02X %02X %02X",
			(((0x1C0000 & $uni) >> 18) | 0xF0),	# 11110 - 3
			(((0x03F000 & $uni) >> 12) | 0x80),	# 10 - 6
			(((0x000FC0 & $uni) >> 6) | 0x80),	# 10 - 6
			(( 0x00003F & $uni) | 0x80);		# 10 - 6
	}
	return $ret;
}

print get_utf8_byte_seq(0x7f), "\n";	# 7F
print get_utf8_byte_seq(0x054d), "\n";	# D5 8D
print get_utf8_byte_seq(0x6789), "\n";	# E6 9E 89
print get_utf8_byte_seq(0x10ffff), "\n";	# F0 90 80 80

=pod

=head1 NOTE

Uncomment the ''demo_main;'' to see the demo.

=head1 REFERENCE
<pre>
/* uses max 4 chars from utf (including the trailing 0) */
void ucs2_to_utf8(unsigned short /*unicode*/ c, char* utf)
{
	if (c < 0x80)
	{
		utf[0] = c; /* 0******* */
		utf[1] = 0;
	}
	else if (c < 0x800)
	{
		utf[0] = 0xc0 | (c >> 6); /* 110***** 10****** */
		utf[1] = 0x80 | (c & 0x3f);
		utf[2] = 0;
	}
	else
	{
		utf[0] = 0xe0 | (c >> 12); /* 1110**** 10****** 10****** */
		utf[1] = 0x80 | ((c >> 6) & 0x3f);
		utf[2] = 0x80 | (c & 0x3f);
		utf[3] = 0;
	}
	/* UTF-8 is defined for words of up to 31 bits,
	but we need only 16 bits here */
}
</pre>
=cut
