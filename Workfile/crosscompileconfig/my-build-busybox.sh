#!/bin/bash

export PATH=~/arm2011/bin:$PATH

#arm-none-linux-gnueabi-
# Shells
#   POSIX math support
# Editor -> awk
# Misc -> dc

#In current busybox config, two config options enabled
#that depends on libm (math functions): these are math
#support for awk and dc. For dc it's just pow and exp
#functions, for awk it's a whole lot of functions -
#usual sin cos tan atan log sqrt pow exp, maybe some
#others.

make clean
time make -j8 $* 2> 2.txt | tee 1.txt


