#!/usr/bin/perl
#
# use WWW::Mechanize to query yahoo dictionary
#
# It would be go crazy under win32 if ''use encoding 'utf-8' ''
# But it would be warning "wide character in print ..." under linux
#

use strict;
use warnings;

use WWW::Mechanize;
use Encode qw(from_to encode decode);
#use Encode::Guess;


sub yahoo_dict_query($);

sub yahoo_dict_query($)
{
	my $str = shift;
	#my $http = "http://tw.dictionary.yahoo.com/search?ei=UTF-8&p=$str";
	my $http = "http://tw.dictionary.yahoo.com/search?p=$str";
	my $mech = WWW::Mechanize->new();
	$mech->get($http);
	my $r = "";

	my $html = $mech->content();

	if ( $^O eq 'MSWin32' )  {
		#my $enc = guess_encoding($html, qw/big5-eten utf8/);
		# guess the encoding
		$html = encode ("big5", decode("UTF-8", $html));
		#from_to($html, "UTF-8", "big5");
	}

#
# get rip off the following RE from result
#
# the following dissecting code from ydict.pl by Yen-Ming Lee <leeym@leeym.com>
#
	$html =~ s/\r//g;
	$html =~ s/\n//g;

	if ($html =~ m{<em class="warning">})  {
		if ($html =~ m{<em class="warning">.*?>(\S+)<.*?</em>})  {
			my $q = $1;
			print "ERROR: $str -> $q\n";
			return yahoo_dict_query($q);
		}
		else  {
			print "ERROR: $str\n";
			return "Error";
		}
	}
	$r = $r . "$str\n";

	my $i = 0;
	while ($html =~ m{<div class=p(\w+)>(.*?)</div>}i)  {
		my $type = $1;
		my $line = $2;
		$html = $';		#'
		$line =~ s/^\s+//;
		$line =~ s/\s+$//;

		if ($type eq 'cixin')  {
			$i = 0;
		}
		elsif ($type eq 'chi' or $type eq 'eng')  {
			$line = "\t$line";
		}
		elsif ($type eq 'explain')  {
			$i++;
			$line = "$i $line";
		}
		else  {
			next;
		}
		$line =~ s/<[^>]+>//g;
		$r = $r . $line . "\n";
	}
	$r = $r . "\n";
	return $r;
}


sub main()
{
	unless (@ARGV)  {
		print "usage: $0 <string1> [string2 ...]\n";
		exit;
	}
	foreach my $par (@ARGV)  {
		my $result = yahoo_dict_query($par);
		print $result;
	}
}

main();

=pod

=head1 NAME

mydict.pl

=head1 SYNOPSIS

mydict.pl <word1> [word2 word3 ...]

=head1 DESCRIPTION

Use yahoo! dictionary to query word.

=cut
