project(readln)

add_executable(rdln rl.c)

target_link_libraries(
    rdln
    readline
)
