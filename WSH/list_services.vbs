' list all services on local machine

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
