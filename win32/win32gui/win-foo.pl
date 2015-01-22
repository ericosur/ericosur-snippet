#!/usr/bin/perl
# it can only be run under win32

#
# my win32 hello world demo script
#
#

use strict;
use warnings;

use Win32::GUI();

my $main;

sub show($);

sub Main_Terminate
{
	return -1;
}

# Resize Window
sub Hello_OnSize {
  my ($self) = @_;
  my ($width, $height) = ($self->GetClientRect())[2..3];
  $self->Edit->Resize($width+1, $height-40) if exists $self->{Edit};
}

sub OnOkButtonClick
{
	my $file = "win-foo.pl";

	return if ! -f $file;
	open my $fh, $file or return;

	while (<$fh>)  {
		s/\n//;
		$main->Edit->Append($_);
		$main->Edit->Append("\r\n");
	}
	$main->Edit->SetFocus();
	close $fh;
}

sub OnTestButtonClick
{
	$main->Edit->Text("");
	my $result = `exiftool`;
	$result = join "\r\n", split /\n/,$result;
	show($result);
#	$main->Edit->Append($result);
#	$main->Edit->SetFocus();
}

sub OnCallButtonClick
{
#	$main->Edit->Text("");
	my $result = `sp.pl`;
	$result = join "\r\n", split /\n/,$result;
	$result = $result . "\r\n";
	show($result);
#	$main->Edit->Append($result);
#	$main->Edit->SetFocus();
}

sub OnGetButtonClick
{
	my $line_idx;
	my $d = shift;
	$line_idx = $main->Edit->GetLineCount();
	$main->edtLine->Text($line_idx);
}

sub show($)
{
	my $text = shift;
	$main->Edit->Append($text);
	$main->Edit->SetFocus();
}

sub clear
{
	$main->Edit->Text("");
}

sub main()
{
	my $button_top = 8;
	my $button_w = 60;
	my $button_h = 24;

	$main = Win32::GUI::Window->new(
		-name   => 'Hello',
		-size => [800, 600],
		-pos => [100, 100],
		-text   => 'My multiline',
		-onResize   => \&Hello_OnSize,
	);

	my $EditFont = new Win32::GUI::Font (
		-name => "Dina",
		-size => 10,
	    );

	# Create Textfield for Edit Text
	$main->AddTextfield(
	    -name      => "Edit",
	    -pos       => [0, 40],
	    -size      => [20, 20],
	    -multiline => 1,
	    -hscroll   => 1,
	    -vscroll   => 1,
	    -autohscroll => 1,
	    -autovscroll => 1,
	    -keepselection => 1 ,
	    -font => $EditFont
	);

	$main->AddTextfield(
		-name => 'edtLine',
		-pos => [520, $button_top],
		-size => [48, $button_h],
		-readonly => 1,
		-align => 'center',
	);

	$main->AddButton(
		-name => 'OkButton',
		-pos => [10, $button_top],
		-size => [$button_w, $button_h],
		-onClick => \&OnOkButtonClick,
		-caption => 'Load',
	);

	$main->AddButton(
		-name => "TestButton",
		-pos => [80, $button_top],
		-size => [$button_w, $button_h],
		-onClick => \&OnTestButtonClick,
		-caption => 'Exiftool',
	);

	$main->AddButton(
		-name => "CallButton",
		-pos => [150, $button_top],
		-size => [$button_w, $button_h],
		-onClick => \&OnCallButtonClick,
		-caption => 'Call sp',
	);

	$main->AddButton(
		-name => 'GetButton',
		-pos => [220, $button_top],
		-size => [$button_w, $button_h],
		-onClick => \&OnGetButtonClick,
		-caption => 'Get Line',
	);

	$main->AddButton(
		-name => 'ClearButton',
		-pos => [290, $button_top],
		-size => [$button_w, $button_h],
		-onClick => \&clear,
		-caption => 'Clear',
	);

	$main->Edit->SetFocus();
	$main->Edit->Text("");
	$main->Edit->LimitText(60000);
	$main->Show();
	Win32::GUI::Dialog();

	exit(0);
}

main;
