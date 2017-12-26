cmake_minimum_required (VERSION 2.6)

project(easytest)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

add_executable(rfind rfind.cpp)
add_executable(getret getret.cpp)
add_executable(gete e.cpp)
