project(demo)
cmake_minimum_required(VERSION 2.8)
set(CMAKE_VERBOSE_MAKEFILE off)

find_package(gflags REQUIRED)

set(MYUSERNAME    $ENV{USER})
set(MYLOCALGFLAGS "/home/${MYUSERNAME}/src/github/gflags")
message("my local gflags dir: ${MYLOCALGFLAGS}")
include_directories("${MYLOCALGFLAGS}/build/include")
link_directories("${MYLOCALGFLAGS}/build/lib")

add_executable(demo demo.cpp)
target_link_libraries(demo gflags pthread)
