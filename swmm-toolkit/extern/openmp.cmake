#
# CMakeLists.txt - CMake configuration file for OpenMP Library on Darwin
#
# Created: Mar 17, 2021
# Updated: May 19, 2021
#
# Author: Michael E. Tryby
#         US EPA ORD/CESER
#
# Note:
#  Need to build libomp for binary compatibility with Python.
#
#  OpenMP library build fails for Xcode generator. Use Ninja or Unix Makefiles
#  instead.
#
# All sources were obtained directly from the LLVM releases on github
# See license-llvm-openmp.txt for the corresponding license and 
# https://openmp.llvm.org/ for details on the OpenMP run-time. 

################################################################################
#####################    CMAKELISTS FOR OPENMP LIBRARY    ######################
################################################################################

include(FetchContent)


FetchContent_Declare(OpenMP
    URL
        https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.1/openmp-12.0.1.src.tar.xz
    URL_HASH
        SHA256=60fe79440eaa9ebf583a6ea7f81501310388c02754dbe7dc210776014d06b091
)

set(OPENMP_STANDALONE_BUILD TRUE)
set(LIBOMP_INSTALL_ALIASES OFF)

FetchContent_MakeAvailable(OpenMP)
set(OpenMP_AVAILABLE TRUE)


target_link_directories(omp
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_BINARY_DIR}/_deps/openmp-build/runtime/src>
        $<INSTALL_INTERFACE:${LIBRARY_DIST}>
)

install(TARGETS omp
    LIBRARY
    DESTINATION
        "${LIBRARY_DIST}"
)

if(CMAKE_C_COMPILER_ID MATCHES "Clang\$")
    set(OpenMP_C_FLAGS "-Xpreprocessor -fopenmp -I${CMAKE_BINARY_DIR}/_deps/openmp-build/runtime/src")
    set(OpenMP_C_LIB_NAMES "omp")
    set(OpenMP_omp_LIBRARY "${CMAKE_BINARY_DIR}/_deps/openmp-build/runtime/src/libomp.dylib")
endif()

if(CMAKE_CXX_COMPILER_ID MATCHES "Clang\$")
    set(OpenMP_CXX_FLAGS "-Xpreprocessor -fopenmp -I${CMAKE_BINARY_DIR}/_deps/openmp-build/runtime/src")
    set(OpenMP_CXX_LIB_NAMES "omp")
    set(OpenMP_omp_LIBRARY "${CMAKE_BINARY_DIR}/_deps/openmp-build/runtime/src/libomp.dylib")
endif()