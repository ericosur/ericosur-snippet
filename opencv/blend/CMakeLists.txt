cmake_minimum_required(VERSION 3.0)

set(PN  "blend")

find_package( OpenCV REQUIRED )

project(${PN})
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")
if(NOT ${CMAKE_SYSTEM_NAME} STREQUAL "Darwin")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")
endif()

add_executable(${PN} blend.cpp)
target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
)

add_executable(
    cvcat
    cat.cpp
)
target_link_libraries(
    cvcat
    ${OpenCV_LIBS}
)
