use strict;
use warnings;

my $debug = 1;

sub get_config($)
{
	my $ifile = shift;
	print "get_config: $ifile\n" if $debug;
	open my $fh, $ini or die;
	while ( <$fh> )  {
		next if /^$/;
		next if /^#/;
		s/\n//;
		eval($_);
		print "get_config: $_\n" if $debug && $verbose;
	}
	close $fh;
}
