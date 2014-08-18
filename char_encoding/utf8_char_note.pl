#!/usr/bin/perl

#use Unicode::String qw(utf8 latin1 utf16);
#use utf8;

use lib 'd:/ericosur-google';
use Ericosur;

$a = "國1";
hexdump($a);
sep();

#print utf8::is_utf8($a) ? "yes" : "no", "\n";

use Unicode::String qw(utf8 latin1 utf16);
#use utf8;

$a = "國1";
hexdump($a);
sep();


=pod

=head1 NAME

utf8_char_note.pl

=head1 DESCRIPTION

Save this file as ASCII or UTF8 encoding then run it to see the hexdump.

=cut
