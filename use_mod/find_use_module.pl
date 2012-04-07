#!/usr/bin/perl

use strict;
use File::Glob ':glob';

my @list = glob('*.pl');

for (@list)
{
	s/\n//;
#	print;
	if (-f $_)
	{
		list_use_module($_);
	}
}

sub list_use_module()
{
	my $file = shift;
	my $fh;

	print $file,":\n";
	open $fh, $file or die;


LINE:
	while (<$fh>)
	{
		next LINE if (/^#/);
		next LINE if (/use strict;/);
		next LINE if /use warnings;/;
		print $_ if (/^use/);
	}

	close $fh;
}

