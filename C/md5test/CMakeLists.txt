cmake_minimum_required(VERSION 3.0)

set(PN    md5test)

set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")
set(CMAKE_CXX_STANDARD 11)

project(${PN})
find_package(OpenSSL REQUIRED)

# it's too new for cross compiler
add_executable(${PN}
    main.cpp
    toolbox.cpp
)

target_link_libraries(${PN}
    crypto
)
