#!/usr/bin/perl
﻿
use strict;
use warnings;

use Text::CSV::Simple;

# need a csv file with 4 colomns
my $datafile = 'abc.csv';

die if (not -e $datafile);

my $parser = Text::CSV::Simple->new;
$parser->field_map(qw/name phone1 phone2 mvpn/);
my @data = $parser->read_file($datafile);

# list all
for my $elem (@data)
{
	if ($elem->{mvpn})
	{
		print $elem->{name},"\t", $elem->{mvpn},"\n";
	}
}

