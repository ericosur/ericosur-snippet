#!/usr/bin/wish
button .b1 -text "Hello,World!" -command exit
pack .b1
button .b2 -text "Hello,TCL/TK" -command "destroy .b2"
pack .b2
