cmake_minimum_required(VERSION 3.0)

set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")
set(CMAKE_CXX_STANDARD 11)

set(PN "eten")
project(${PN})

find_package( OpenCV REQUIRED )

# mytool
link_directories("/usr/local/lib/mytool")
include_directories("/usr/local/include/mytool")

# libiconv
link_directories("/usr/local/lib")

add_executable(
    ${PN}
    main.cpp
    fontutil.cpp
    try_iconv.cpp
)

target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
    mytool
    libiconv.so
)
