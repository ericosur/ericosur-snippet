#!/usr/bin/env perl

use Encode qw(from_to);
use feature 'say';

while (<DATA>) {
    $s = $_;
    $s =~ s/\\(\d{3})/pack("C", oct($1))/eg;
    from_to($s, "GB2312", "UTF-8");
    say $s;

}

__DATA__
\310\272\320\307.-.[\276\370\266\324\265\304\311\371\322\364-TAS.2009].\327\250\274\255.(Flac).cue
\310\272\320\307.-.[\276\370\266\324\265\304\311\371\322\364-TAS.2009].\327\250\274\255.(Flac).flac
