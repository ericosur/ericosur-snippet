cmake_minimum_required(VERSION 3.0)

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")

set(CMAKE_CXX_STANDARD 11)
#include(armlinux.txt)

set(USE_GLIB    1)

set(PN "hex")
project(${PN})

add_executable(
    ${PN}
    main.cpp
    charutil.cpp
)


if(USE_GLIB)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DUSE_GLIB")
    include_directories("/usr/include/glib-2.0")
    include_directories("/usr/lib/x86_64-linux-gnu/glib-2.0/include")
    target_link_libraries(${PN} glib-2.0)
endif()

