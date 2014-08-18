use Data::Dump qw(dump);

sub shuffle (@) {
	my @a=\(@_);
	my $n;
	my $i=@_;
	print "i: ", $i, "\n";
	map {
	  $n = int(rand($i--)) + 1;
	  print "n=$n\n";
	  (${$a[$n]}, $a[$n] = $a[$i])[0];
	} @_;
	dump(@_);
	return @_;
}

@mm = qw(1 2 3 4 5 6);
shuffle(@mm);
