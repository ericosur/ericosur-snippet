#!/usr/bin/perl
#
# get registry data demo
# list all the tips of the day from registry
#
# 2007/10/12 by ericosur
#

# use strict;
use warnings;

use Win32::TieRegistry;

my $line = <DATA>;
$line =~ s/\n//;
printf "read registry value from:\n%s\n", $line;

$Registry->Delimiter("/");

my $envkey = $Registry->{$line};
printf "result:\n%s\n", $envkey->{"path"};


### set the registry value
### $envkey->{"path"} =

undef $envkey;

__DATA__
HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Control/Session Manager/Environment/

__END__

$Registry->Delimiter("/");
my $tips= $Registry->{"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"};

foreach ( keys %$tips )
{
	print "$_: ", $tips->{$_}, "\n";
}

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment

>> reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"

    @members = keys( %{$envkey} );
    @subKeys = grep(  m#^/#,  keys( %{$envkey->{"Environment"}} )  );
    # @subKeys= ( "/", "/EditFlags" );
    @valueNames = grep(  ! m#^/#,  keys( %{$swKey->{"Environment"}} )  );
    # @valueNames= ( "DefaultIcon/", "shell/", "shellex/" );
