while (<DATA>) {
	my $ln = $_;
	s/([0-9a-f]+)$/hex($1)/eg;
	$_ = $ln;
	s/([0-9]+)$/sprintf("%08x",$1)/eg;
	print;
}

__DATA__
This is 12345678
addr at: abcdef12
hex number: 21340000
