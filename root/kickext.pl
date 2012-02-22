#!/usr/bin/perl
=pod

=head1 SYSNOPSIS

just kick '.pl' off

=head1 USAGE

dir *.pl | perl -p q.pl

=head1 NOTE

One liner usage:

dir *.pl /b | perl -pe "s[\.pl][]"

another non sense one-liner
dir *.jpg /b | perl -pe "s[IMG_(\d+)\.JPG][$1]i"

dir /b *.pl | perl -npe "s/\.pl//;"

=cut

# code here
#    chomp;
    s/\.pl//;
#    print "$_\n";

