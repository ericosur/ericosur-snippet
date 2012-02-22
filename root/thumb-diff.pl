#!/usr/bin/perl
#
# ���ϥ� friendly flickr �� large �M thumb ���Ϥ��O��
# �b�������l�ؿ���
#
# folder \
#		+-- large \
#		+-- thumb \
# �o�� script ��b folder �U�A���椧��|��
# �u�ʪ��ɮצC�X�ӡC(�w���O thumb �U�� jpg �� large �h)
#
# 2007/10/15 by ericosur

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
