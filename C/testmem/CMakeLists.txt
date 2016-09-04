cmake_minimum_required(VERSION 2.6)

#include (arm201405.txt)
#include (poky.txt)
#include (armlinux.txt)

message("CMAKE_SOURCE_DIR= ${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR= ${CMAKE_BINARY_DIR}")

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

project(testmem)

add_executable(testmemset testmemset.c)
add_executable(testmemcpy testmemcpy.c)
