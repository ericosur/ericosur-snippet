#!/usr/bin/perl
#
# use WWW::Mechanize to query yahoo dictionary
#

use strict;
use warnings;

use WWW::Mechanize;
use Encode;
use Encode::Guess;

sub main()
{
	my $str = $ARGV[0] || "paranoid";
	my $result = yahoo_dict_query($str);
	print $result;
}

sub yahoo_dict_query()
{
	my $str = shift;
	my $http = "http://tw.dictionary.yahoo.com/search?ei=UTF-8&p=$str";
	my $mech = WWW::Mechanize->new();
	$mech->get($http);

	# guess the encoding
	my $enc = guess_encoding($mech->content(), qw/big5-eten utf8/);
	my $html = encode ("big5-eten", decode($enc->name, $mech->content()));

#
# get rip off the following RE from result
#
	# kill the java script section
	$html =~ s/<script.+?<\/script>//sgx;
	# kill the html tags
	$html =~ s/<[^>]*>//g;
	# kill the blank line more than 2
	$html =~ s/\n{2,}/\n/sg;
	# eat the space more than 2
	$html =~ s/\s{2,}(\n|\S)/$1/sg;
	# eat the extra unnecessary paragraphy
	$html =~ s/&raquo.*//s;
	$html =~ s/.*段落翻譯//s;
	$html =~ s/您是不是還想知道.*//s;
	$html =~ s/相似字詞.*//s;

	return $html;
}

main();

=pod

=head1 NAME

www-yahoo-dict.pl

=head1 SYNOPSIS

www-yahoo-dict.pl chrysanthemum
www-yahoo-dict.pl quadrennium
www-yahoo-dict.pl <word-to-query>

=head1 DESCRIPTION

Use yahoo! dictionary to query word.

=cut
