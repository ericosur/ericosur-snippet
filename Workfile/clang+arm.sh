#!/bin/bash 

# this script demos how to use clang as compiler
# and arm2014.05 as cross compiler
# to static link a c source

# may use this command to replace 'ldd'
# $ LD_TRACE_LOADED_OBJECTS=1 /bin/grep

CLANGDIR=$HOME/Downloads/llvm/clang+llvm-3.7.1-x86_64-linux-gnu-ubuntu-14.04
ARMTOOL=$HOME/arm2014.05

CLANG=$CLANGDIR/bin/clang-3.7
SYSROOT=$ARMTOOL/arm-none-linux-gnueabi/libc
BEGINDIR=$ARMTOOL/lib/gcc/arm-none-linux-gnueabi/4.8.3

export PATH=$ARMTOOL/bin:$CLANGDIR/bin:$PATH
 
cd $BEGINDIR
$CLANG -target arm-none-linux-gnueabi  --sysroot=$SYSROOT \
  -I${SYSROOT}/include  \
  -L${BEGINDIR}         \
  -static      \
  -o $HOME/fib \
  $HOME/gcode/snippet/C/fib.c

#  ${ARMTOOL}/lib/gcc/arm-none-linux-gnueabi/4.8.3/crtbegin.o \

