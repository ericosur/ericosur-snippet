cmake_minimum_required(VERSION 3.5)

project(rc4_encrypt)

#set(BUILD_DOCUMENTATION YES)

set(CMAKE_CXX_FLAGS "-Wall -O3")
find_package(OpenSSL REQUIRED)

add_subdirectory(./lib/)
include_directories(./lib/)
add_subdirectory(./doc/)

# it's too new for cross compiler
add_executable(mymd md5main.cpp)
add_executable(myrc rc4main.cpp)
add_executable(myenc myenc.cpp)
add_executable(mydec mydec.cpp)
add_executable(hdr ReadHeader.cpp)

target_link_libraries(mymd mytool crypto)
target_link_libraries(myrc mytool crypto)
target_link_libraries(myenc mytool crypto)
target_link_libraries(mydec mytool crypto)
target_link_libraries(hdr mytool crypto)
