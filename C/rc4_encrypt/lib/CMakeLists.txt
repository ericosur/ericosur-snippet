cmake_minimum_required(VERSION 3.0)

add_library(mytool STATIC toolbox.cpp)
find_package(OpenSSL REQUIRED)

if (${OPENSSL_FOUND})
    message("openssl found ==>")
    message("version:" ${OPENSSL_VERSION})
    message("roodir:" ${OPENSSL_ROOT_DIR})
    message("include dir:" ${OPENSSL_INCLUDE_DIR})
    include_directories(${OPENSSL_INCLUDE_DIR})
    message("libs:" ${OPENSSL_LIBRARIES})
    target_link_libraries(mytool ${OPENSSL_LIBRARIES})
endif ()

