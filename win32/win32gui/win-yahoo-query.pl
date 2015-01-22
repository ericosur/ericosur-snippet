#!/usr/bin/perl

#
# my win32 hello world demo script
#
#

use strict;
use warnings;

use Win32::GUI();

use WWW::Mechanize;
use Encode;
use Encode::Guess;

sub show($);

my $mw;
my $edtQuery;

sub main
{
	my $button_top = 8;
	my $button_w = 60;
	my $button_h = 24;

	$mw = Win32::GUI::Window->new(
		-name   => 'Hello',
		-size => [320, 280],
		-pos => [100, 100],
		-text   => 'My multiline',
		-onResize   => \&OnResize,
	);

	my $EditFont = new Win32::GUI::Font (
		-name => "Dina",
		-size => 9,
	);

	# Create Textfield for Edit Text
	$mw->AddTextfield(
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

	$edtQuery = $mw->AddTextfield(
		-name => 'edtQuery',
		-pos => [10, $button_top],
		-size => [100, $button_h],
		#-readonly => 1,
		#-align => 'center',
	);

	$mw->AddButton(
		-name => 'QueryButton',
		-pos => [120, $button_top],
		-size => [$button_w, $button_h],
		-onClick => \&OnQueryButtonClick,
		-caption => 'Query',
	);

	$mw->Edit->SetFocus();
	$mw->Edit->Text("");
	#$mw->Edit->LimitText(60000);
	#$edtQuery->Show();
	$mw->Show();
	Win32::GUI::Dialog();

	exit(0);
}

sub Main_Terminate
{
	return -1;
}

# Resize Window
sub OnResize
{
  my ($self) = @_;
  my ($width, $height) = ($self->GetClientRect())[2..3];
  $self->Edit->Resize($width+1, $height-40) if exists $self->{Edit};
}

sub OnQueryButtonClick
{
	my $str = $edtQuery->Text();
	my $result = yahoo_dict_query( $str );
	show($result);
	$mw->Edit->SetFocus();
}

sub show($)
{
	my $text = shift;

	$text = join("\r\n", split("\n", $text)) . "\r\n";
	$mw->Edit->Append($text);
	$mw->Edit->SetFocus();
}

sub clear
{
	$mw->Edit->Text("");
}

sub yahoo_dict_query()
{
	my $str = shift;
	my $http = "http://tw.dictionary.yahoo.com/search?ei=UTF-8&p=$str";
	my $mech = WWW::Mechanize->new();
	$mech->get($http);

	# guess the encoding
	my $enc = guess_encoding($mech->content(), qw/big5-eten utf8/);
	my $html = encode ("big5-eten", decode($enc->name, $mech->content()));

#
# get rip off the following RE from result
#
	# kill the java script section
	$html =~ s/<script.+?<\/script>//sgx;
	# kill the html tags
	$html =~ s/<[^>]*>//g;
	# kill the blank line more than 2
	$html =~ s/\n{2,}/\n/sg;
	# eat the space more than 2
	$html =~ s/\s{2,}(\n|\S)/$1/sg;
	# eat the extra unnecessary paragraphy
	$html =~ s/&raquo.*//s;
	$html =~ s/.*段落翻譯//s;
	$html =~ s/您是不是還想知道.*//s;
	$html =~ s/相似字詞.*//s;

	return $html;
}

main;
