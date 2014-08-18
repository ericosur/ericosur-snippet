#!/usr/bin/perl

# Almost the same as ``MyBack'' program at
# C:\Projects\¤pµ{¦¡\myBack\myBack.exe
# -- Jul 22 1998 by Eric
# init version
# -- Aug 6 1998 by Eric
# Because there are some ZIP/ARJ files in \\projects, it wastes
# lots of time to compress compressed files. I compress these file
# twice: first time add uncompressed file with compression factor,
# second time just storing those ZIP/ARJ archives.
# -- Aug 21 1998 by Eric
# add: seperate compress ZIP/ARJ files and plain files...

use strict;

my $rarpath = "c:\\progra~1\\winrar\\";
my $rarbin = "winrar.exe";
my $action = "a -y -tl -rr -ri12 -r -mdE -m4 -s";
my $arc_path = "c:\\temp\\";

sub my_time_postfix {
    my ($ss,$mm,$hh,$dd,$MM,$yy,$wd,$yd,$isdst) = localtime(time);
    return sprintf("%04d-%02d-%02d_%02d-%02d", $yy+1900, $MM+1, $dd, $hh, $mm);
}

sub ExecRAR($$) {
    my $prefix = shift @_;
    my $target = shift @_;
#    $target = '"' . $target . '"';

    my $arc_file = $arc_path . $prefix . &my_time_postfix . ".rar";
    print $arc_file, "\n";

    my $excl_args = '-x*.zip -x*.arj -x*.rar';
    my $cmd = "$rarpath$rarbin $action $excl_args $arc_file $target";
    print "First exec [$cmd]\n";
    system $cmd;

    # -m0 will override previous -m4 switch
    $cmd = "$rarpath$rarbin $action -m0 -inul $arc_file $target*.arj $target*.zip $target*.rar";
    print "Second exec [$cmd]\n";
    system $cmd;
}

# a modified version...
# only for files in c:\projects...
sub ExecRAR_prj($$) {
    my $prefix = shift @_;
    my $target = shift @_;

    my $arc_file = $arc_path . $prefix . &my_time_postfix . '.rar';
    print $arc_file, "\n";

    my $excl_args = '-x*.zip -x*.arj -x*.tds -x*.il? -x*.~*';
    my $cmd = "$rarpath$rarbin $action -ds $excl_args $arc_file $target";
    print "First exec [$cmd]\n";
    system $cmd;

    # -m0 will override previous -m4 switch
    $cmd = "$rarpath$rarbin $action -m0 -ds $arc_file $target*.arj $target*.zip";
    print "Second exec [$cmd]\n";
    system $cmd;
}

unless ( -e $rarpath . $rarbin ) {  # if not exist
    die "cannot locate WinRAR program\n";
}

#testing...
#ExecRAR("ErPerl", "c:\\Perl\\Eric\\");

# issue commands...

ExecRAR("Doc", "c:\\MyDocu~1\\");
ExecRAR("Becky", "c:\\Mail\\");
ExecRAR("Usr", "c:\\Progra~1\\Netscape\\Users\\Ericosur\\");
ExecRAR_prj("Prj", "c:\\Projects\\");
