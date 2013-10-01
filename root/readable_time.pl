#!/usr/bin/perl

use strict;

# adb shell getprop ro.runtime.firstboot in milli second
my $android_unixtime = 1368525096398;
my $readtime = localtime($android_unixtime/1000);

printf("unix: %s\nlocal: %s\n", $android_unixtime, $readtime);
