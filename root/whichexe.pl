#!/usr/bin/perl
# Similar to UNIX which command.
#
# On my NT box:
#
#  D:\src\perl\win32-guitest>eg\which.pl perl
#  D:\perl\bin\perl.EXE
#  D:\src\perl\win32-guitest>eg\which.pl regedit
#  C:\WINNT\regedit.EXE
#  D:\src\perl\win32-guitest>eg\which.pl notepad
#  C:\WINNT\system32\notepad.EXE
#  D:\src\perl\win32-guitest>
#

use strict;
use if $^O eq "MSWin32", "Win32::GuiTest::Cmd qw(WhichExe)";

die "only win32" if $^O ne "MSWin32";
print WhichExe(shift);

