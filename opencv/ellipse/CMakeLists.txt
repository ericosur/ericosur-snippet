cmake_minimum_required(VERSION 3.0)

set(PN "ell")

project(${PN})

#set(OpenCV_DIR    "/usr/local/share/OpenCV")
message("OpenCV_DIR: ${OpenCV_DIR}")
find_package( OpenCV REQUIRED )
message("opencv ver: ${OpenCV_VERSION}")
include_directories(${OpenCV_INCLUDE_DIRS})
message("opencv inc: ${OpenCV_INCLUDE_DIRS}")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")
if(NOT ${CMAKE_SYSTEM_NAME} STREQUAL "Darwin")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")
endif()

add_executable(${PN}
    main.cpp
    drawutil.cpp drawutil.h
    hsv2rgb.cpp hsv2rgb.h
)

target_link_libraries(${PN} ${OpenCV_LIBS})

add_executable(
    drawtext
    drawtext.cpp
)
target_link_libraries(drawtext ${OpenCV_LIBS})

add_executable(
    imghash
    imghash.cpp
)
target_link_libraries(imghash ${OpenCV_LIBS})

add_executable(
    kal
    kal.cpp
)
target_link_libraries(kal ${OpenCV_LIBS})
