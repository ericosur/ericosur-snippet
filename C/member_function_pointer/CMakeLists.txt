cmake_minimum_required(VERSION 3.0)

####### use clang #######
# cd path/to/clang/bin/
# export PATH=$PWD:$PATH
# cd -
# cmake -DUSE_CLANG=1 ..
#########################

if(USE_CLANG)
    message("turn on clang!")
    set(CMAKE_C_COMPILER    "clang")
    set(CMAKE_CXX_COMPILER  "clang++")
endif()


project(demo_function_pointer)
set(CMAKE_CXX_STANDARD 11)

message("CMAKE_SOURCE_DIR= ${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR= ${CMAKE_BINARY_DIR}")

add_executable(demo_fp main.cpp foo.cpp)
