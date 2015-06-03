#!/usr/local/bin/wish -f
set id 0
entry .entry -width 30 -relief sunken -textvariable cmd
pack .entry -padx 1m -pady 1m
bind .entry <Return> {
        set id [incr id]
        if {$id > 5} {
                destroy .b[expr $id -5]

        }
        button .b$id -command "exec <@stdin >@stdout $cmd" -text $cmd
        pack .b$id -fill x
        .b$id invoke
        .entry delete 0 end
}

#end of file
