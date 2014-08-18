' get the physical memory size from wmi

strComputer = "."

Set objSWbemServices = GetObject("winmgmts:\\" & strComputer)
Set colSWbemObjectSet = _
	objSWbemServices.InstancesOf("Win32_LogicalMemoryConfiguration")

For Each objSWbemObject In colSWbemObjectSet
	Wscript.Echo "Total Physical Memory (kb): " & _
	objSWbemObject.TotalPhysicalMemory
Next
