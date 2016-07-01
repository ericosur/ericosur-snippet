use strict;

my %var = ();
$var{'int'} = 123;
$var{'array'} = [1, 2, 3, 4];
$var{'hash'} = {1 => 2, 3 => 4};
$var{'name'} = 'Cindy';
$var{'sub'} = sub { print "Hi! $_[0]! ^^\n" };
$var{'sub2'} = sub { print "Bye Bye, $_[0]. ^_^\n" };

$var{'sub'}($var{'name'});
$var{'sub2'}($var{'name'});
