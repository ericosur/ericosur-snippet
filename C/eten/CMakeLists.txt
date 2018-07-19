cmake_minimum_required(VERSION 3.0)

set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")
set(CMAKE_CXX_STANDARD 11)

set(PN "eten")
project(${PN})

find_package( OpenCV REQUIRED )


add_executable(
    ${PN}
    main.cpp
    fontutil.cpp
)


target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
)
