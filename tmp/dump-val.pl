use Dumpvalue;
my $dumper = new Dumpvalue;
$dumper->set(globPrint => 1);
#$dumper->dumpValue(\*::);
#$dumper->dumpvars('main');
#my $dump = $dumper->stringify($some_value);

my $val = 1;
$dumper->dumpValue($val);
