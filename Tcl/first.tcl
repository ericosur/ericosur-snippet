#!/usr/local/bin/wish8.3
tk useinputmethods 1
font create bsmilpfont -family "ar pl mingti2l big5" -size 16
label .a -text "¼ÐÅÒ" -font bsmilpfont
pack .a
button .b -text "«ö¶s" -command { puts stdout $cc; exit } -font bsmilpfont
pack .b
entry .c -textvariable cc -font bsmilpfont
pack .c
