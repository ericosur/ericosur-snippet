#!/usr/bin/perl
#
# data section: stroke data from unihan.txt
# read from stroke_range.txt (the output from stroke_range.pl)
# and add unihan stroke data to last column
# output to terminal
#

use strict;
use warnings;

my %unihan_strokes = ();

sub load_unihan_stroke_table()
{
	my $debug = 0;
	my ($icount, $fcount) = (0, 0);
    my $iff = 'new/extract_ktotalstrokes.txt';

    open my $ifh, $iff or die;
	while (<$ifh>)  {
		next if m/^$/;
		next if m/^#/;

		++$icount;
		# U+3400	kTotalStrokes	5
		my ($uni, $strokes) = (
				m/(U\+[0-9A-Fa-f]{4,})\s+
				kTotalStrokes\s+
				(\d+)
				/x
		);

		if ($uni && $strokes)  {
			print "<$uni> => <$strokes>\n" if $debug;
			$unihan_strokes{$uni} = $strokes;
			++ $fcount;
		}
		print STDERR "$fcount / $icount\r";
	}
}

sub check_file()
{
	my $ifile = q(stroke_range.txt);
	my $debug = 0;
	open my $ifh, $ifile or die;
	print STDERR "input: $ifile\n";

	print "#bigfive\tunicode\tbigchar\tbig5stroke\tunihanstroke\n";
	while ( <$ifh> )  {
		next if m/^#/;
		next if m/^$/;

		my $line = $_;
		$line =~ s/[\r\n]//;
		my ($ucs2, $old_stroke) = ( $line =~ m/0x....\s+(0x....)\s+..\s+(\d+)/ );
		$old_stroke = -1 if (!$old_stroke);
		$ucs2 =~ s/0x/U\+/;
		print "[$ucs2] -> [$old_stroke]\n" if $debug;

		if ($unihan_strokes{$ucs2})  {
			if ($unihan_strokes{$ucs2} != $old_stroke) {
			    printf "%s\t%d\t%s\n", $line, $unihan_strokes{$ucs2},
			        (($unihan_strokes{$ucs2} != $old_stroke) ? '???' : ' ');
		    }
		} else  {
			#print $line, "\n";
			#printf "%s\tn/a\n", $line;
		}

	}
	close $ifh;
}

#
# main procedure here
#
sub main
{
	print STDERR "load_unihan_stroke_table(): \n";
	load_unihan_stroke_table();
	print STDERR "check_file(): \n";
	check_file();
}

main;
