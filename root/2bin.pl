#!/usr/bin/perl
=pod

=head1 DESCRIPTION

Translate c array hex values into binary.

(the '','' and space would be ignored)
input data format:

0x01, 0x02, 0x5c, 0x68, 0x5c, 0x7b

=head1 NOTE

the line beginning with C<//> and C<#> would be ignored

=cut

use strict;

#
# use pack, sprintf, replace to finish this job
#
sub dec_str
{
	s/0x([a-fA-F0-9][a-fA-F0-9]),?\s*/pack("C", hex($1))/eg;
	return $_;
}


sub main()
{
	#
	# only stdin, stdout currently
	#
	my $ifh = \*STDIN;
	binmode $ifh;
	my $ofh = \*STDOUT;
	binmode $ofh;
	my $ret;

	LINE:
	while (<$ifh>)  {
		s/(\r|\n)//;
		s[#.*$][];	# strip perl style comment
		s[//.*$][];	# strip c++ style comment
		next LINE if /^$/;	# skip empty line
		#$ret = $_;
		$ret = dec_str($_);
		print $ofh $ret;
	}

	close $ifh;
	close $ofh;
}

main;
