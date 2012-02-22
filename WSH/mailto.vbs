'--------------------------------------------------------------------
'
' Mailout using CDONTS.NewMail
'
'--------------------------------------------------------------------

' Declare all variables.
Option Explicit
Dim objSendMail
Dim strTo, strFrom
Dim strSubject, strBody

' Mail constants (some are for reference).
Const CdoBodyFormatHTML = 0 ' Body property is HTML
Const CdoBodyFormatText = 1 ' Body property is plain text (default)
Const CdoMailFormatMime = 0 ' NewMail object is in MIME format
Const CdoMailFormatText = 1 ' NewMail object is plain text (default)
Const CdoLow    = 0         ' Low importance
Const CdoNormal = 1         ' Normal importance (default)
Const CdoHigh   = 2         ' High importance

strFrom    = "someone@microsoft.com"  ' Change to your e-mail address.
strTo      = "someone@microsoft.com"  ' Change to the recipient address.
strSubject = "Test Message"          ' Change to your subject.

' This line calls the ReadFile() function to read the page contents.
strBody = ReadFile("C:\MAILOUT.TXT")

' This line calls the MakePage() function to format the page as HTML.
strBody = MakePage(strSubject,strBody)

' The following section creates the mail object and sends the mail.
Set objSendMail = CreateObject("CDONTS.NewMail")
	objSendMail.From    = strFrom
	objSendMail.To      = strTo
	objSendMail.Subject = strSubject & " (" & Date() & ")"
	objSendMail.Body    = strBody

	objSendMail.BodyFormat = CdoBodyFormatHTML
	objSendMail.MailFormat = CdoMailFormatMime
	objSendMail.Importance = CdoNormal

	objSendMail.Send
Set objSendMail = Nothing

' This function returns a properly formatted HTML page.
Function MakePage(txtSubject, txtBody)
	Dim txtTemp
	txtTemp = "<HTML>" & vbCrLf
	txtTemp = txtTemp & "<HEAD><TITLE>"
	txtTemp = txtTemp & txtSubject
	txtTemp = txtTemp & "</TITLE></HEAD>" & vbCrLf
	txtTemp = txtTemp & "<BODY>" & vbCrLf
	txtTemp = txtTemp & "<H2>" & txtSubject & "</H2>" & vbCrLf
	txtTemp = txtTemp & txtBody & vbCrLf
	txtTemp = txtTemp & "</BODY>" & vbCrLf
	txtTemp = txtTemp & "</HTML>"
	MakePage = txtTemp
End Function

' This function opens a file and returns the contents of the file.
Function ReadFile(txtFile)
	Dim txtTemp, objFS, objFL
	Set objFS = CreateObject("Scripting.FileSystemObject")
	Set objFL = objFS.OpenTextFile(txtFile)
	Do While Not objFL.AtEndOfStream
		txtTemp = txtTemp & objFL.ReadLine
		txtTemp = txtTemp & vbCrLf
	Loop
	objFL.Close
	Set objFS = Nothing
	ReadFile = txtTemp
End Function
