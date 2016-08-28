cmake_minimum_required(VERSION 3.5)

project(md5test)

set(CMAKE_CXX_FLAGS "-Wall -O3")
find_package(OpenSSL REQUIRED)

# it's too new for cross compiler
add_executable(md5test main.cpp toolbox.cpp)

target_link_libraries(md5test crypto)
