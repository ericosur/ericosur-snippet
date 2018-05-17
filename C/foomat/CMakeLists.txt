cmake_minimum_required (VERSION 3.0)

project(foo)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

add_executable(
    foo
    main.cpp
    mymat.cpp
)
