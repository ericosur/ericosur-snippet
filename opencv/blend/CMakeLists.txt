cmake_minimum_required(VERSION 3.0)

set(PN  "blend")

set(OpenCV_DIR    "/opt/intel/opencv/share/OpenCV")
#set(OpenCV_DIR    "/usr/local/share/OpenCV")
message("OpenCV_DIR: ${OpenCV_DIR}")
find_package( OpenCV REQUIRED )

include_directories(${OpenCV_INCLUDE_DIRS})

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
