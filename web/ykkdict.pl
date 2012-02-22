#!/usr/bin/perl
# Shih-Yuan Lee <fourdollars@gmail.com>
# http://fd.idv.tw

# reference from
# http://blog.nahoya.com/archives/2007_08/168
# this script need support UTF-8 and ANSI
#

use Term::ANSIColor qw(:constants);
use LWP::Simple;
use strict;
use warnings;
use Encode;

my $debug = 0;
my $trigger = 0;

if ($#ARGV == -1) {
	print "<Yahoo!奇摩字典> ";
	while (<>) {
		chomp;
		if ("$_" eq '') {
			print "<Yahoo!奇摩字典> ";
			next;
		}
		ydict($_);
		print "<Yahoo!奇摩字典> ";
	}
} else {
	while ($#ARGV != -1) {
		if ($trigger) {
			print "\n";
		} else {
			$trigger = 1;
		}
		ydict(shift);
	}
}

sub ydict
{
	my $p = shift;
	die if !$p;
	my $html = get("http://tw.dictionary.yahoo.com/search?ei=UTF-8&p=$p");
	$html =~ s/\r//g;
	$html =~ s/\n//g;

	if ($html =~ m{<em class="warning">}) {
		if ($html =~ m{<em class="warning">.*?>(\S+)<.*?</em>}) {
			my $q = $1;
			print BOLD . YELLOW . "拼字檢查: $p -> $q" . RESET . "\n\n";
			return ydict($q);
		} else {
			print BOLD . YELLOW . "查無此字: $p\n" . RESET;
			return;
		}
	}

	print BOLD . YELLOW . "$p 的查詢結果:" . RESET . "\n\n";

	while ($html =~ m{<div class="break"></div>}) {
		my $block = $`;
		$html = $';
		parser($block);
	}
	parser($html);
}

sub parser
{
	my $html = shift;
	if ($html =~ m{<h2>(.*?)</h2>}) {
		my $line = $1;
		$line =~ s,<sup>,[,g;
		$line =~ s,</sup>,],g;
		$line =~ s/<[^>]+>//g;
		$line =~ s/^\s+//;
		$line =~ s/\s+$//;
		print "<h2>" if $debug;
		print BOLD."$line".RESET."\n";
	}
	parsermore($html);
}

sub parsermore
{
	my $i = 0;
	my $flag = 0;
	my $html = shift;
#	http://tw.dictionary.yahoo.com/search?ei=UTF-8&p=$p
	while ($html =~ m{<div class="?(p\w+|chinese-explain pexplain|chinese)"?>(.*?)</div>}i)
	{
		my $type = $1;
		my $line = $2;
		my $color = RESET;
		my $bold = BOLD;
		my $reset = RESET;
		$html = $';
		$line =~ s/^\s+//;
		$line =~ s/\s+$//;
		print "type=$type\nline=$line\n" if $debug;
		if ($type eq 'pcixin')
		{
			$flag = 0;
			$i = 0;
			$color = BOLD . RED;
			next if not ($line);
			print "<pcixin>\n" if $debug;
		}
		elsif ($type eq 'pchi')
		{
			$color = GREEN;
			$reset = RESET.$color;
			$line = "        $line";
			print "<pchi>\n" if $debug;
		}
		elsif ($type eq 'peng')
		{
			$color = CYAN;
			$reset = RESET.$color;
			$line = "        $line";
			print "<peng>\n" if $debug;
		}
		elsif ($type eq 'chinese')
		{
			my $num = $line =~ s/<br>/\n    /g;
			$line = "    $line";
			print "<chinese>\n" if $debug;
		}
		elsif ($type eq 'pexplain')
		{
			if ($flag == 0) {
				$i++;
				if ($line =~ m{<li>}) {
					my $reval;
					do {
						$reval = $line =~ s/<li>/    $i. /;
						$i++;
					} while ($reval);
					my $num = $line =~ s/<br>/\n/g;
					$i = 0;
				} else {
					$line = "    $i. $line";
					print "<pexplain 1>\n" if $debug;
				}
			} else {
				$line = "    $line" if ($line);
				print "<pexplain 2>\n" if $debug;
			}
		}
		elsif ($type eq 'chinese-explain pexplain')
		{
			if ($flag == 0) {
				$i++;
				if ($line =~ m{<li>}) {
					my $reval;
					do {
						$reval = $line =~ s/<li>/\n    $i. /;
						$i++;
					} while ($reval);
					my $num = $line =~ s/<br>/\n/g;
					$i = 0;
				} else {
					$line = "    $i. $line";
					print "<pexplain 1>\n" if $debug;
				}
			} else {
				$line = "    $line" if ($line);
				print "<pexplain 2>\n" if $debug;
			}
		}
		elsif ($type eq 'ptitle')
		{
			$flag = 1;
			$color = BOLD . BLUE;
#			next if ($line =~ m{KK} && $line =~ m{DJ});

			my $dir = 'http://l.yimg.com/f/i/tw/dictionary/pic/';
			my $map = Encode::decode('utf8', " æa:   ɑ       ʊɔɝəɚʌeɛŋ ʃʒ θð   iɪuopbtdkfvszmnhlrwj`,g ḷṃṇ");

			$line =~ s/\s+(DJ)/\n$1/g;

			while ($line =~ m{<img[^>]*['"]$dir/0+(\d+)\.gif['"][^>]*>}ig) {
				my $char = Encode::encode('utf8', substr($map, $1, 1));
				my $fname = $1 < 10 ? "00$1" : $1 < 100 ? "0$1" : $1;
				$line =~ s!<img[^>]*['"]$dir/$fname\.gif["'][^>]*>!$char!ig;
			}

			print "<ptitle>\n" if $debug;
		}
		else
		{
			$color = BOLD . BLUE;
			print "<others>\n" if $debug;
			next;
		}
		$line =~ s,<b>,$bold,g;
		$line =~ s,</b>,$reset,g;
		$line =~ s,<sup>,[,g;
		$line =~ s,</sup>,],g;
		$line =~ s/<[^>]+>//g;
		print $color."$line".RESET."\n";
	}
}
