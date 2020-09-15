#
# CMakeLists.txt - CMake configuration file for swmm-toolkit python package
#
# Created:   Feb 6, 2020
# Modified   May 7, 2020
#
# Author: Michael E. Tryby
#         US EPA ORD/CESER
#


cmake_minimum_required (VERSION 3.17)

project(swmm-toolkit)

#set(Python_FIND_VIRTUALENV FIRST)

#set(Python_ROOT_DIR "/opt/python/cp37-cp37mu")
#set(Python_INCLUDE_DIR ${PYTHON_INCLUDE_DIR})
#set(Python_LIBRARY ${Python_ROOT_DIR}/)
find_package (Python 3.7 COMPONENTS Interpreter Development REQUIRED)


find_package(SWIG REQUIRED)
cmake_policy(SET CMP0078 NEW)
cmake_policy(SET CMP0086 NEW)
include(${SWIG_USE_FILE})


add_subdirectory(swmm-solver)


add_subdirectory(src/swmm/toolkit)


# Relocate external libs into install package
if(APPLE)
    install(CODE "execute_process(
        COMMAND
            ${PROJECT_SOURCE_DIR}/swmm-solver/tools/relocate.zsh ${EXTERN_LIB_PATH}
        WORKING_DIRECTORY
            ${CMAKE_INSTALL_PREFIX}
        )"
    )
endif()
