#!/usr/bin/perl

#
# This script is saved as:
# (1) ASCII
# You would got the error at line 10.
#
# (2) UTF8
# The length of $a would be 2 characters.
# And the $a would be internally encoding as Unicode.
#

use Unicode::String qw(utf8 latin1 utf16);
use utf8;

$a = "國1";

printf "length = %d\n", length($a);

for ($i = 0; $i < length($a); $i++)  {
	printf "%x ", ord(substr($a, $i, 1));
}

print "is utf8?\t";
print utf8::is_utf8($a) ? "yes" : "no", "\n";

#
# the character 國
# big5: B0EA
# unicode: 570B
# UTF8: e5 9c 8b
#
