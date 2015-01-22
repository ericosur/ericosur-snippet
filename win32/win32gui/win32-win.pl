#!/usr/bin/perl
# 送給有使用 Perl 開發 Win32 視窗程式的同好們 :)

use strict;
use warnings;

use Win32::GUI;
use Win32::API;

use constant WS_EX_LAYERED    => 0x00080000;
use constant LWA_COLORKEY     => 0x00000001;
use constant LWA_ALPHA        => 0x00000002;
use constant GWL_EXSTYLE      => -20;

my $alpha = 230;       # 視窗透明度, 0~255

my $SetLayeredWindowAttributes = Win32::API->new(
    "user32","SetLayeredWindowAttributes", "LLIN", "I"
)
or die "Failed to load SetLayeredWindowAttributes: $!";

my $text = defined($ARGV[0]) ? $ARGV[0] : "Hello, world";

my $main = Win32::GUI::Window->new(
    -name   => 'Main',
    -width  => 100,
    -height => 100,
    -text   => 'Perl',
);


my $font = Win32::GUI::Font->new(
        -name => "Comic Sans MS",
        -size => 24,
);

my $label = $main->AddLabel(
    -text       => $text,
    -font       => $font,
    -foreground => 0x0000FF
);


$main->Resize(
    $label->Width()  + $main->Width()  - $main->ScaleWidth(),
    $label->Height() + $main->Height() - $main->ScaleHeight()
);


$main->SetWindowLong(
    GWL_EXSTYLE,
    $main->GetWindowLong(GWL_EXSTYLE)|WS_EX_LAYERED||WS_EX_LAYERED
);

$SetLayeredWindowAttributes->Call(
    $main->{-handle}, 0, $alpha, LWA_ALPHA
);

$main->Show();
Win32::GUI::Dialog();
exit(0);

sub Main_Terminate {
    return -1;
}
