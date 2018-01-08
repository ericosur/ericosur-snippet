cmake_minimum_required(VERSION 2.8)

set(PN "capture")

project(${PN})

find_package( OpenCV REQUIRED )

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")

add_executable(
    ${PN}
    main.cpp
    captureDemo.cpp
)

target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
)
