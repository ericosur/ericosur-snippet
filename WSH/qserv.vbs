' from msdn examples

' Script for finding a class in WMI Repository
Set args = wscript.arguments
If args.Count <= 0 Then
    Wscript.Echo "Tool to search for a matching class in the WMI Repository. "
    Wscript.Echo "USAGE: <keywordToSearch> [<namespaceToSearchIn>]"
    Wscript.Echo "Example1: Cscript search.vbs service"
    Wscript.Echo "Example2: Cscript search.vbs video root\cimv2"
Else
    ' If no Namespace is specified then the Default is the ROOT namespace
    rootNamespace = "\\.\ROOT"
    keyword = args(0)
    If args.Count > 1 Then
        rootNamespace = args(1)
    End If
    EnumNameSpace rootNamespace
    Wscript.Echo vbNewLine
End if

' Subroutine to recurse through the namespaces

Sub EnumNameSpace(parentNamespaceName)

Set objService = GetObject("winmgmts:" & parentNamespaceName)

Set collMatchingClasses = objService.Execquery _
    ("Select * From meta_class Where __class " & _
    "Like '%" & keyword & "%'")
If (collMatchingClasses.count > 0) Then
    Wscript.Echo vbNewLine
    Wscript.Echo vbNewLine
    Wscript.Echo "Matching Classes Under Namespace: " & parentNamespaceName

    For Each matchingClass in collMatchingClasses
        Wscript.Echo "    " & matchingClass.Path_.CLASS
    Next
End if

Set collSubNamespaces = objService.Execquery _
    ("select * from __namespace")
For Each subNameSpace in collSubNamespaces
    EnumNameSpace subNameSpace.path_.namespace + _
        "\" + subNameSpace.Name
Next

End Sub
