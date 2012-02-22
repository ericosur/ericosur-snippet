#!/usr/bin/perl

#
# 顯示 cin 表格內：
#	輸入法名稱
#   cjk 字數
#	cjk ext A 字數
#	cjk ext B 字數
#	輸入法可輸出字數
#
# 以 tab 隔開...
# 可用 sed "s/\t/,/g" foo.txt > bar.csv
#

use strict;
use File::DosGlob 'glob';
use utf8;
use Encode;

my $output_table = 0;

my %count_range = ();
#
# U+4E00 ~ U+9FFF		cjk unified ideographs
# U+3400 - U+4DBF		cjk unified ideographs extension A
# U+20000 - U+2A6DF		cjk unified ideographs extension B
#
sub which_range($)
{
	my $cp = shift;
	if ($cp >= 0x4e00 && $cp <= 0x9fff)  {
		return "cjk";
	} elsif ($cp >= 0x3400 && $cp <= 0x4DBF)  {
		return "extA";
	} elsif ($cp >= 0x20000 && $cp <= 0x2A6DF)  {
		return "extB";
	} else  {
		return "misc";
	}
}


#
# output the unique charactersinto text file
#
sub save_char($$)
{
	my ($ofile, $r_data) = @_;
#	print "output to ", $ofile, "\n";
#	open my $ofh, ">", $ofile or die;
#	binmode $ofh, ":utf8";
	my $line_num = 0;
	my $codepoint;

	foreach (sort @{$r_data})  {
		$codepoint = ord($_);
#		printf $ofh "%X\n", $codepoint;
		$count_range{ which_range($codepoint) } ++;
	}
#	close $ofh;
}


sub show_range
{
	printf "%d\t%d\t%d\t%d\t",
		$count_range{'cjk'},
		$count_range{'extA'},
		$count_range{'extB'},
		$count_range{'misc'};
}


sub print_out($)
{
	my $href = shift;
	my %hh = %{$href};
	# print hash and array ref within it
	my @tmp = sort { scalar(@{$hh{$b}}) <=> scalar(@{$hh{$a}}) } keys %hh;
	for my $ii (1..scalar @tmp)  {
		next if (not $tmp[$ii]);
		print $tmp[$ii], "\t";	# 字
		print scalar @{$hh{$tmp[$ii]}}, "\t";	# 字根數
		print join(',', @{$hh{$tmp[$ii]}});	# 字根列表
		print "\n";
	}
}


#
# main procedure
#
sub main
{

	my $arg = $ARGV[0] || "*.cin";
#	my (%left, %right) = ();
	my @files = glob $arg;
	#foreach my $fname (@files)  {
	#    print "$fname\n";
	#}

	print "IME\tcjk\textA\textB\tmisc\ttotal\n";
	foreach my $ff (@files)  {
		next if not -e $ff;
		print "$ff\t";
		open my $ifh, $ff or die "$!";
		my $flag = 0;
		my $cnt = 0;
		my %right = ();
		my %left = ();
		my $line;
		%count_range = ();

		while (<$ifh>)  {
			next if m/^#/;
			$line = decode("utf8", $_);
			if ( $line =~ m/%chardef\s+begin/ )  {
				$flag = 1;
	#			print "begin\n";
				next;
			}
			if ($flag == 1)  {
				++ $cnt;
				$line =~ m/^(\w+)\s(.*)/;
				push( @{$right{$2}}, $1 );
				push( @{$left{$1}}, $2 );
				next;
			}
			if ( $line =~ m/%chardef\s+end/ )  {
				$flag = 0;
	#			print "end\n"
				next;
			}
		}	# while (<$ifh>)  { ...
		close $ifh;
		my @rchar = keys %right;
		save_char(${ff}.'.txt', \@rchar);
		show_range;
		print scalar @rchar;
	#	print "$cnt\n";	# total lines
		print "\n", '-'x80, "\n";

		binmode STDOUT, ":utf8";

		# 列出字與它的字根 (由字根數大的優先)
		print_out( \%right );

		print "\n", '-'x80, "\n";

		# 列出字根與輸出的字 (由字數多的優先)
		print_out( \%left );

	}	# foreach (...)

}

main;

