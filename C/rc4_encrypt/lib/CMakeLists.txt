cmake_minimum_required(VERSION 3.0)

find_package(OpenSSL REQUIRED)

if (${OPENSSL_FOUND})
    message("openssl found ==>")
    message("roodir:" ${OPENSSL_ROOT_DIR})
    message("include dir:" ${OPENSSL_INCLUDE_DIR})
    message("libs:" ${OPENSSL_LIBRARIES})
    message("version:" ${OPENSSL_VERSION})
endif ()

include_directories(/opt/local/include)

add_library(mytool STATIC toolbox.cpp)
target_link_libraries(mytool crypto)
