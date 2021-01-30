set(BINARY ${CMAKE_PROJECT_NAME})
set(BINARY_RUN ${BINARY}_run)
set(CMAKE_CXX_STANDARD 20)
set(CXX_STANDARD 20)


file(GLOB_RECURSE SOURCES LIST_DIRECTORIES true *.h *.cpp)

set(SOURCES ${SOURCES})

add_executable(${BINARY_RUN} ${SOURCES})

add_library(${BINARY}_lib STATIC ${SOURCES})
#DB
#file(CREATE_LINK "${PROJECT_SOURCE_DIR}/data/asc2018.sqlite" "${CMAKE_CURRENT_BINARY_DIR}/data.sqlite" COPY_ON_ERROR)
#Config file
#file(CREATE_LINK "${PROJECT_SOURCE_DIR}/config.ini" "${CMAKE_CURRENT_BINARY_DIR}/config.ini" COPY_ON_ERROR)
#file(CREATE_LINK "${PROJECT_SOURCE_DIR}/src/Kernel.cl" "${CMAKE_CURRENT_BINARY_DIR}/Kernel.cl" COPY_ON_ERROR)
#find_package(OpenCLHeaders REQUIRED)

target_link_libraries(${BINARY_RUN}
    pthread
    benchmark::benchmark
)
# Valgrind memcheck
#add_test(NAME ${CMAKE_PROJECT_NAME}_memcheck COMMAND "${memcheck_command} ./${BINARY}_run" )
