#!/usr/bin/perl

use strict;
use v5.10;

my @ten = qw(0 ¥Ò ¤A ¤þ ¤B ¥³ ¤v ©° ¨¯ ¤Ð ¬Ñ);
my @twelve = qw(0 ¤l ¤¡ ±G ¥f ¨° ¤x ¤È ¥¼ ¥Ó ¨» ¦¦ ¥è);
my @animal = qw(0 ¹« ¤û ªê ¨ß Às ³D °¨ ¦Ï µU Âû ª¯ ½Þ);

sub lunar_to_solar($$)
{
	my ($x, $y) = @_;
	my ($lower, $upper) = (1800, 1990);
	my $r = ($x - $y) * 5 + $x + 1803;

	if ($x - $y < 0) {
		$r += 60;
	}

	say $ten[$x], $twelve[$y], "(", $animal[$y], ") => ";
	say $r;

	while ($r > $lower && $r < $upper) {
		$r += 60;
		say $r;
	}
}

sub solar_to_lunar($$)
{
	my $year = shift;
	my $desire = shift;

	my ($x, $y) = ( ($year-3) % 10, ($year-3) % 12 );
	$x += 10 if ($x == 0);
	$y += 12 if ($y == 0);

	if ($desire == 0) {
		say $year, " => ", $ten[$x], $twelve[$y], " (", $animal[$y], ")";
	} elsif ($desire == $y) {
		say $year, " => ", $ten[$x], $twelve[$y], " (", $animal[$y], ")";
	}
}

sub main()
{
	my ($x, $y) = (1, 7);
	lunar_to_solar($x, $y);
	for (my $yy = 1900; $yy <= 2050; $yy++) {
		solar_to_lunar($yy, 5);
	}
}

main;
