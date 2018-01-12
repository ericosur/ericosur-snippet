cmake_minimum_required(VERSION 2.8)

set(PN "faced")

project(${PN})

find_package( OpenCV REQUIRED )

include_directories("$ENV{HOME}/src/github/json/src/")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_CXX_FLAGS "-DUSE_JSON")

add_executable(
    ${PN}
    main.cpp
    face_demo.cpp
)

target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
)
