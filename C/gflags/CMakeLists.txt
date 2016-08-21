project(demo)
cmake_minimum_required(VERSION 2.8)
set(CMAKE_VERBOSE_MAKEFILE off)

find_package(gflags REQUIRED)

include_directories("/home/ericosur/src/github/gflags/build/include")
link_directories("/home/ericosur/src/github/gflags/build/lib")

add_executable(demo demo.cpp)
target_link_libraries(demo gflags pthread)
