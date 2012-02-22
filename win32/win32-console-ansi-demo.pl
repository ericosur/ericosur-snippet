#!/usr/bin/env perl

# only for win32
use Win32::Console::ANSI;

print "\e[1;34mThis text is bold blue.\e[0m\n";
print "This text is normal.\n";
print "\e[33;45;1mBold yellow on magenta.\e[0m\n";
print "This text is normal.\n";
