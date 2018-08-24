cmake_minimum_required(VERSION 2.8)

set(PN "faced")

project(${PN})

find_package( OpenCV REQUIRED )

# for json.hpp
include_directories("/usr/local/include")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DUSE_JSON")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")

add_executable(
    ${PN}
    main.cpp
    face_demo.cpp
)

target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
)
