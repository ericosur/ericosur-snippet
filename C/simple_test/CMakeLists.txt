cmake_minimum_required(VERSION 3.0)

##### use Intel ICC #####
# before using it, setup vars for ICC
# source /opt/intel/system_studio_2018/bin/compilervars.sh \
#      -arch intel64 -platform linux
# turn it on via CLI:
# cmake -DUSE_INTEL=1 ..

####### use clang #######
# cd path/to/clang/bin/
# export PATH=$PWD:$PATH
# cd -
# cmake -DUSE_CLANG=1 ..
#########################

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

project(easytest)

add_executable(rfind rfind.cpp)
add_executable(getret getret.cpp)
add_executable(gete gete.cpp)
add_executable(hello_tester
    hello_tester.cpp
    boxmuller.cpp
    test_func.cpp
    test_json.cpp
)
add_executable(mul mul.cpp)
add_executable(fib fib.c)
add_executable(memmove memmove.c)
add_executable(delete_null  delete_null.cpp)
add_executable(shift  shift.cpp)
#add_executable(atan  atan.cpp)

add_executable(test_jvs  test_jvs.c  jvs.c)
add_executable(nullptr  nullptr.cpp)

add_executable(validate_utf8 validate_utf8.cpp)
add_executable(hexdec hexdec.cpp)

add_executable(boss    boss.c)
add_executable(worker  worker.c)
