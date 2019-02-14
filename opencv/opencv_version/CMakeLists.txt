cmake_minimum_required(VERSION 3.0)

set(PN "opencv_version")
project(${PN})

set(OpenCV_DIR    "/opt/intel/opencv/share/OpenCV")
#set(OpenCV_DIR    "/usr/local/share/OpenCV")
find_package( OpenCV REQUIRED )

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")
if(NOT ${CMAKE_SYSTEM_NAME} STREQUAL "Darwin")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")
endif()

# eg: Linux 2.14.xx
message("cmake system: ${CMAKE_SYSTEM_NAME}-${CMAKE_SYSTEM_VERSION}-${CMAKE_SYSTEM_PROCESSOR}")

#      - OpenCV_LIBS                     : The list of all imported targets for OpenCV modules.
#      - OpenCV_INCLUDE_DIRS             : The OpenCV include directories.
#      - OpenCV_COMPUTE_CAPABILITIES     : The version of compute capability.
#      - OpenCV_ANDROID_NATIVE_API_LEVEL : Minimum required level of Android API.
#      - OpenCV_VERSION                  : The version of this OpenCV build: "3.4.2"
#      - OpenCV_VERSION_MAJOR            : Major version part of OpenCV_VERSION: "3"
#      - OpenCV_VERSION_MINOR            : Minor version part of OpenCV_VERSION: "4"
#      - OpenCV_VERSION_PATCH            : Patch version part of OpenCV_VERSION: "2"
#      - OpenCV_VERSION_STATUS           : Development status of this build: ""
#    Advanced variables:
#      - OpenCV_SHARED                   : Use OpenCV as shared library
#      - OpenCV_INSTALL_PATH             : OpenCV location
#      - OpenCV_LIB_COMPONENTS           : Present OpenCV modules list
#      - OpenCV_USE_MANGLED_PATHS        : Mangled OpenCV path flag

message("INFO: opencv version: ${OpenCV_VERSION}${OpenCV_VERSION_STATUS}")
message("INFO: opencv include dirs: ${OpenCV_INCLUDE_DIRS}")
message("INFO: opencv libs: ${OpenCV_LIBS}")

add_executable(${PN}    main.cpp)
target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
)

