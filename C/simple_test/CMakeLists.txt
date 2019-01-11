cmake_minimum_required(VERSION 3.0)

# before using it, setup vars for ICC
# source /opt/intel/system_studio_2018/bin/compilervars.sh \
#      -arch intel64 -platform linux
# turn it on via CLI:
# cmake -DINTEL=1 ..
#
if(INTEL)
    message("turn on ICC!")
    set(CMAKE_C_COMPILER    "icc")
    set(CMAKE_CXX_COMPILER  "icpc")
endif()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

project(easytest)

add_executable(rfind rfind.cpp)
add_executable(getret getret.cpp)
add_executable(gete gete.cpp)
add_executable(hello_world hello_world.cpp json.hpp)
add_executable(mul mul.cpp)
add_executable(fib fib.c)
add_executable(memmove memmove.c)
add_executable(delete_null  delete_null.cpp)
add_executable(shift  shift.cpp)
add_executable(atan  atan.cpp)