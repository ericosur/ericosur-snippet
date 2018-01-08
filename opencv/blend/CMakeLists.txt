cmake_minimum_required(VERSION 2.8)

project(blend)

find_package( OpenCV REQUIRED )

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")

add_executable(blend blend.cpp)

target_link_libraries(
    blend
    ${OpenCV_LIBS}
)
