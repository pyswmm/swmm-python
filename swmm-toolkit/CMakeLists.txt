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

cmake_policy(SET CMP0094 NEW)
#set(Python_FIND_VIRTUALENV FIRST)
set(Python3_ROOT_DIR "/opt/_internal/cpython-3.7.7")
find_package (Python3 COMPONENTS Interpreter Development)


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
