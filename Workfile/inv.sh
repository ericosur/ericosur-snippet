#!/bin/bash 

CLANGDIR=$HOME/Downloads/llvm/clang+llvm-3.7.1-x86_64-linux-gnu-ubuntu-14.04
ARMTOOL=$HOME/arm2014.05

CLANG=$CLANGDIR/bin/clang-3.7
SYSROOT=$ARMTOOL/arm-none-linux-gnueabi/libc
BEGINDIR=$ARMTOOL/lib/gcc/arm-none-linux-gnueabi/4.8.3

export PATH=$ARMTOOL/bin:$CLANGDIR/bin:$PATH
 
cd $BEGINDIR
$CLANG -target arm-none-linux-gnueabi  --sysroot=$SYSROOT \
  -O3 \
  -I${SYSROOT}/include  \
  -L${BEGINDIR}         \
  -static      \
  -o $HOME/abu-clang-arm  \
  $HOME/Dropbox/abundant.c

#  ${ARMTOOL}/lib/gcc/arm-none-linux-gnueabi/4.8.3/crtbegin.o \

