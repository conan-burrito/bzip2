cmake_minimum_required(VERSION 3.1.2)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp)

find_package(BZip2 CONFIG REQUIRED)
target_link_libraries(example BZip2::BZip2)
