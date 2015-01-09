#!/usr/bin/env perl

# demo Term::ANSIColor

use strict;
use Term::ANSIColor;

print color 'bold green';
print "This text is bold green\n";
print color 'bold blue';
print "This text is bold blue.\n";
print color 'reset';
print "This text is normal.\n";
print colored ("Yellow on magenta.", 'yellow on_magenta'), "\n";
print "This text is normal.\n";
print colored ['yellow on_magenta'], 'Yellow on magenta.';
print "\n";
