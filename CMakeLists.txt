cmake_minimum_required(VERSION 3.1.2)
project(bzip2 C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(MSVC OR MSVC90 OR MSVC10)
    set(MSVC ON)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()

set(BZ2_LIBRARY BZip2)
set(BZ2_NAMESPACE BZip2)
set(BZ2_CONFIG ${BZ2_NAMESPACE}Config)

add_library(${BZ2_LIBRARY}
    src/blocksort.c
    src/bzlib.c
    src/compress.c
    src/crctable.c
    src/decompress.c
    src/huffman.c
    src/randtable.c
)
target_include_directories(${BZ2_LIBRARY} PRIVATE src)
set_target_properties(${BZ2_LIBRARY} PROPERTIES OUTPUT_NAME bz2)

set_target_properties(${BZ2_LIBRARY}
    PROPERTIES
        VERSION ${BZ2_VERSION_STRING}
        SOVERSION ${BZ2_VERSION_MAJOR}
)

export(
    TARGETS ${BZ2_LIBRARY}
    NAMESPACE ${BZ2_NAMESPACE}::
    FILE "${CMAKE_CURRENT_BINARY_DIR}/${BZ2_CONFIG}.cmake"
)

include(GNUInstallDirs)
install(
    TARGETS ${BZ2_LIBRARY}
    EXPORT ${BZ2_CONFIG}
    BUNDLE DESTINATION ${CMAKE_INSTALL_BINDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
install(FILES src/bzlib.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(
    EXPORT ${BZ2_CONFIG}
    DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/${CMAKE_PROJECT_NAME}"
    NAMESPACE ${BZ2_NAMESPACE}::
)
