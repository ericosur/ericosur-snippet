#!/usr/bin/perl
#HICON ExtractIcon(
#    HINSTANCE hInst,
#    LPCTSTR lpszExeFileName,
#    UINT nIconIndex
#);
#shell32.dll

use Win32::API;
use Data::Dump qw(dump);

	my $file = 'c:/windows/system32/shell32.dll';

	print "calling ExtractIcon()...\n";
    my $ExtractIcon = Win32::API->new(
        "shell32", "ExtractIcon", 'NPN', 'N'
    );
    exit -1 if $ExtractIcon eq 0;

    my $icon = $ExtractIcon->Call(0, $file, -1);
    printf "There are %d icons in (%s)\n", $icon, $file;
