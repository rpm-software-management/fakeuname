cmake_minimum_required(VERSION 2.8.5)

set(VERSION 1.0.0)
if(${CMAKE_VERSION} VERSION_LESS "3.0.0")
    project(fakeuname C)
    set(PROJECT_VERSION ${VERSION})
else()
    cmake_policy(VERSION 3.0.0)
    project(fakeuname LANGUAGES C VERSION ${VERSION})
endif()

include(GNUInstallDirs)

configure_file("fakeuname.in" "fakeuname" @ONLY)
install(PROGRAMS "fakeuname" DESTINATION ${CMAKE_INSTALL_FULL_BINDIR})

add_subdirectory("src")
