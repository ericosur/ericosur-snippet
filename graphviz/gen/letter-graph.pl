#!/usr/bin/perl

use strict;
use warnings;
use v5.10;
use Data::Dump qw(dump);

my $fh;

sub print_letter($)
{
	my $letter = shift;
	$letter = lc $letter;
	my @array = split //, $letter;
	my $sz = scalar @array;

	dump(@array);

	my $mm = $array[0];
	my $nn;
	if ($sz == 1)  {
		$nn = $mm;
	}
	else  {
		$nn = $array[1];
	}
	print $fh "\t$mm -> $nn [color = blue];\n";

#	print "\t$nn -> ", join("->", @array), ";\n";
	for (my $i=1; $i+1 < scalar @array; $i ++)  {
		$mm = $array[$i];
		$nn = $array[$i+1];
		print $fh "\t$mm -> $nn;\n";
	}
}

sub main()
{
	my $ofdot = 'tmp.dot';
	my $ofpng = 'word.png';

	my $v_color = 'red';
	my $v_shape = 'egg';

	my $alpha = $ARGV[0] || qw{localization};

	open $fh, ">$ofdot" or die;

	print $fh <<EOF;
// this dot is engerated by $0
digraph g {

	node [fontsize = 12 shape = circle fontname = "Lucida Console Bold"];
	edge [labelfontsize="10" fontsize="8"];

	label = "$alpha";
	a [shape = $v_shape style = dashed color = $v_color label = "a"];
	e [shape = $v_shape style = dashed color = $v_color label = "e"];
	i [shape = $v_shape style = dashed color = $v_color label = "i"];
	o [shape = $v_shape style = dashed color = $v_color label = "o"];
	u [shape = $v_shape style = dashed color = $v_color label = "u"];

	{ rank = same; a; e; i; o; u; }

EOF

	print_letter($alpha);
	print $fh "}\n";
	close $fh;
	print "output to $ofdot\n";

	my $cmd = "dot -Tpng -o $ofpng $ofdot ";
	print "image: $ofpng\n";
	system $cmd;
}

main;
