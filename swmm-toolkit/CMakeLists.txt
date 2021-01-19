#
# CMakeLists.txt - CMake configuration file for swmm-toolkit python package
#
# Created:   Feb 6, 2020
# Modified   Jan 12, 2021
#
#  Author:     See AUTHORS
#


cmake_minimum_required (VERSION 3.17)

project(swmm-toolkit
    VERSION
        0.8.1
)


find_package(PythonExtensions REQUIRED)
    message(STATUS "PYTHON_PREFIX=${PYTHON_PREFIX}")

set(Python_FIND_VIRTUALENV FIRST)
#set(Python3_ROOT_DIR ${PYTHON_PREFIX})
#set(Python3_EXECUTABLE ${PYTHON_PREFIX}/bin)
#set(Python3_LIBRARY ${PYTHON_PREFIX}/lib)
#set(Python3_INCLUDE_DIRS ${PYTHON_PREFIX}/include)

set(CMAKE_FIND_DEBUG_MODE TRUE)
    find_package (Python3 ${PYTHON_VERSION_STRING} COMPONENTS Interpreter Development.Module)
set(CMAKE_FIND_DEBUG_MODE FALSE)

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
            ${PROJECT_SOURCE_DIR}/tools/relocate.zsh ${EXTERN_LIB_PATH}
        WORKING_DIRECTORY
            ${CMAKE_INSTALL_PREFIX}
        )"
    )
endif()
