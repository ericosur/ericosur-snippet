cmake_minimum_required(VERSION 3.0)

project(sendkey)

set(CMAKE_LEGACY_CYGWIN_WIN32 1)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS  "-Wall -O3")
set(CMAKE_C_FLAGS  "-Wall -O3")

add_executable(sk
    sendkey.h
    main.cpp
    sendkey.cpp
)
