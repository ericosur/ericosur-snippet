; keepawake.ahk
;
; send R-Shift key stroke every 60 seconds
;
; for Autohotkey v1

;
; # win
; ! alt
; ^ ctrl
; + shift
;

#SingleInstance
#Persistent

wtf_path := "c:\Users\rasmus_lai\Desktop\wtf.ahk"
autohotkeyexe_path := "d:\Tool\AutoHotkey\AutoHotkeyU64.exe"

; icon is a locker, but never have a chance to see it
Menu, Tray, Icon, shell32.dll, 48

; ; ctrl+win+numpad ENTER reload this script
; #NumpadEnter::
;     ; Send, ^s ; To save a changed script
;     MsgBox, "Reload WTF Autohotkey script"
;     Run, %autohotkeyexe_path% %wtf_path%
;     Return


SetTimer, CheckIdle, 180000    ; 60 sec / 1 min
Return

CheckIdle:
If (A_TimeIdle > 180000)
{
    Send {RShift}
}
Return

; control mmsys.cpl sounds
