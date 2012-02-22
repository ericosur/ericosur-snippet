#!/usr/bin/perl

#------------------------------------------
# hasher.pl
#
# Author:  H. Carvey
# copyright 2001 H. Carvey
# keydet89@yahoo.com
#------------------------------------------

#------------------------------------------
# Load necessary Perl Modules
#------------------------------------------
use Tk;
use Tk::Button;
use Tk::Menu;
use Tk::Menubutton;
use Tk::Checkbutton;
use Tk::DialogBox;
use Tk::Dialog;
use Tk::Label;
use Tk::Entry;
use Tk::LabFrame;
use Digest::MD5;
use Digest::SHA1;

#------------------------------------------
# Application Preferences
#------------------------------------------
my($Name) = "Win32 File Hasher";
my($Ver) = "1.1";

# Change Log: v1.1 MAC times added

#------------------------------------------
# Main Window
#------------------------------------------
my $mw = MainWindow->new();
$mw->title("$Name v $Ver");
$mw->setPalette("grey");

#------------------------------------------
# Menu Bar
#------------------------------------------
$menuFrame = $mw->Frame(-background => "grey",
			 -borderwidth => 1,
			 -relief => 'raised'
			)->pack(-fill => 'x',
				-side => 'top');

# File Menu
$fileMenu = $menuFrame->Menubutton(-text => "File",
                                   -borderwidth => 1)->pack(-side => 'left', -padx => 2);

# Open button
$fileMenu->command(-label => "Open",
                   -accelerator => "Alt+F",
                   -underline => 0,
                   -command => sub {my $fn = $mw->getOpenFile(-initialdir => Win32::GetCwd);
                                   $fn =~ s!/!\\!g;
                                   $nameEntry->delete(0,end);
                                   $nameEntry->insert(0,$fn);});

# Save button
$fileMenu->command(-label => "Save",
                   -accelerator => "Alt+S",
                   -underline => 0,
                   -command => sub {\save();});

# Separator
$fileMenu->separator();

# Exit button
$fileMenu->command(-label => "Exit",
                   -accelerator => "Alt+X",
                   -underline => 1,
                   -command => sub {exit});

# Help Menu
$helpMenu = $menuFrame->Menubutton(-text => "Help", -tearoff => 0,
                                -borderwidth => 1,
         -menuitems => [['command' => "About",
         -command => sub {my $dialog = $mw->Dialog(
         							-text => "$Name v $Ver\n\nCopyright 2001 H. Carvey\nkeydet89\@yahoo.com",
         							-title => "About",
         							-takefocus => 1,
         							-default_button => "OK",
         							-buttons => [qw/OK/]);
         							$dialog->Show();}]
         ])->pack(-side => 'right');


#------------------------------------------
# File entry
#------------------------------------------
$entryLabFrame = $mw->LabFrame(-label => "File Name",
											-labelside => "acrosstop")->pack(-expand => 'y',
				     																-side => 'top',
				     																-fill => 'x');

$nameEntry = $entryLabFrame->Entry(-state => 'normal',
                                   -background => 'white',
                                   -relief => 'sunken',
                                   -width => 40 ) -> pack(-padx => 5, -pady => 5,
                                                          -side => 'left');

# Get Button
$getButton = $entryLabFrame->Button(-command => sub {my $fn = $mw->getOpenFile(-initialdir => Win32::GetCwd);
                                                     $fn =~ s!/!\\!g;
                                                     $nameEntry->delete(0,end);
                                                     $nameEntry->insert(0,$fn);},
				 -activebackground => "grey",
				 -borderwidth => 1,
				 -relief => 'raised',
				 -text => "Open File"
				)->pack(-padx => 5, -pady => 5, -side => 'right');

#------------------------------------------
# MAC Frame
#------------------------------------------
my $macFrame = $mw->Frame(-background => "grey",
                          -borderwidth => 1,
                          -relief => 'sunken'
                          )->pack(-fill => 'x',
                          -side => 'top');

my $mLabFrame = $macFrame->LabFrame(-label => "Last Modification Time",
														-labelside =>"acrosstop")->pack(-expand => 'y',
														                           -side => 'left',
														                           -fill => 'x');
my $mEntry = $mLabFrame->Entry(-state => 'normal',
                                   -background => 'white',
                                   -relief => 'sunken',
                                   -width => 25) -> pack(-padx => 5, -pady => 5,
                                                          -side => 'left');

my $aLabFrame = $macFrame->LabFrame(-label => "Last Access Time",
														-labelside =>"acrosstop")->pack(-expand => 'y',
														                           -side => 'left',
														                           -fill => 'x');
my $aEntry = $aLabFrame->Entry(-state => 'normal',
                                   -background => 'white',
                                   -relief => 'sunken',
                                   -width => 25) -> pack(-padx => 5, -pady => 5,
                                                          -side => 'left');

my $cLabFrame = $macFrame->LabFrame(-label => "Creation Time",
														-labelside =>"acrosstop")->pack(-expand => 'y',
														                           -side => 'left',
														                           -fill => 'x');
my $cEntry = $cLabFrame->Entry(-state => 'normal',
                                   -background => 'white',
                                   -relief => 'sunken',
                                   -width => 25) -> pack(-padx => 5, -pady => 5,
                                                          -side => 'left');
#------------------------------------------
# Main Frame ;-)
#------------------------------------------
my $mainFrame = $mw->Frame(-background => "grey",
			 -borderwidth => 1,
			 -relief => 'raised'
			)->pack(-fill => 'x',
				-side => 'top');
#------------------------------------------
# MD5 Frame
#------------------------------------------
$pwdLabFrame = $mainFrame->LabFrame(-label => "MD5 Hash",
			     -labelside => "acrosstop")->pack(-expand => 'y',
				     																-side => 'left',
				     																-fill => 'x');

#------------------------------------------
#
#------------------------------------------
my $md5Frame = $pwdLabFrame->Frame(-borderwidth => 0,
				       -background => "grey",
				       -relief => 'flat')->pack( -padx => 5,
					     													 -pady => 5,
					     													 -fill => 'x');

my $md5Entry = $md5Frame->Entry(-state => 'normal',
                                   -background => 'white',
                                   -relief => 'sunken',
                                   -width => 35) -> pack(-padx => 5, -pady => 5,
                                                          -side => 'right');
#------------------------------------------
# SHA1 Frame
#------------------------------------------
$shaLabFrame = $mainFrame->LabFrame(-label => "SHA1 Hash",
			     -labelside => "acrosstop")->pack(-expand => 'y',
				     																-side => 'right',
				     																-fill => 'x');

$shaFrame1 = $shaLabFrame->Frame(-borderwidth => 0,
				       -background => "grey",
				       -relief => 'flat')->pack( -padx => 5,
					     													 -pady => 5,
																				-fill => 'x');

my $shaEntry = $shaFrame1->Entry(-state => 'normal',
                                   -background => 'white',
                                   -relief => 'sunken',
                                   -width => 45) -> pack(-padx => 5, -pady => 5,
                                                          -side => 'right');


#------------------------------------------
# bottom Button bar
#------------------------------------------
$buttonFrame = $mw->Frame(-borderwidth => 1, -background => "grey",
			          -relief => 'raised')->pack(-side => 'bottom', -fill => 'x');

my $label = $buttonFrame->Label(-text => "File Size (in bytes):  ")
												->pack(-padx => 5, -pady => 5, -side => 'left');

my $sizeEntry = $buttonFrame->Entry(-state => 'normal',
                                   -background => 'white',
                                   -relief => 'sunken',
                                   -width => 20) -> pack(-padx => 5, -pady => 5,
                                                          -side => 'left');

$closeButton = $buttonFrame->Button(-command => sub {exit},
				 -activebackground => "grey",
				 -borderwidth => 1,
				 -relief => 'raised',
				 -text => "Close"
				)->pack(-padx => 5, -pady => 5, -side => 'right');

$hashButton = $buttonFrame->Button(-command => sub {\hash()},
				 -activebackground => "grey",
				 -borderwidth => 1,
				 -relief => 'raised',
				 -text => "Hash"
				)->pack(-padx => 5, -pady => 5, -side => 'right');

#------------------------------------------
# dialogue
#------------------------------------------

sub update {$mw->update;}

#------------------------------------------
# End of MainLoop
#------------------------------------------
MainLoop;

#------------------------------------------
# hash subroutine
#------------------------------------------
sub hash {
	my $file = $nameEntry->get;
	my $md5;
	my $sha;

	my ($size,$atime,$mtime,$ctime) = (stat($file))[7..10];
	my $a_time = localtime($atime);
	my $m_time = localtime($mtime);
	my $c_time = localtime($ctime);

	$mEntry->delete(0,end);
	$mEntry->insert(0,$m_time);

	$aEntry->delete(0,end);
	$aEntry->insert(0,$a_time);

	$cEntry->delete(0,end);
	$cEntry->insert(0,$c_time);

	$sizeEntry->delete(0,end);
	$sizeEntry->insert(0,$size);

	open(FILE, $file);
  binmode(FILE);
	$md5 = Digest::MD5->new->addfile(*FILE)->hexdigest;
	close(FILE);

	open(FILE, $file);
  binmode(FILE);
	$sha = Digest::SHA1->new->addfile(*FILE)->hexdigest;
	close(FILE);

	$md5Entry->delete(0,end);
	$md5Entry->insert(0,$md5);

	$shaEntry->delete(0,end);
	$shaEntry->insert(0,$sha);
}

#------------------------------------------
# save subroutine
#------------------------------------------
sub save {
	my $sf = $mw->getSaveFile(-initialdir => Win32::GetCwd);
	my $file = $nameEntry->get();
	my $md5 = $md5Entry->get();
	my $sha = $shaEntry->get();
	my $mtime = $mEntry->get();
	my $atime = $aEntry->get();
	my $ctime = $cEntry->get();
	my $size = $sizeEntry->get();

  open(FH,">>$sf");
  print FH "$file;$size;$mtime;$atime;$ctime;$md5;$sha\n";
  close(FH);

}

