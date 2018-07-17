use strict;
use v5.10;
no if $] >= 5.018, warnings => qw( experimental::smartmatch );

#http://www.slideshare.net/acme/whats-new-in-perl-510

my @items = qw(apple ball cat dog egg);

foreach (@items)  {
    when (/apple/)  { say "apple is cool" }
    when (/ball/)   { say "playing ball is funning" }
    when (/cat/)    { say "catty kitty cat" }
    when (/dog/)    { say "wanwan!" }
    say "$_ cannot match!";
}

my $x = 'cat';
say "yeah $x in items!" if ($x ~~ @items);

my %hash = (a => 'apple', b => 'ball', c => 'cat');
$x = 'c';
say "yeah $x in hash keys!" if ($x ~~ %hash);