#
# CMakeLists.txt - CMake configuration file for swmm-toolkit python package
#
# Created:   Feb 6, 2020
# Modified   Jan 12, 2021
#
#  Author:     See AUTHORS
#

################################################################################
##################    CMAKELISTS FOR SWMM-TOOLKIT PROJECT    ###################
################################################################################

cmake_minimum_required (VERSION 3.17)

project(swmm-toolkit
    VERSION
        0.8.1
)


# TODO: Figure out how to use this
#find_package(PythonExtensions REQUIRED)
#message(STATUS "PYTHON_PREFIX=${PYTHON_PREFIX}")


# Trick here is to perform build in a python virtual environment
set(Python_FIND_VIRTUALENV FIRST)
find_package (Python3 ${PYTHON_VERSION_STRING} COMPONENTS Interpreter Development.Module)


# SWIG is a build requirement so needs to be installed first
find_package(SWIG REQUIRED)
cmake_policy(SET CMP0078 NEW)
cmake_policy(SET CMP0086 NEW)
include(${SWIG_USE_FILE})


# This gets passed down the project tree to trigger rpath configuration
option(BUILD_WHEEL "Configure for python wheel build" ON)


add_subdirectory(swmm-solver)

add_subdirectory(src/swmm/toolkit)


# Relocate external libs into install package
#if(NOT MSVC)
#    install(CODE "execute_process(
#        COMMAND
#            ${PROJECT_SOURCE_DIR}/tools/relocate.$<$<BOOL:${APPLE}>:z>sh ${EXTERN_LIB_PATH}
#        WORKING_DIRECTORY
#            ${CMAKE_INSTALL_PREFIX}
#        )"
#    )
#endif()
