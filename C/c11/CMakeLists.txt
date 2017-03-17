cmake_minimum_required(VERSION 2.6)

#include (arm201405.txt)
#include (poky.txt)
#include (armlinux.txt)

message("CMAKE_SOURCE_DIR= ${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR= ${CMAKE_BINARY_DIR}")

set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

project(demos)

add_executable(c11 c11.cpp)
add_executable(main
    main.cpp myinc.cpp myinc.cpp foo.h)
add_executable(mytimer mytimer.cpp)
add_executable(myalarm myalarm.cpp)

# comment out if compiler too old
add_subdirectory(c14/)
add_subdirectory(readln/)

