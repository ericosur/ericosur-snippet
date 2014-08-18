SendMailOutlook "rasmus.lai@benq.com", "test from vbs", "test test", "rasmus.lai@benq.com"

Sub SendMailOutlook(aTo, Subject, TextBody, aFrom)

  'Create an Outlook object
  Dim Outlook 'As New Outlook.Application
  Set Outlook = CreateObject("Outlook.Application")

  'Create e new message
  Dim Message 'As Outlook.MailItem
  Set Message = Outlook.CreateItem(olMailItem)
  With Message
    'You can display the message To debug And see state
    '.Display

    .Subject = Subject
    .Body = TextBody

    'Set destination email address
    .Recipients.Add (aTo)

    'Set sender address If specified.
    Const olOriginator = 0
    If Len(aFrom) > 0 Then .Recipients.Add(aFrom).Type = olOriginator

    'Send the message
    .Send
  End With
End Sub
