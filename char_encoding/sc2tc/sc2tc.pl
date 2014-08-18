open $fh, "sc2tc.txt" or die;
binmode($fh, ':encoding(utf8)');

while ( <$fh> ) {
	next if /^$/;
	print if /^#/;
	s/[\r\n]//;
	s/(\S+)\t(\S+)/sprintf("%x\t%x\n", ord($1),ord($2))/e;
	print $_;
}
close $fh;
