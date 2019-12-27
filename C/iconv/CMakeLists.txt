cmake_minimum_required(VERSION 3.0)

set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")
set(CMAKE_CXX_STANDARD 11)

set(PN "icv")
project(${PN})

add_executable(
    ${PN}
    try_iconv.cpp
)

# include_directories("/usr/include/glib-2.0")
# include_directories("/usr/lib/x86_64-linux-gnu/glib-2.0/include")

link_directories("/home/rasmus/anaconda2/lib")
target_link_libraries(${PN} libiconv.so)
