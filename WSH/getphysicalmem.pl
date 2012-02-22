#!/usr/bin/perl

# use Win32::OLE to call wmi to get physical memory size
# after the END section, there is the vbscript version

use Win32::OLE;
use Data::Dump qw(dump);

my $objname = q(winmgmts:\\\\.);
my $obj = Win32::OLE->GetObject($objname);
#dump($obj);

my $inst = $obj->InstancesOf("Win32_LogicalMemoryConfiguration");
#dump($inst);

foreach my $oo (in $inst)  {
	print "total physical memory (KB): " . $oo->TotalPhysicalMemory();
}

__END__

' the VBScript version example

strComputer = "."

Set objSWbemServices = GetObject("winmgmts:\\" & strComputer)
Set colSWbemObjectSet = _
 objSWbemServices.InstancesOf("Win32_LogicalMemoryConfiguration")

For Each objSWbemObject In colSWbemObjectSet
 Wscript.Echo "Total Physical Memory (kb): " & _
 objSWbemObject.TotalPhysicalMemory
Next
