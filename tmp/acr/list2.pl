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
	my $cnt = 0;
	my $line = 3;
	my $cc = 0;
	#my @arr = split(//,$buf);

	foreach (split(//,$buf)) {
		if ($cnt && ($cnt % $line == 2)) {
			printf("%04x:%02x  ", $cnt+$off, ord($_));
			$cc ++;
		}
		if ($cc==6) {
			print "\n";
			$cc = 0;
		}
		$cnt += 1;
	}
	print "\n";
	print "cnt:$cnt\n";
}

sub list_file()
{
	my $file = 'user.profile';
	my $offset = 0x89;
	my $ret;
	my $buf;
	my $bufsize = 6*3*48;

	printf("offset: 0x%02x\n", $offset);
	open my $fh, $file or die;
	binmode $fh;
	seek($fh, $offset, 0);
	##for (my $i=0; $i<10; $i++) {
	$ret = read($fh, $buf, $bufsize, 0);
	printf("ret=%d\n", $ret);
	output_hex($buf, $offset);
	##}
	close $fh;
}

sub main()
{
	list_file();
}

main;
