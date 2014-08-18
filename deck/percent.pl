$sum = 6188;

open $fh, "cnt.txt" or die;
while (<$fh>)  {
	m/^\s+(\d+)\s+(\S+)/;
	printf "%s: %d  %.4f / 100\n", $2, $1, $1/$sum*100;
}
close $fh;
