cmake_minimum_required(VERSION 3.0)

# before using it, setup vars for ICC
# source /opt/intel/system_studio_2018/bin/compilervars.sh \
#      -arch intel64 -platform linux
# turn it on via CLI:
# cmake -DINTEL=1 ..

if(INTEL)
    message("turn on ICC!")
    set(CMAKE_C_COMPILER    "icc")
    set(CMAKE_CXX_COMPILER  "icpc")
endif()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

project(stl)

add_executable(
    min
    min.cpp)
add_executable(
    shuffle
    shuffle.cpp)
add_executable(
    intersection
    intersection.cpp)
add_executable(
    dist
    dist.cpp)
