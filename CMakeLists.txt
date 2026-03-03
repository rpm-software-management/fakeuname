cmake_minimum_required(VERSION 3.5.0)

set(VERSION 1.0.0)
project(fakeuname LANGUAGES C VERSION ${VERSION})

include(GNUInstallDirs)

configure_file("fakeuname.in" "fakeuname" @ONLY)
install(PROGRAMS "${CMAKE_BINARY_DIR}/fakeuname" DESTINATION ${CMAKE_INSTALL_FULL_BINDIR})

add_subdirectory("src")
