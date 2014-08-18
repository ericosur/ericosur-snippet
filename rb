#!/bin/bash

# a helper script to call rmbom.pl to remove BOM marker
$HOME/gcode/snippet/root/rmbom.pl $1 > $1.bak
cp $1.bak $1
rm $1.bak

# another way to remove BOM byte using VI
# load file
# :set nobomb
# :wq

