#!/usr/bin/perl

# -*- coding: utf-8 -*-

#
# 一、到中央氣象局抓取目前天氣觀測的 pdf 檔
# 二、將 pdf 轉為純文字檔
# 三、利用 regexp 抓取我要的文字，並印出
#
# 需要 CAM::PDF 安裝附帶的 pdftotext 轉換 pdf 成 text 格式

use strict;
use warnings;
use WWW::Mechanize;

sub fetch_pdf()
{
	my $mech = WWW::Mechanize->new( autocheck => 1 );
	# 偽裝為 IE6
	$mech->agent_alias( 'Windows IE 6' );

	my $url = q(http://www.cwb.gov.tw/V5/forecast/taiwan/Data/W31.pdf);

	my $file = 'tmp.pdf';	# default name
	if ( $url =~ m!\/([^/]+)$! )  {
		$file = $1 if $1;
		$file = lc($file);
	}
	#print "file: ", $file,"\n";
	$mech->get($url, ":content_file" => $file);

	return $file;
}

# call ''pdftotext'' come with CAM::PDF
# also need poddler-data package for CJK pdf
sub pdf_to_text($)
{
	my $ifile = shift;
	my $ofile = $ifile;

	$ofile =~ s!\.pdf!\.txt!i;
	my $cmd = 'pdftotext -layout ' . $ifile . ' ' . $ofile;
	system $cmd;
	return $ofile;
}


sub get_wanted_line($)
{
	my $file = shift;
	my $line;
	my $otime;

	open my $fh, $file or die;
	while ( <$fh> ) {
		s/[\r\n]//;
		if ( m/觀測時間/ )  {
			s/\\//;
			$otime = $_;
			next;
		}
		if ( m/台\s+北/ )  {
			s/台\s+北/台北\t/;
			$line = $_;
			$line =~ s!				# to parse ''20.1(+3.5)''
				(
					-?\d*\.\d+			# 20.1
				)
				\(
					\s*
						([+-]\d+\.\d+)	# +3.5
					\s*
				\)
				!
					\t$1\($2\)
				!x;
			#printf("<%s>\t<%s>\n", $1, $2);
			$line =~ s/\s{2,}/\t/g;
			last;
		}
	}
	close $fh;

	return unless $line;	# cannot get proper data
	#print $line;
	my @a = split /\t/, $line;
	print $otime, "\n";
	printf("站名: %s\n風向: %s\n風力: %s\n陣風: %s\n能見度: %s\n氣溫: %s\n濕度: %s
氣壓: %s\n天氣: %s\n累積雨量: %s\n", $a[0], $a[1], $a[2], $a[3], $a[4], $a[5], $a[6],
		$a[7], $a[8], $a[9]);
}


sub main
{
	my $ofile = fetch_pdf();
	my $textfile = pdf_to_text($ofile);
	get_wanted_line($textfile);
}

main;
