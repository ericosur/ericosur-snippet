use Data::Dump qw(dump);

@row = ();
$cnt = 0;
$fname = sprintf("%02d.txt", $cnt);

while (<DATA>)  {
	@row = split /\w+/;
	open $fh, "> $fname" or die;
	foreach (@row)  {
		print $fh $_,"\t";
	}
	close $fh;
}

__DATA__
1		2		3
0.1		0.5		0.8
0.9		1.2		3.2
9.2		8.4		7.2
