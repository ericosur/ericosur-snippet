use strict;
use Storable;

my %hash = ();
my $dfile = 'result.dat';

if (not -e $dfile)  {
	die "cannot load $dfile\n";
}

%hash = %{ retrieve($dfile) };

my $total = 0;
foreach (keys %hash)  {
	$total += $hash{$_};
}

foreach my $key ( sort { $hash{$b} <=> $hash{$a} } (keys %hash) )  {
	printf "\"%s\",\"%d\",\"%f\"\n", $key, $hash{$key}, $hash{$key}/$total;
}
