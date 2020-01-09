cmake_minimum_required(VERSION 3.0)

####### use clang #######
# cd path/to/clang/bin/
# export PATH=$PWD:$PATH
# cd -
# cmake -DUSE_CLANG=1 ..
#########################

if(USE_CLANG)
    message("turn on clang!")
    set(CMAKE_C_COMPILER    "clang")
    set(CMAKE_CXX_COMPILER  "clang++")
endif()

set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

#include(armlinux.txt)
project(tostring)

add_executable(app main.cpp)
