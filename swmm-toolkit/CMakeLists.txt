#
# CMakeLists.txt - CMake configuration file for swmm-toolkit python package
#
# Created:   Feb 6, 2020
# Modified   Jun 7, 2021
#
#  Author:   See AUTHORS
#

################################################################################
##################    CMAKELISTS FOR SWMM-TOOLKIT PROJECT    ###################
################################################################################

cmake_minimum_required (VERSION 3.17)

project(swmm-toolkit
    VERSION
        0.9.0
)


# Trick here is to perform build in a python virtual environment
set(Python_FIND_VIRTUALENV FIRST)
#set(CMAKE_FIND_DEBUG_MODE TRUE)
if(NOT MSVC)
    find_package (Python3 ${PYTHON_VERSION_STRING} COMPONENTS Interpreter Development.Module REQUIRED)
else()
    find_package (Python3 ${PYTHON_VERSION_STRING} COMPONENTS Interpreter Development REQUIRED)
endif()
#set(CMAKE_FIND_DEBUG_MODE FALSE)


# SWIG is a build requirement so needs to be installed first
find_package(SWIG REQUIRED)
cmake_policy(SET CMP0078 NEW)
cmake_policy(SET CMP0086 NEW)
include(${SWIG_USE_FILE})


# If wheel build on Apple fetch and build OpenMP Library
if (APPLE)
    include(./extern/openmp.cmake)
else()
    find_package(OpenMP
        OPTIONAL_COMPONENTS
            C
    )
endif()


# Add project subdirectories
add_subdirectory(swmm-solver)

add_subdirectory(src/swmm/toolkit)
