#!/usr/bin/perl -w

# reference from http://www.perlmonks.org/index.pl?node_id=401098


use strict;
use bignum qw(hex);

#my @alphanum = (0 .. 9, "a" .. "z", "A" .. "Z");
my @alphanum = (0 .. 9, "a" .. "z");
my $divisor = scalar @alphanum;

#my $enc = &enc(1_000);
#my $dec = &dec($enc);
#print "$enc $dec\n";

#my $hexstr = "0x6d9e9aba8b2e11473c947e859d6e740a";
my $hexstr = "0xfffffffffffffffffffffffff";
my $x = hex($hexstr);
my $b62 = enc($x);

print "hex: ", $hexstr, ", len = ", length($hexstr), "\n";
print "base62: ", $b62, ", len = ", length($b62), "\n";

exit 0;

sub dec {

  my $num = shift;

  # strip leading 0's
  $num =~ s/$0+//g;

  my ($y, $result) = (0, 0);

  foreach (split(//, reverse($num))) {
    my $found = 0;

    foreach my $item (@alphanum) {
      if ($item eq $_) {
        last;
      }
      $found++;
    }

    my $temp = $found * ($divisor ** $y);
    $result += $temp;
    $y++;
  }

  return $result;
}

sub reduce {
  return (int($_[0] / $divisor), $_[0] % $divisor);
}

sub enc {

  my $num = shift;
  my $end = "";

  my ($a, $b) = reduce($num);
  $end = $alphanum[$b] . $end;
  until ($a < $divisor) {
    ($a, $b) = reduce($a);
    $end = $alphanum[$b] . $end;
  }

  $end = $alphanum[$a] . $end unless $a == 0;

  return $end;
}
