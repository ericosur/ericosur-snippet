#!/usr/local/bin/wish -f
proc power {base p} {
        set result 1
        while {$p > 0} {
                set result [expr $result*$base]
                incr p -1
        }
        return $result
}
entry .base -width 6 -relief sunken -textvariable base
label .label1 -text "to the power"
entry .power -width 6 -relief sunken -textvariable power
label .label2 -text "is"
label .result -textvariable result
pack .base .label1 .power .label2 .result -side left -padx 1m -pady 2m
bind .base <Return> {set result [power $base $power]}
bind .power <Return> {set result [power $base $power]}
# End of File
