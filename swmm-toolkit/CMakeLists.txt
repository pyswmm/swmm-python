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


set(Python_EXECUTABLE ${PYTHON_EXECUTABLE})
set(Python_INCLUDE_DIRS ${PYTHON_INCLUDE_DIR})
set(Python_LIBRARY ${PYTHON_LIBRARY})
find_package (Python ${PYTHON_VERSION_STRING} COMPONENTS Interpreter Development)


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
