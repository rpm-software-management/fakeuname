add_compile_options(-fPIC -Wall -Wextra -O2 -g)

add_library(fakeuname SHARED fakeuname.c)
install(TARGETS fakeuname LIBRARY DESTINATION ${CMAKE_INSTALL_FULL_LIBDIR})
