#!/usr/bin/perl -w

#
# perk/tk small test
#
# 2006/12/27 by ericosur
#

use strict;
use warnings;

use encoding 'big5', STDIN => 'big5', STDOUT => 'big5';
use Tk;
use Tk::Font;

my $line = "����r";

my $mw = MainWindow->new;


$mw->Label(
	-text => $line,
	-font => 'mingti16',
)->pack;

$mw->Button(
    -text    => 'Quit',
    -command => sub { exit },
)->pack;

MainLoop;

__END__;
#!/usr/local/bin/wish8.3
tk useinputmethods 1
font create bsmilpfont -family "ar pl mingti2l big5" -size 16
label .a -text "����" -font bsmilpfont
pack .a
button .b -text "���s" -command { puts stdout $cc; exit } -font bsmilpfont
pack .b
entry .c -textvariable cc -font bsmilpfont
pack .c
