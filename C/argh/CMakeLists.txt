cmake_minimum_required(VERSION 3.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

include_directories("/usr/local/include")

project(argh)

add_executable(
    argh main.cpp argh.h
)

add_executable(
    exam example.cpp argh.h
)
