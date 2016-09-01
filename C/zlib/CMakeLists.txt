cmake_minimum_required(VERSION 2.6)

message("CMAKE_SOURCE_DIR= ${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR= ${CMAKE_BINARY_DIR}")

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

project(zpipe)

add_executable(zpp zpipe.c)
target_link_libraries(zpp z)

add_executable(buffy buffy.c)
target_link_libraries(buffy z)

add_executable(demo example.c)
target_link_libraries(demo z)
