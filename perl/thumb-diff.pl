#!/usr/bin/perl
use utf8;
=encoding utf-8

=head1 DESCRIPTION

先使用 friendly flickr 把 large 和 thumb 的圖分別放
在對應的子目錢裡

folder \
	+-- large \
	+-- thumb \
這個 script 放在 folder 下，執行之後會把
短缺的檔案列出來。(預期是 thumb 下的 jpg 比 large 多)

2007/10/15 by ericosur

=cut

use strict;
use warnings;


sub main()
{
	my @large = ();
	@large = map {
		s[\n|large\/][];
		uc;
	} glob("large/*.jpg");

	my @thumb = ();
	@thumb = map {
		s[\n|thumb\/][];
		uc;
	} glob("thumb/*.jpg");

	my @diff = diff_of_array(@thumb, @large);

	# http://www.perlfect.com/articles/sorting.shtml
	my @sorted = sort { $a cmp $b } @diff;	# alphabetical sort

	my $ofile = "diff.txt";
	open my $oh, "> $ofile" or die "cannot output: $!\n";
	print $oh join("\n", @sorted), "\n";
	close $oh;
	print STDERR "result output to $ofile\n";
}

sub diff_of_array()
{
	my (@thumb, @large) = @_;

	my @union = ();
	my @intersection = ();
	my @difference = ();
	my %count = ();
	my $element;

    foreach $element (@thumb, @large)  {
    	$count{$element}++;
    }
    foreach $element (keys %count)  {
        push @union, $element;
        push @{ $count{$element} > 1 ? \@intersection : \@difference }, $element;
    }
    return @difference;
}

main;
