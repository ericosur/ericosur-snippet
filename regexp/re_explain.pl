#!/usr/bin/perl

#
# Dec 16 2007 by ericosur
#

use strict;
use warnings;
use YAPE::Regex::Explain;

my $re_str = $ARGV[0] || qr((?<!\.\d)(?<=\d)(?=(?:\d\d\d)+\b)/,);
my $exp_str = YAPE::Regex::Explain->new( $re_str )->explain;

print $exp_str;

=pod

=head1 NAME

explain_re.pl

=head1 SYNTAX

explain_re [regular expression string]
If no argument specified, a default RE string would be used.

=head1 REQUIREMENT

need install YAPE::Regex and YAPE::Regex::Explain

=head1 NOTE

Idea from the book __Mastering Perl__

=cut
