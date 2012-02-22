   '--------------------------------------------------
   '
   ' Sends email from the local SMTP service using CDONTS objects
   '
   ' Usage:
   '   sendmail -t <to> -f <from> -s "<subject>" -b "<message>"
   '   sendmail [-help|-?]
   '
   '--------------------------------------------------

   Option Explicit
   On Error Resume Next

   Dim objSendMail, oArgs, ArgNum
   Dim strTo, strFrom, strSubject, strBody

   Set oArgs = WScript.Arguments
   ArgNum = 0

   While ArgNum < oArgs.Count
      Select Case LCase(oArgs(ArgNum))
         Case "-to","-t":
            ArgNum = ArgNum + 1
            strTo = oArgs(ArgNum)
         Case "-from","-f":
            ArgNum = ArgNum + 1
            strFrom = oArgs(ArgNum)
         Case "-subject","-s":
            ArgNum = ArgNum + 1
            strSubject = oArgs(ArgNum)
         Case "-body","-b":
            ArgNum = ArgNum + 1
            strBody = oArgs(ArgNum)
         Case "-help","-?":
            Call DisplayUsage
         Case Else:
            Call DisplayUsage
      End Select
      ArgNum = ArgNum + 1
   Wend

   If oArgs.Count=0 Or strTo="" Or strFrom="" Or _
         strSubject="" Or strBody="" Then
      Call DisplayUsage
   Else
      Set objSendMail = CreateObject("CDONTS.NewMail")
         objSendMail.From = strFrom
         objSendMail.To = strTo
         objSendMail.Subject = strSubject
         objSendMail.Body = strBody
         objSendMail.Send
      Set objSendMail = Nothing
   End If

   ' Display the usage for this script
   Sub DisplayUsage
      WScript.Echo "Usage:"
      WScript.Echo "  sendmail -t <to address> -f <from address> -s " & _
         Chr(34) & "<subject>" & Chr(34) & " -b " & Chr(34) & _
         "<message body>" & Chr(34)
      WScript.Echo "  sendmail [-help|-?]"
      WScript.Echo ""
      WSCript.Quit
   End Sub
