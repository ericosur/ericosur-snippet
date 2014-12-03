#!/usr/bin/perl

# to find lunar/animal year name for specified year

use strict;
use v5.10;

my @ten = qw(0 甲 乙 丙 丁 戊 己 庚 辛 壬 癸);
my @twelve = qw(0 子 丑 寅 卯 辰 巳 午 未 申 酉 戌 亥);
my @animal = qw(0 鼠 牛 虎 兔 龍 蛇 馬 羊 猴 雞 狗 豬);

sub lunar_to_solar($$)
{
	my ($x, $y) = @_;
	my ($lower, $upper) = (1800, 2100);
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
    # use default range to list animal year 7 (horse, MA)
	lunar_to_solar(1, 7);

    my ($maxy, $miny) = (2040, 1940);
	for (my $yy = $miny; $yy <= $maxy; $yy++) {
		solar_to_lunar($yy, 4); # rabbit (TU)
	}

	for (my $yy = $miny; $yy <= $maxy; $yy++) {
		solar_to_lunar($yy, 5); # dragon (LON)
    }
}

main;
