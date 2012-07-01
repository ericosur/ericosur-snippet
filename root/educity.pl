#!/usr/bin/perl

use v5.10;
use Win32::Clipboard;

my $file = 'rand1234.txt';
my $cmd = "openssl rand -base64 -out $file 8";
say $cmd;
system $cmd;

open my $fh, $file or die;

my $content = <$fh>;
close $fh;
unlink $file;

$content =~ s/[=\r\n\W]+//g;
$content =~ s/^\d(\w+)/$1/;
$content = lc($content);

say $content;
Win32::Clipboard()->Set($content);

