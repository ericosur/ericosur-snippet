#!/usr/bin/perl
# KAKE PAD (kPad) version 4.3.1
# A few new faetures added to the core and some via plugin

use Tk;
use Tk::DialogBox;
use Tk::Entry;
use Tk::Label;
use Tk::Scrollbar;
use Tk::Text;
use Tk::Menu;
use Tk::Frame;
use Tk::DialogBox;
use Tk::Menubutton;
use Tk::Button;
use Tk::Radiobutton;
use File::Glob;
use File::Find;
use FileHandle;
use LWP::Simple;
#most of the above is only put in so I can compile to stand alone exe
#If you use as script keep the last two and use Tk;

# Below is the init section
# A few thing to do is check OS to see if its Windows or not
($ar) = @ARGV; #Let the program do its thing with the arguments
# Bah check OS
# Just to make sure test $0, this is a work around for a minor bug
# Detect : a trade mark of a DOS system
if($^O ne "Win32") {
if($0 =~/\//g){
@hd = split "/", $0;
$hdl = pop(@hd); # Knock the filename off the array we don't need it
$basedir = join('/', @hd);
}else{
$basedir = ".";
}
}else{
$basedir = ".";
}

$main = MainWindow->new(-title=> "kPad"); #Generates the main window

$menubar = $main->Frame()->pack(-side => "top", -fill => "x"); #Notice I create the menu bar as
# a frame not a Tk::Menu menubar, this makes things easier

#Below I define all the DialogBoxes,note they can be globaly used

$about = $main->DialogBox(-title=>"About...",-buttons=>["OK"]); #Creates the about Dialog
$aabout = $about->add("Label",-text=>"kPad - Perl to the max!\n by Paul Malcher\nVersion 4.3.2\n")->pack; #Adds a label to $about
$kweabt = $main->DialogBox(-title=>"About kWebedit...",-buttons=>["OK"]); #Creates the About kWebedit Dialog
$akweabt =$kweabt->add("Label",-text=>"kWebedit v.1.0.3\nby Chris Litwin\nDesigned exclusively for use in kPad.")->pack; #That's the about for kWebedit.
$help = $main->DialogBox(-title=>"Help Topics",-buttons=>["OK"]); #Creates Help Dialog
$ahelp = $help->add("Label",-text=>"Help topics for KPAD\nWell, this is a text/file editor mainly meant for scripting and programming use.
Like notepad but made for the programmer.")->pack;
$nsave = $main->DialogBox(-title=>"Warning File Has changed!",-buttons=>["Save","Exit"]);
$ansave = $nsave->add("Label",-text=>"The documents contents have changed since you opened.\nDo you wish to save?.")->pack;
$nimp = $main->DialogBox(-title=>"Non-implementation Error",-buttons=>["OK"]);
$animp = $nimp->add("Label",-text=>"This function is not yet implemented!")->pack;
$fdisc = $main->DialogBox(-title=>"Disclaimer...",-buttons=>["OK"]);
$afdisc = $fdisc->add("Label",-text=>"Please note that some websites have their contents protected by copyright law.\nUse source that doesn't belong to you responsibly. :)")->pack;

$fetch = $main->DialogBox(-title =>'HTML Source Fetch',-buttons=>["OK"]);
$afetch = $fetch->add("Label",-text=>'Fetch what:')->pack;
$bfetch = $fetch->add("Entry")->pack;

$dummy = $main->DialogBox(-title=>'Dummy Box');
$adummy = $dummy->add("Text")->pack;

# Begin new Kpad 4.0 features
# Plugin/Macros or whatever you want to call them
# First we find and autoload plugin, yes we use grep, makes life good
opendir(DIR, $basedir) or warn ("Cannot open current directory! Autoload Aborted!");
my @contents = readdir(DIR);
closedir(DIR);
# Links may be ignored completely:
# No hidden files and ".." directories:
@contents = grep {!/^\./} @contents;
# Get files:
my @files = grep {-f} @contents;
# no dirs or hidden files
my @plugins = grep {/\.kpd/} @contents;
my @plugins = grep {!/[\~]/} @plugins; # This line is just for kedit backup files
# Print wow that was easy and it worked, any file with a .kpd extension is assummed to be a plugin
# Now I got to load them into an array and then added each to a list box
$pls = 0;
# Heck with lets do it all in one loop
foreach(@plugins) {
open pin,"<$basedir/@plugins[$pls]";
@gn = split "::" , <pin>;
if(@gn[2] eq "auto"){
@n[$pls] = "auto";
}else{
@n[$pls] = @gn[1];
}
$pls++;
}
# determin the number of plugins, so we can size the list accordingly
$nop = scalar(@n); #notice @n does not get shortend, this is important later on
foreach(@n) {
if($_ eq "auto"){
$nop--; # make sure auto plugins are not listed
}
}

# Build the menu with list box
$plugin = $main->DialogBox(-title=>'Macro Execution Menu',-buttons=>["Close"]);
$bplugin = $plugin->add("Label",-text=>'Double Click To Execute Macro')->pack;
$aplugin = $plugin->Listbox("-width"=>40, "-height"=> $nop)->pack;
foreach(@n) {
if($_ eq "auto"){
$arun = 0;
}else{
$aplugin->insert('end', "$_");
}
}
$aplugin->bind('<Double-1>' , \&eplugin); # Plugin name now can be different from the file name

$filemenu = $menubar->Menubutton(-text => 'File', -underline => 0,-tearoff => 0)->pack(-side=>'left'); #This puts
#the file button on the frame used for the menu bar

#Below are the commands for that button
#note How I included the subs into the command function

$filemenu->command(-label => 'New',-command => sub{
$text->delete('1.0','end');
});



$filemenu->command(-label => 'Open',-command => sub{
$text->delete('1.0','end');
my $types = [['All Files',        '*.*',             ]];
$open = $main->getOpenFile(-filetypes=>$types);
open FILE, "<$open"; #took weeks to get this right,its there so te whole file loads correctly
while (! eof FILE){
$text->insert('end',FILE -> getline);
}
close FILE;
$text ->pack;
$track = $text->get('1.0','end');
});

$filemenu->command(-label => 'Save',-command => sub{
$data = $text->get('1.0','end'); #Saving for widget to file is a piece of cake
if($ar eq ""){
open FILE , ">$open";
print FILE "$data";
close FILE;
}else{
open FILE , ">$ar";
print FILE "$data";
close FILE;
}
});

$filemenu->command(-label => 'Save As',-command => sub{
my $types = [['All Files',        '*.*',             ]];
my $save = $main->getSaveFile(-filetypes=>$types);
$data = $text->get('1.0','end'); #Saving for widget to file is a piece of cake
open FILE , ">$save";
print FILE "$data";
close FILE;
$open = $save; 
});

$filemenu->separator;

$filemenu->command(-label => 'Exit',-command => sub{
exit(0);
});

$editmenu = $menubar->Menubutton(-text => 'Edit', -underline => 0,-tearoff => 0)->pack(-side=>'left');

$editmenu->command(-label => 'Cut',-command => sub{
my ($w) = @_;
$text->Column_Copy_or_Cut(1);
});

$editmenu->command(-label => 'Copy',-command => sub{
my ($w) = @_;
$text->Column_Copy_or_Cut(0);
});

$editmenu->command(-label => 'Paste',-command => sub{
$text->clipboardColumnPaste();
});

$editmenu->separator;

$editmenu->command(-label => 'Select All',-command => sub{
$text->selectAll();
});

$editmenu->command(-label => 'Unselect All',-command => sub{
$text->unselectAll();
});

#$viewmenu = $menubar->Menubutton(-text => 'View', -underline => 0,-tearoff => 0)->pack(-side=>'left');

#$viewmenu->command(-label => 'Word Wrap',-command => sub{
#});

$searchmenu = $menubar->Menubutton(-text => 'Search', -underline => 0,-tearoff => 0)->pack(-side=>'left');

$searchmenu->command(-label => 'Find',-command => sub{
$text->findandreplacepopup(1);
});

$searchmenu->command(-label => 'Find And Replace',-command => sub{
$text->findandreplacepopup(0);
});

#$searchmenu->command(-label => 'Find File',-command => sub{
#find(\&wanted, "/","/" );
#});

$toolsmenu = $menubar->Menubutton(-text => 'Tools', -underline => 0,-tearoff => 0)->pack(-side=>'left');

$toolsmenu->command(-label => 'Goto Line',-command => sub{
$text->GotoLineNumberPopUp();
});

$toolsmenu->command(-label => 'Which Line?',-command => sub{
$text->WhatLineNumberPopUp();
});

$htmlmenu = $menubar->Menubutton(-text => 'HTML', -underline => 0,-tearoff => 0)->pack(-side=>'left');

$htmlmenu->command(-label => 'Basic HTML',-command => sub{
$text->delete('1.0','end');
$text->insert('end', "<html> \n");
$text->insert('end', "<head> \n");
$text->insert('end', "<title>Your Title Here</title> \n");
$text->insert('end', "</head> \n");
$text->insert('end', "<body> \n");
$text->insert('end', "Your Content Here! \n");
$text->insert('end', "</body> \n");
$text->insert('end', "</html> \n");
});

$htmlmenu->command(-label => 'Basic CSS2 (IE 5.5+ only)',-command => sub{
$text->delete('1.0','end');
$text->insert('end', "<style type=text/css> \n");
$text->insert('end', "<!-- \n");
$text->insert('end', "body{ \n");
$text->insert('end', "font-family: [Font(s), multiple speparated by commas] ; \n");
$text->insert('end', "font-size: [size, add pt for points or px for pixels] ; \n");
$text->insert('end', "background: [background, add # to the front for HEX]; \n");
$text->insert('end', "color: [Same as above]; \n");
$text->insert('end', "scrollbar-face-color: [Same as above]; \n");
$text->insert('end', "scrollbar-shadow-color: [Same as above]; \n");
$text->insert('end', "scrollbar-highlight-color: [Same as above]; \n");
$text->insert('end', "scrollbar-3dlight-color: [Same as above]; \n");
$text->insert('end', "scrollbar-darkshadow-color: [Same as above]; \n");
$text->insert('end', "scrollbar-track-color: [Same as above]; \n");
$text->insert('end', "scrollbar-arrow-color: #466587; \n");
$text->insert('end', "} \n");
$text->insert('end', "a{ \n");
$text->insert('end', "color: [Color, add # for hex]; \n");
$text->insert('end', "text-decoration:[This can be none, underline, or overline]; \n");
$text->insert('end', "} \n");
$text->insert('end', "a:hover{ \n");
$text->insert('end', "color: [Same as above]; \n");
$text->insert('end', "text-decoration: [Same as above]; \n");
$text->insert('end', "} \n");
$text->insert('end', "--> \n");
$text->insert('end', "</style> \n");
});

$htmlmenu->command(-label => 'Definition List',-command =>sub{
$text->delete('1.0','end');
$text->insert('end', "<dl> \n");
$text->insert('end', "<dt>Definition Term here..add as many of this and the next line as needed.</dt> \n");
$text->insert('end', "<dd>Defintion of Term here</dd> \n");
$text->insert('end', "</dl> \n");
});

$htmlmenu->command(-label => 'Fetch source code...',-command => sub{$fdisc->Show;
$fetch->Show;
$htm = $bfetch->get;
$contents = get($htm);
open ttt, ">temp.dat";
print ttt "$contents";
close ttt;
open FILE, "<temp.dat"; #took weeks to get this right,its there so te whole file loads correctly
$text->delete('1.0','end');
while (! eof FILE){
$text->insert('end',FILE -> getline);
}
close FILE;
$text ->pack;
$track = $text->get('1.0','end');
});

$pluginmenu = $menubar->Menubutton(-text => 'Macros', -underline => 0,-tearoff => 0)->pack(-side=>'left');

$pluginmenu->command(-label => 'Execute Macro',-command => sub{$plugin->Show;});

$aboutmenu = $menubar->Menubutton(-text => 'Help', -underline => 0,-tearoff => 0)->pack(-side=>'left');

$aboutmenu->command(-label => 'Help Topics...',-command => sub{$help->Show;});

$aboutmenu->command(-label => 'About KPAD...',-command => sub{$about->Show;});

$aboutmenu->command(-label => 'About kWebedit...',-command => sub{$kweabt->Show;});

$text = $main->Scrolled(Text,-scrollbars=>'se')->pack(-fill=>'both',-expand=>1); #Scrolled Text
#widget that adapts to the size of the window

if($ar ne ""){
open FILE, "<$ar"; #took weeks to get this right,its there so te whole file loads correctly
while (! eof FILE){
$text->insert('end',FILE -> getline);
}
close FILE;
$text ->pack;
$track = $text->get('1.0','end');
}

sub eplugin { # Plugin executor, non-auto
$v = $aplugin->get('active');
# Fix for plugin vs. filename fix
# @plugins @n
$fp = 0;
while(@n[$fp] ne $v){ # assume the names in @plugin match with @n 
# which they will unless you screw with the way plugins are handled
$fp++;
}
$v = @plugins[$fp];
# Hope it works
open pe, "<$basedir/$v"; # presto it does
# The same fucking bug in Tk again, yes the one that took weeks to work around
# I got to do this the hard way
$adummy->delete('1.0','end');
while (! eof pe){
$adummy->insert('end', pe -> getline);
}
$tdata = $adummy->get('2.0','end'); # this is the only way to load an entire plugin into a var the right way, fuck
eval ( $tdata );
if($@){ # Only way to to make so it can trap multiple errors without the app having a fatal error itself
$error = $@;
&merr($error);
}
}

sub aeplugin { # Auto plugin executor
$apc = 0;
while(@n[$apc] ne ""){
if(@n[$apc] eq "auto"){
$v = @plugins[$apc];
# Hope it works
open pe, "<$basedir/$v"; # presto it does
# The same fucking bug in Tk again, yes the one that took weeks to work around
# I got to do this the hard way
$adummy->delete('1.0','end');
while (! eof pe){
$adummy->insert('end', pe -> getline);
}
$tdata = $adummy->get('2.0','end'); # this is the only way to load an entire plugin into a var the right way, fuck
eval ( $tdata );
if($@){ # Only way to to make so it can trap multiple errors without the app having a fatal error itself
$error = $@;
&merr($error);
}
}
$apc++;
}
$arun = 1;
}

sub merr { # merr, macro/plugins error
$merr = $main->DialogBox(-title =>'Macro Error',-buttons=>["OK"]);
$amerr = $merr->add("Label", -text=>"Error: $error")->pack;
$merr->Show;
undef $merr;
}

if($arun eq "0"){
&aeplugin();
}
MainLoop; #The main processing loop











