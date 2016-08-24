cmake_minimum_required(VERSION 2.6)

project(demo_function_pointer)

add_executable(demo_fp main.cpp foo.cpp)

message("CMAKE_SOURCE_DIR= ${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR= ${CMAKE_BINARY_DIR}")

