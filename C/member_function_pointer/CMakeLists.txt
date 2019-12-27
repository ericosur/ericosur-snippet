cmake_minimum_required(VERSION 3.0)

project(demo_function_pointer)
set(CMAKE_CXX_STANDARD 11)

message("CMAKE_SOURCE_DIR= ${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR= ${CMAKE_BINARY_DIR}")

add_executable(demo_fp main.cpp foo.cpp)
