#!/usr/bin/perl

#
# from ptt, only for win32
#
use Win32::Process qw(STILL_ACTIVE);
use Win32;

my $ProcessObj;
my $url = "http://tw.yahoo.com/";
my $timeout = 30000;

Win32::Process::Create($ProcessObj,
                      "C:\\Progra~1\\Intern~1\\iexplore.exe",
                      "iexplore $url",
                      0,
                      NORMAL_PRIORITY_CLASS,
                      ".")|| die ErrorReport();

$ProcessObj->Wait($timeout);
$ProcessObj->GetExitCode( $exitcode );
print "Process completed with exit code $exitcode\n";
$ProcessObj->Kill($exitcode);   # kill it after timeout value
