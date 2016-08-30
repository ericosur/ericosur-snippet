cmake_minimum_required (VERSION 2.6)

project(autotz)
add_executable(autotz autotz.cpp)

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")
