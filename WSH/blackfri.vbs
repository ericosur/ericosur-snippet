; black friday
; from http://diary.tw/tim/726

counts = 0

For i = 1 to 2000
  For j = 1 to 12
    If WeekDay(DateSerial(i, j, 13), vbSunday) = 6 Then
      counts = counts + 1
    End If
  Next
Next

WScript.Echo counts
