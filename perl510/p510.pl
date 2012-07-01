use v5.10;

$a = 0;
$b = 10;

$c = $a || $b;
say $c;

# same as $c = ( defined($a) ? $a : $b );
$c = $a // $b;
say $c;
