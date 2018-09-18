cmake_minimum_required(VERSION 2.8)

set(PN "cvfoo")
project(${PN})

find_package( OpenCV REQUIRED )

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")
if(NOT ${CMAKE_SYSTEM_NAME} STREQUAL "Darwin")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")
endif()

add_executable(${PN} main.cpp)

target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
)
