#!/usr/bin/perl
use strict;
use warnings;

use Text::Lorem;
use Getopt::Std;
use if $^O eq "MSWin32","Win32::Clipboard";

my %opts = ();
getopts("s:w:p:", \%opts);	# all take argument string

my $text = Text::Lorem->new();
my $total;
my $sentences;
my $paragraphs;

#my $ww = $opts{w} || 1;
my $ss = $opts{s} || 1;
my $pp = $opts{p} || 1;

	# Generate a string of text with 5 words
	#    $words = $text->words(5);
	#    print "$words\n";

	# Generate sentences
	print STDERR "ss = $ss\n";
	$sentences = $text->sentences($ss);
	$total .= $sentences . "\n";
	print "$sentences\n";
	sep();

	# Generate paragraphs
	print STDERR "pp = $pp\n";
	$paragraphs = $text->paragraphs($pp);
	$total .= $paragraphs;
	print "$paragraphs\n";
	sep();


count_word(\$total);
count_char(\$total);

Win32::Clipboard()->Set($total) if $^O eq "MSWin32";

sub sep
{
	print '-' x 70, "\n";
}

sub count_word
{
	my $str = shift;
	my $cnt = 0;

	++ $cnt while ($$str =~ m/\w+/g);
	print STDERR "word count = $cnt\n";
}

sub count_char
{
	my $str = shift;
	my $cnt = 0;

	++$cnt while ($$str =~ m//g);
	print STDERR "char count = $cnt\n";
}

