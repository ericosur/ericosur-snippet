cmake_minimum_required(VERSION 2.6)

#include (arm201405.txt)
#include (poky.txt)
#include (armlinux.txt)

message("CMAKE_SOURCE_DIR= ${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR= ${CMAKE_BINARY_DIR}")

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3 -std=c++11")
set(CMAKE_C_FLAGS "-Wall -O3 -std=c99")

project(enlarge)

add_executable(enlarge enlarge.c)
target_link_libraries(enlarge freeimage)

#set_target_properties(
#    main c11
#    PROPERTIES
#    COMPILE_FLAGS    -std=c++11
#)
