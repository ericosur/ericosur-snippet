cmake_minimum_required(VERSION 3.0)

# before using it, setup vars for ICC
# source /opt/intel/system_studio_2018/bin/compilervars.sh \
#      -arch intel64 -platform linux
# turn it on via CLI:
# cmake -DUSE_INTEL=1 ..

# use clang...
# cmake -DUSE_CLANG=1 ..


project(fmt_demo)


if(USE_INTEL)
    message("turn on ICC!")
    set(CMAKE_C_COMPILER    "icc")
    set(CMAKE_CXX_COMPILER  "icpc")
endif()
if(USE_CLANG)
    message("turn on clang!")
    set(CMAKE_C_COMPILER    "clang")
    set(CMAKE_CXX_COMPILER  "clang++")
endif()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

include_directories("/usr/local/include")

# for library __fmt__
set(FMT_BASEDIR     "../fmt")
include_directories("${FMT_BASEDIR}/include")
add_executable(
    fmt
    main.cpp
    tests.cpp
    ${FMT_BASEDIR}/src/format.cc
)
