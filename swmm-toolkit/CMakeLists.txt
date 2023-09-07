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
        0.15.0
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

if(APPLE)
    set(CMAKE_C_COMPILER clang)
    set(CMAKE_CXX_COMPILER clang++)

    if(CMAKE_C_COMPILER_ID MATCHES "Clang\$")
        set(OpenMP_C_FLAGS "-Xpreprocessor -fopenmp")
        set(OpenMP_C_LIB_NAMES "omp")
        set(OpenMP_omp_LIBRARY omp)
    endif()

    if(CMAKE_CXX_COMPILER_ID MATCHES "Clang\$")
        set(OpenMP_CXX_FLAGS "-Xpreprocessor -fopenmp")
        set(OpenMP_CXX_LIB_NAMES "omp")
        set(OpenMP_omp_LIBRARY omp)
    endif()

endif()

find_package(OpenMP
    REQUIRED
    OPTIONAL_COMPONENTS
        C
)

# Add project subdirectories
add_subdirectory(swmm-solver)

add_subdirectory(src/swmm/toolkit)
