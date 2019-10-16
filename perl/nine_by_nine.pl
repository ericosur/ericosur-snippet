#!/usr/bin/perl
#
# a non-sense 9x9 multiple table generator
#

#for ($i = 0; $i < 9; $i ++)	# stupid and error-prone

for my $mm (1..9)
{
	for my $nn (1..9)
	{
		print $mm * $nn, "\t";
	}
	print "\n";
}

=pod

=head1 NAME

nine_by_nine.pl

=head1 SYNOPSIS

nine_by_nine.pl

=head1 DESCRIPTION

Just non-sense double for-loop example.

=cut
