#!/usr/bin/perl
# Yen-Ming Lee <leeym@leeym.com>
# 2007/01/09

# copy/paste from http://plog.longwin.com.tw/programming/2007/01/12/y_dictionary_script_2007
# http://fourdollars.blogspot.com/2007/01/blog-post.html

use strict;

use Encode qw(encode decode from_to);
use Term::ANSIColor qw(:constants);
use Data::Dumper;
use LWP::Simple;


sub dummy_test($)
{
	my $arg = shift;
	print $arg,"\n";
}

sub ydict($)
{
	my $p = shift;
	die if !$p;
	my $html = get("http://tw.dictionary.yahoo.com/search?p=$p");
	from_to($html, "utf-8", "big5") if $ENV{'LC_CTYPE'} =~ /Big5/;
	my $i = 0;
	$html =~ s/\r//g;
	$html =~ s/\n//g;
	if ($html =~ m{<em class="warning">})
	{
		if ($html =~ m{<em class="warning">.*?>(\S+)<.*?</em>})
		{
			my $q = $1;
			print BOLD . YELLOW . "\nERROR: $p -> $q\n" . RESET;
			return ydict($q);
		}
		else
		{
			print BOLD . YELLOW . "ERROR: $p\n" . RESET;
			return;
		}
	}
	print BOLD . YELLOW . "\n$p\n" . RESET;
	while ($html =~ m{<div class=p(\w+)>(.*?)</div>}i)
	{
		my ($type, $line) = ($1, $2);
		$html = $';		#'
		my $color;
		my $bold = BOLD;
		my $reset = RESET;
		$line =~ s/^\s+//;
		$line =~ s/\s+$//;

		if ($type eq 'cixin')
		{
			$i = 0;
			$color = BOLD . RED;
		}
		elsif ($type eq 'chi' or $type eq 'eng')
		{
			$color = CYAN;
			$reset = RESET . $color;
			$line = "\t$line";
		}
		elsif ($type eq 'explain')
		{
			$i++;
			$line = "$i $line";
		}
		else
		{
			$color = BOLD . BLUE;
			next;
		}
		$line =~ s,<b>,$bold,g;
		$line =~ s,</b>,$reset,g;
		$line =~ s/<[^>]+>//g;
		print $color . "$line\n" . RESET;
	}
	print "\n";
}

sub main()
{
	if (not @ARGV)  {
		die "should specify one word to lookup!";
	}

	while (@ARGV)  {
		ydict(shift @ARGV);
#		dummy_test(shift @ARGV);
	}
}

main;
