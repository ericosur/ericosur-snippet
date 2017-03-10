cmake_minimum_required(VERSION 2.6)

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

project(demos)

add_executable(c14 c14.cpp)
add_executable(cpp14 cpp14.cpp)

set_target_properties(
    c14
    cpp14
    PROPERTIES
    COMPILE_FLAGS    -std=c++14
)
