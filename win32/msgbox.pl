#!/usr/bin/perl
#
# demo perl script call win32 api to GetTickCount() and MessageBox()
#
# 2007/04/30 by ericosur
# 2008/03/16 add some more info string from win32

use Win32;

my $ticks = Win32::GetTickCount();

my $name = Win32::LoginName;
my $node = Win32::NodeName;
my $buildnum = Win32::BuildNumber;

my $str =<<EOL;
name: $name
node: $node
build: $buildnum
ticks: $ticks
EOL

Win32::MsgBox($str, MB_OK | MB_ICONINFORMATION , "win32 info");
