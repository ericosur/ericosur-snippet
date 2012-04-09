#!/bin/bash

# a helper script to call rmbom.pl to remove BOM marker
~/gcode/ericosur/root/rmbom.pl $1 > $1.bak
cp $1.bak $1
rm $1.bak

