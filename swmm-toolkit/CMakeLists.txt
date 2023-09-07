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

OPTION (USE_OpenMP "Use OpenMP to enamble <omp.h>" ON)
# Find OpenMP
if(APPLE AND USE_OpenMP)
    if(CMAKE_C_COMPILER_ID MATCHES "Clang")
        set(OpenMP_C "${CMAKE_C_COMPILER}")
        set(OpenMP_C_FLAGS "-fopenmp=libomp -Wno-unused-command-line-argument")
        set(OpenMP_C_LIB_NAMES "libomp" "libgomp" "libiomp5")
        set(OpenMP_libomp_LIBRARY ${OpenMP_C_LIB_NAMES})
        set(OpenMP_libgomp_LIBRARY ${OpenMP_C_LIB_NAMES})
        set(OpenMP_libiomp5_LIBRARY ${OpenMP_C_LIB_NAMES})
    endif()
    if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
      set(OpenMP_CXX "${CMAKE_CXX_COMPILER}")
      set(OpenMP_CXX_FLAGS "-fopenmp=libomp -Wno-unused-command-line-argument")
      set(OpenMP_CXX_LIB_NAMES "libomp" "libgomp" "libiomp5")
      set(OpenMP_libomp_LIBRARY ${OpenMP_CXX_LIB_NAMES})
      set(OpenMP_libgomp_LIBRARY ${OpenMP_CXX_LIB_NAMES})
      set(OpenMP_libiomp5_LIBRARY ${OpenMP_CXX_LIB_NAMES})
    endif()
endif()

if(USE_OpenMP)
  find_package(OpenMP REQUIRED)
endif(USE_OpenMP)

if (OPENMP_FOUND)
    include_directories("${OPENMP_INCLUDES}")
    link_directories("${OPENMP_LIBRARIES}")
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    # set (CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
endif(OPENMP_FOUND)

# Add project subdirectories
add_subdirectory(swmm-solver)

add_subdirectory(src/swmm/toolkit)
