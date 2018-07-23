cmake_minimum_required(VERSION 3.0)

set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_CXX_FLAGS "-Wall -O3")
set(CMAKE_C_FLAGS "-Wall -O3")
set(CMAKE_CXX_STANDARD 11)

set(PN "eten")
project(${PN})

# usally we need to manually build libiconv, default is 0
set(USE_ICONV    0)

set(SOURCES
    main.cpp
    fontutil.cpp
)

set(MYLIBS
    mytool
)

if(USE_ICONV)
    message("USE_ICONV is ON")
    set(SOURCES    "${SOURCES} try_iconv.cpp")
    set(MYLIBS     "${MYLIBS}  libiconv.so")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}  -DUSE_ICONV")
endif()

find_package( OpenCV REQUIRED )

# mytool
link_directories("/usr/local/lib/mytool")
include_directories("/usr/local/include/mytool")

# libiconv
link_directories("/usr/local/lib")

add_executable(
    ${PN}
    ${SOURCES}
)

target_link_libraries(
    ${PN}
    ${OpenCV_LIBS}
    ${MYLIBS}
)
