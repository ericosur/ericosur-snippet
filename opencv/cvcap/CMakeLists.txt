cmake_minimum_required(VERSION 3.0)

set(PN "cvcap")

project(${PN})

#set(OpenCV_DIR    "/opt/intel/opencv/share/OpenCV")
set(OpenCV_DIR    "/usr/local/share/OpenCV")
find_package( OpenCV REQUIRED )

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")
if(NOT ${CMAKE_SYSTEM_NAME} STREQUAL "Darwin")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")
endif()

add_executable(
    ${PN}
    main.cpp
)
target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
)

add_executable(qrcode qrcode.cpp)
target_link_libraries(qrcode ${OpenCV_LIBS})
