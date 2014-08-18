#!/usr/bin/perl

use strict;
use utf8;
use Storable;

#
# 把 中文字 轉成 注音
#
# note: 破音字只取第一音
#
# all input and output are using UTF-8
#
# execute:
# zh2bpmf.pl 2> nul > a.txt
#

# 需要的表格檔：
my $dfile = 'data/bpmf.dat';
my $tfile = 'data/big5-bopomofo-u8.txt';
my %bpmf = ();

#
# load bpmf hash data from $dfile (text) or $tfile (binary)
#
sub load_table
{
	# load hash if data file exists
	if (-e $dfile)  {
		%bpmf = %{ retrieve($dfile) };
		return;
	}

	my $cnt = 0;

	open my $ifh, $tfile or die;
	while ( <$ifh> )  {
		++ $cnt;
		$_ = decode("utf8", $_);
		s/[\r|\n]//;
		m/([\x{4E00}-\x{9FFF}])\s+
		  (\d)\s+
		  ([\x{0200}-\x{9FFF}]+)\s?
		 /x;
		#print ">",$1,">>",">>>",$3,"\n" if $1;
		#print "line: (",$_,")\n";
		#last if $cnt >4;
		if ($1 and $3)  {
			$bpmf{$1} = $3;
		}
	}
	close $ifh;

	# store %bpmf to file if no data file
	store(\%bpmf, $dfile);
}


sub main
{
	load_table;

	my $iff = $ARGV[0] || "zh.txt";
	print STDERR "read from $iff\n";
	open my $ifh, "<:utf8", $iff or die "please specify a input file name";

	binmode STDERR;
	binmode STDOUT;

	while (<$ifh>)  {
		foreach my $cc (split //, $_)  {
#			print $cc," ";
			if ($bpmf{$cc})  {
				print $bpmf{$cc};
			}
			else  {
				print $cc;
			}
		}
		print "\n";
	}
	close $ifh;
}

main;
