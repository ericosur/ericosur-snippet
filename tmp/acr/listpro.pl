#!/usr/bin/perl
=pod
start with 0
group 3, set 5, pos 1 => 0x298

1 group 48 cards, 1 set 6 cards
6 groups

#0 card at 0x8b
=cut

my $debug = 1;

sub output_hex($$)
{
	my $buf = shift;
	my $off = shift;
	my $max = 48 * 6;
	my @arr = split(//,$buf);

	for (my $i=0; $i<$max; $i++) {
		my $addr = $off+$i*3+2;
		printf("%04x:%02x  ", $addr, ord($arr[$addr]));
		$arr[$addr] = chr(0x06);
		if (($i+1)%6==0) {
			print "\n";
		}
	}
	print "\n";
	my $outbuf = join("",@arr);
	return $outbuf;
}

sub list_file()
{
	my $file = 'ericosur.profile';
	my $ret;
	my $buf;
	my $bufsize = 2472;
	my $offset = 0x89;

	open my $fh, $file or die;
	binmode $fh;
	$ret = read($fh, $buf, $bufsize, 0);
	printf("ret=%d\n", $ret);
	my $modify = output_hex($buf, $offset);
	close $fh;

	open my $ofh, "> test.profile" or die;
	binmode $ofh;
	print $ofh $modify;
	close $ofh;
}

sub main()
{
	list_file();
}

main;
