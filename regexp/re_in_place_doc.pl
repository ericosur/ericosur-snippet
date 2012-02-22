#!/usr/bin/perl
#
# demo the in-script data and parsing in place
#
# here doc, here document

#
# 2007/11/14 by ericosur
#

my @lines = ( << "EOL" =~ /^\s*(.+)/gm );
	I sit beside the fire and think
	of all that I have seen,
	of meadow-flowers and butterflies
	and summers that have been;
EOL

print join("\n", @lines), "\n";
print '-'x40,"\n";

print <<"EOF" =~ /^\s*\|\s+(.*\n)/g;
	|	Attention criminal slacker, we have yet
	|	to receive payment for our legal services.
	|
	|	Love and kisses
	|
EOF

print '-'x40,"\n";

     print <<FOO =~ /^\s+(.*\n)/g;
             Attention, dropsied weasel, we are
             launching our team of legal beagles
             straight for your scrofulous crotch.

                     xx oo
FOO

__DATA__;
I sit beside the fire and think...
by J. R. R. Tolkien

I sit beside the fire and think
of all that I have seen,
of meadow-flowers and butterflies
In summers that have been;

Of yellow leaves and gossamer
in autumns that there were,
with morning mist and silver sun
and wind upon my hair.

I sit beside the fire and think
of how the world will be
when winter comes without a spring
that I shall ever see.

For still there are so many things
that I have never seen:
in every wood in every spring
there is a different green.

I sit beside the fire and think
of people long ago,
and people who will see a world
that I shall never know.

But all the while I sit and think
of times there were before,
I listen for returning feet
and voices at the door.
