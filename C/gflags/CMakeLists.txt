cmake_minimum_required(VERSION 3.0)

set(CMAKE_VERBOSE_MAKEFILE off)
set(CMAKE_CXX_STANDARD 11)
set(MYUSERNAME    $ENV{USER})
set(MYLOCALGFLAGS "/home/${MYUSERNAME}/src/github/gflags")

project(demo)
find_package(gflags REQUIRED)

message("my local gflags dir: ${MYLOCALGFLAGS}")
include_directories("${MYLOCALGFLAGS}/build/include")
link_directories("${MYLOCALGFLAGS}/build/lib")

add_executable(demo demo.cpp)
target_link_libraries(demo gflags pthread)
