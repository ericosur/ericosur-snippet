#!/usr/bin/perl -w

#
# small perl/tk demo
# 2006/12/27 by ericosur
#

use Tk;

my $mw = MainWindow->new;
$mw->title("Good Window");
$mw->Label(-text => "This window looks much more organized, and less haphazard\n" .
	"because we used some options to make it look nice")->pack;

$mw->Button(-text => "Exit",
	-command => sub { exit })->pack( -side => 'bottom',
									-expand => 1,
									-fill => 'x');
$mw->Checkbutton(-text => "I like it!")->pack(-side => 'left',
											-expand => 1);
$mw->Checkbutton(-text => "I hate it!")->pack(-side => 'left',
											-expand => 1);
$mw->Checkbutton(-text => "I don't care")->pack(-side => 'left',
											-expand => 1);


MainLoop;
