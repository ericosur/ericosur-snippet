#!/usr/bin/perl
=pod

=head1 DESCRIPTION

1. convert C++ comment to C style

2. strip all C comment

3. convert C<0xAB> into binary

=head1 REFERENCE

perl faq 4.27
http://www.perl.com/doc/FAQs/FAQ/oldfaq-html/Q4.27.html

=cut

$/ = undef;
$_ = <>;

# the following regexp would replace c++ style comment into c style comment
s[//(.*)|/\*[^*]*\*+([^/*][^*]*\*+)*/|"(\\.|[^"\\])*"|'(\\.|[^'\\])*'|[^/"']+]
 [$1 ? "/*$1 */" : $&]gex;

#'

# strip all c style comment out
s[/\*[^*]*\*+([^/*][^*]*\*+)*/|([^/"']*("[^"\\]*(\\[\d\D][^"\\]*)*"[^/"']*|'[^'\\]*(\\[\d\D][^'\\]*)*'[^/"']*|/+[^*/][^/"']*)*)][$2]g;

#"

s/[\x0d\x0a]//g;
s/0x([a-fA-F0-9]{2}),?\s*/pack("C", hex($1))/eg;

print;
