#!/usr/bin/perl

#
# list all services on local machine,
# and attached the vbscript version
#

use Win32::OLE;
use Data::Dump qw(dump);

my $objname = q(winmgmts:\\\\.);
my $obj = Win32::OLE->GetObject($objname);

my $inst = $obj->InstancesOf("Win32_Service");
dump($inst);

foreach my $objserv (in $inst)  {
	print "name: ", $objserv->Name, "\n",
		"display name: ", $objserv->DisplayName, "\n",
		"description: ", $objserv->Description, "\n",
		"path name: ", $objserv->PathName, "\n",
		"start mode: ", $objserv->StartMode, "\n",
		"state: ", $objserv->State, "\n\n";
}

__END__

strComputer = "."

Set objSWbemServices = GetObject("winmgmts:\\" & strComputer)
Set colServices = objSWbemServices.InstancesOf("Win32_Service")

For Each objService In colServices
 Wscript.Echo "Name: " & objService.Name & vbCrLf & _
 "Display Name: " & objService.DisplayName & vbCrLf & _
 "Description: " & objService.Description & vbCrLf & _
 "Path Name: " & objService.PathName & vbCrLf & _
 "Start Mode: " & objService.StartMode & vbCrLf & _
 "State: " & objService.State & vbCrLf
Next
