#!/usr/bin/perl
#
# rgb
#

sub b888($)
{
	my $p = shift;
	return ((($p) << 24) >> 24);
}

sub g888($)
{
	my $p = shift;
	return ((($p) << 16) >> 24);
}

sub r888($)
{
	my $p = shift;
	return ((($p) << 8) >> 24);
}

sub r888($)
{
	my $p = shift;
	return ((($p) << 8) >> 24);
}

# rgb565
sub r565($)
{
	my $p = shift;
	return ($p >> 11);
}
sub g565($)
{
	my $p = shift;
	return (($p << 21) >> 26);
}
sub b565($)
{
	my $p = shift;
	return (($p << 27) >> 27);
}
sub rh565($)
{
	my $p = shift;
	return ($p >> 27);
}
sub gh565($)
{
	my $p = shift;
	return (($p << 5) >> 26);
}
sub bh565($)
{
	my $p = shift;
	return (($p << 11) >> 27);
}

sub rgb888_to_rgb565($)
{
	my $p = shift;
	my $r = 0;
	$r = b888($p) >> 3;
	$r += (g888($p) >> 2) << 5;
	$r += (r888($p) >> 3) << 11;
	return $r;
}

sub rgb565_to_rgb888($)
{
	my $p = shift;
	my $r;
	my $c;
	$c = b565($p);
	$r = ($c << 3) | ($c & 0xc7);
	$c = g565($p);
	$r += (($c << 2) | ($c & 0x03)) << 8;
	$c = r565($p);
	$r += (($c << 3) | ($c & 0x07)) << 16;
	return $r;
}

my $val = 0xfcff00;
printf("%06x %02x,%02x,%02x\n", $val, r888($val), g888($val), b888($val));
my $chg = rgb888_to_rgb565($val);
printf("%06x => %04x\n", $val, $chg);
printf("%04x => %06x\n", $chg, rgb565_to_rgb888($chg));
$chg = 0xe847;
printf("%04x => %06x\n", $chg, rgb565_to_rgb888($chg));
$chg = 0xdefa;
printf("%04x => %06x\n", $chg, rgb565_to_rgb888($chg));
$chg = 0xfade;
printf("%04x => %06x\n", $chg, rgb565_to_rgb888($chg));
$chg = 0x12A5;
printf("%04x => %06x\n", $chg, rgb565_to_rgb888($chg));
$chg = 0xA512;
printf("%04x => %06x\n", $chg, rgb565_to_rgb888($chg));
