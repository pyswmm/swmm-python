#
# CMakeLists.txt - CMake configuration file for swmm-toolkit python package
#
# Created:   Feb 6, 2020
# Modified   Sep 2, 2025
#
# Author:   See AUTHORS
#

# ###############################################################################
# #################    CMAKELISTS FOR SWMM-TOOLKIT PROJECT    ###################
# ###############################################################################

cmake_minimum_required(VERSION 4.0.2)

project(swmm-toolkit
    VERSION
    0.16.1
)

# Trick here is to perform build in a python virtual environment
set(Python_FIND_VIRTUALENV FIRST)

# set(CMAKE_FIND_DEBUG_MODE TRUE)
if(NOT MSVC)
    find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)
else()
    find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
endif()

# set(CMAKE_FIND_DEBUG_MODE FALSE)

# SWIG is a build requirement so needs to be installed first
find_package(SWIG REQUIRED)
cmake_policy(SET CMP0078 NEW)
cmake_policy(SET CMP0086 NEW)
include(${SWIG_USE_FILE})

# Add project subdirectories
add_subdirectory(swmm-solver)

add_subdirectory(src/swmm/toolkit)
