#! /usr/bin/perl -w

# reference from: http://blog.wu-boy.com/2009/07/01/1492/
# to solve the croak ''Wide character in print with UTF-8 mode''

use Carp;
use File::Basename;
use LWP::Simple;
use WWW::Mechanize;
use LWP::UserAgent;
use WWW::Shorten '0rz';
use Getopt::Std;
use DBI;
use utf8;

binmode(STDIN, ':encoding(utf8)');
binmode(STDOUT, ':encoding(utf8)');
binmode(STDERR, ':encoding(utf8)');
if($_ =~ m/\s*<div\s*class="title"><a\s*href=".+">(.+)<\/a><\/div>\s*/)
{
	$pic_desc = $1;
	print "desc: " . $1 . " \n" if $verbose;
}
