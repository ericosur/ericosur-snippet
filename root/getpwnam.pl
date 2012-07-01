#!/usr/bin/perl

use v5.10;

# http://www.builderau.com.au/program/perl/soa/Obtain-user-group-and-process-information-in-Perl/0,339028313,339222142,00.htm

# get user info
my $logname = $ENV{'LOGNAME'};
($name, $pass, $uid, $gid, $quota, $comment, $gcos, $dir, $shell, $expire) = getpwnam($logname);
print "Name: $name \nUID: $uid \nShell: $shell\n";
print "gid: $gid\nquota: $quota\ngcos: $gcos\n";
print "dir: $dir\nshell: $shell\nexpire: $expire\n";

say '-' x 40;

# get user info
($name, $pass, $uid, $gid, $quota, $comment, $gcos, $dir, $shell, $expire) = getpwuid(1000);
print "Name: $name \nUID: $uid \nShell: $shell\n";

say '-' x 40;

# get user info
while (($name, $pass, $uid, $gid, $quota, $comment, $gcos, $dir, $shell, $expire) = getpwent()) {
print "$name \t $uid \t $dir\n";
}

say '-' x 40;

# get group info
($name, $passwd, $gid, $members) = getgrnam('adm');
print "$name \t $gid \t $members\n";

say '-' x 40;

# get group info
($name, $passwd, $gid, $members) = getgrgid(1);
print "$name \t $gid \t $members\n";

say '-' x 40;

# get group info
while (($name, $passwd, $gid, $members) = getgrent()) {
print "$name \t $gid \t $members\n";
}

say '-' x 40;

# get logged-in user name
say "Current user is " . getlogin();

say '-' x 40;

# get current process ID
say "Current PID is " . getpgrp(0);

say '-' x 40;


# get parent process ID
say "Current process' parent PID is " . getppid();

say '-' x 40;


