#
# CMakeLists.txt - CMake configuration file for swmm-toolkit python package
#
# Created:   Feb 6, 2020
# Modified:
#
# Author: Michael E. Tryby
#         US EPA ORD/CESER
#
# Usage:
#   python setup.py build -- -G"Visual Studio 15 2017 Win64" ..
#


cmake_minimum_required (VERSION 3.13)

project(swmm-toolkit)


set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)


set(Python_FIND_VIRTUALENV FIRST)
set(Python_ROOT_DIR "/usr/local/anaconda3")
find_package(Python 3.7 COMPONENTS Development Interpreter)
message(STATUS "Python_VERSION: ${Python_VERSION}")


find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})


add_subdirectory(swmm-solver)


add_subdirectory(src/swmm/toolkit)
