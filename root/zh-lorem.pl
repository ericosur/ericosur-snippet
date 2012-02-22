#!/usr/bin/env perl
=pod

=head1 NOTE

Demo of Text::Greeking::zh_TW. It would output to STDOUT.
It would print utf8 in linux, and big5 in windows.

=cut

use strict;
use warnings;
use Encode qw(encode);
use Text::Greeking::zh_TW;

print STDERR "demo of Text::Greeking::zh_TW\n";

my $g = Text::Greeking::zh_TW->new;
$g->paragraphs(2, 3);	# change the limit if needs
$g->sentences(1, 4);	# change the limit if needs
my $str = $g->generate;

if ($^O eq 'linux')  {
	# to avoid the croak for wide char output
	binmode(STDOUT, ':encoding(utf8)');
	print $str;
}
else  {
	my $b5 = encode("big5", $str);
	print $b5;
}

