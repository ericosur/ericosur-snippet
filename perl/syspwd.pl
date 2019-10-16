#!/usr/bin/perl

#@ pwd using sys call to get current working directory
#@ not working under win32
#
# 2006/12/27 by ericosur

    require 'asm/unistd.ph';
    use strict;
use warnings;


    my $pwd = chr(0) x 256;
    syscall(&__NR_getcwd, $pwd, 256);
    print "pwd = $pwd\n";
