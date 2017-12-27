project(mycurl)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall -O3")

add_executable(mycurl mycurl.cpp)

target_link_libraries(
    mycurl
    curl
)
