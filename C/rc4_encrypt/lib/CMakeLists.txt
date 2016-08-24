cmake_minimum_required(VERSION 3.0)

find_package(OpenSSL REQUIRED)

add_library(mytool STATIC toolbox.cpp)
target_link_libraries(mytool crypto)
