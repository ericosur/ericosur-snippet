#!/usr/bin/perl
#
# some pack and unpack usage
#

sub sep
{
	print "\n", '-' x 10, "\n";
}

@pp = qw(alpha beta charlie);

sub pz
{
	# null terminated
	print pack('Z*' x ($#pp+1), @pp);
	sep;
}

sub pa0
{
	# space padding
	print pack('A6' x ($#pp+1), @pp);
}

sub pa1
{
	# null padding
	print pack('a6' x ($#pp+1), @pp);
}

sub phh
{
	# ord($char)%16
	print pack('h'x10, '0'..'9');
	print pack('H'x6, 'a'..'f');
	# ord($char)%2
	print pack('b'x10, '0'..'9');
}

sub pccw
{
	@aa = (0x63, 0x64, 0x20, 0x55);
	foreach (@aa)  {
		print pack('c', $_);
	}
}

sub pnnvv
{
	$str = "計劃";
	while ( $str =~ m/(\W)/g )  {
		printf "%02x ", unpack('C', $1);
	}
}

sub pnn
{
 	print join(" ", map { sprintf "%#02x", $_ }
                          unpack("W*",pack("L",0xdeadbeef))), "\n";
}



$sss = "D4C3B2A190";
#@aaa = split / /, $sss;
my $out = pack "H40", $sss;

#hexdump($out);
print join(" ", map { sprintf "%#02x", $_ }
	unpack('W*', $out));
