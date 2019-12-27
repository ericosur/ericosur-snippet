cmake_minimum_required(VERSION 3.0)

# uncomment the next line if using android ndk standalone toolchain
#include (ndk.txt)

message("CMAKE_SOURCE_DIR=${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR=${CMAKE_BINARY_DIR}")

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

project(testmem)

add_executable(testmemset testmemset.c)
add_executable(testmemcpy testmemcpy.c)

set_target_properties(
    testmemset
    testmemcpy
    PROPERTIES
    COMPILE_FLAGS -std=c99
)

