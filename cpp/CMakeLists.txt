cmake_minimum_required(VERSION 3.13)

set(CMAKE_C_COMPILER "gcc")
set(CMAKE_CXX_COMPILER "g++")

project(SortingAlgsBenchmarking VERSION 0.1.0)

#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
set(CPACK_PROJECT_NAME ${PROJECT_NAME})

include(CTest) 

include_directories(libs/benchmark/include)
add_subdirectory(libs/benchmark)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_C_COMPILER_WORKS 1)

include_directories(src)
add_subdirectory(src)

include(CPack)
