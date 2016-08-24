cmake_minimum_required(VERSION 2.6)

message("CMAKE_SOURCE_DIR= ${CMAKE_SOURCE_DIR}")
message("CMAKE_BINARY_DIR= ${CMAKE_BINARY_DIR}")

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

project(demos)

add_executable(c11 c11.cpp)
add_executable(c14 c14.cpp)
add_executable(main
    main.cpp myinc.cpp myinc.cpp foo.h)
add_executable(rdln rl.c)
add_executable(mytimer mytimer.cpp)
add_executable(myalarm myalarm.cpp)

set_target_properties(
    main c11
    PROPERTIES
    COMPILE_FLAGS    -std=c++11
)

set_target_properties(
    c14
    PROPERTIES
    COMPILE_FLAGS    -std=c++14
)

target_link_libraries(
    rdln
    readline
)
