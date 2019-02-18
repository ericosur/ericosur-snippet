cmake_minimum_required(VERSION 3.0)

set(PN "imdecode")
project(${PN})

set(CMAKE_CXX_FLAGS "-Wall -O3")

set(CMAKE_CXX_STANDARD 11)
set(APPLY_JSON         1)
set(APPLY_MYTOOL       0)

# opencv is MUST
find_package( OpenCV REQUIRED )
set(DEPENDENCIES ${OpenCV_LIBS})

include_directories("/usr/local/include")

if(APPLY_MYTOOL)
    link_directories("/usr/local/lib/mytool")
    set(MYTOOL "libmytool.so")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DUSE_MYTOOL")
endif()

# json.hpp
if(APPLY_JSON)
    # message("apply json.hpp, use json.hpp from github repository")
    # include_directories("$ENV{HOME}/src/github/json/single_include/nlohmann")
    message("apply json.hpp, use json.hpp from /usr/local/include")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DUSE_JSON")
endif()



message("====> DEPENDENCIES: ${DEPENDENCIES}")

add_executable(
    ${PN}
    main.cpp
)

target_link_libraries(
    ${PN}
    ${DEPENDENCIES}
    ${MYTOOL}
)
