cmake_minimum_required(VERSION 2.6)

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")


include(armlinux.txt)
project(tostring)

add_executable(app main.cpp)

set_target_properties(
    app
    PROPERTIES
    COMPILE_FLAGS    -std=c++11
)
