cmake_minimum_required(VERSION 3.0)

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

set(CMAKE_CXX_STANDARD 11)
#include(armlinux.txt)

set(PN "hex")

project(${PN})

add_executable(
    ${PN}
    main.cpp
    charutil.cpp
)
