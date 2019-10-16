#!/usr/bin/perl
# display the ascii code

$mm = "a";

# ord() return the ascii value of one char
printf "ord('%s') = %s\n", $mm, ord($mm);

# hex() return the value of the hex digits
printf "hex('%s') = %d\n", $mm, hex($mm);

$mm = "0x1F";
printf "hex('%s') = %d\n", $mm, hex($mm);

$mm = "01F";
printf "hex('%s') = %d\n", $mm, hex($mm);

$mm = "1F";
printf "hex('%s') = %d\n", $mm, hex($mm);

#binmode(STDIN, ':encoding(utf8)');
binmode(STDOUT, ':encoding(utf8)');
print chr(0x4e00);
