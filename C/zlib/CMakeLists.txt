cmake_minimum_required(VERSION 3.0)

message("CMAKE_SOURCE_DIR=${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR=${CMAKE_BINARY_DIR}")

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3 -std=c99")

project(zpipe)

add_executable(zpp zpipe.c)
target_link_libraries(zpp z)

add_executable(buffy buffy.c)
target_link_libraries(buffy z)

add_executable(demo example.c)
target_link_libraries(demo z)
