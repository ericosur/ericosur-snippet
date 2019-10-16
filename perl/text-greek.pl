#!/usr/bin/perl -w

=pod

=head1 NOTE

Demo of module C<Text::Greeking>

=over

=item NOTE

C<Win32::Clipboard> is used
=cut

use strict;
use warnings;

use Text::Greeking;
use if $^O eq "MSWin32","Win32::Clipboard";

my $g = Text::Greeking->new;
$g->paragraphs(2,3);	# min of 1 paragraph and a max of 2
$g->sentences(2,5);		# min of 2 sentences per paragraph and a max of 5
$g->words(4,12);		# min of 8 words per sentence and a max of 16

my $str = $g->generate;	# use default Lorem Ipsum source

print $str,"\n";

if ($^O eq "MSWin32")  {
	print STDERR "NOTE: result text has been copied to clipboard as well\n";
	Win32::Clipboard()->Set($str);
}

printf STDERR "length: %d\n", length($str);

