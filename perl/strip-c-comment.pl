#!/usr/bin/perl
=pod

=head1 NOTE

regular expressions copied from perl faq 4.27
http://www.perl.com/doc/FAQs/FAQ/oldfaq-html/Q4.27.html

use stdin and stdout
=cut

use strict;

$/ = undef;
$_ = <>;

# the following regexp would replace c++ style comment into c style comment
s[//(.*)|/\*[^*]*\*+([^/*][^*]*\*+)*/|"(\\.|[^"\\])*"|'(\\.|[^'\\])*'|[^/"']+]
 [$1 ? "/*$1 */" : $&]gex;

#'

# strip all c style comment out
s[/\*[^*]*\*+([^/*][^*]*\*+)*/|([^/"']*("[^"\\]*(\\[\d\D][^"\\]*)*"[^/"']*|'[^'\\]*(\\[\d\D][^'\\]*)*'[^/"']*|/+[^*/][^/"']*)*)][$2]g;

#"

print;
