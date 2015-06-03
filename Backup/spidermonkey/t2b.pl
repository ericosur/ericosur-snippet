# t2b.pl

# just translate text into 0x02d format with comma

my $cnt = 0;

while (<>)
{
	my @lns = split(//, $_);
	foreach my $cc (@lns)  {
		++ $cnt;
		printf("0x%02x, ", ord($cc));
		print("\n") if ($cnt>0 && $cnt%10==0);
	}
}
