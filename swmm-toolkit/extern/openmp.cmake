#
# CMakeLists.txt - CMake configuration file for OpenMP Library on Darwin
#
# Created: Mar 17, 2021
# Updated: Aug 29, 2025
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


# Append local dir to module search path
list(
    APPEND CMAKE_MODULE_PATH
        ${CMAKE_BINARY_DIR}/_deps/llvm_cmake-src/Modules
)

include(
    FetchContent
)


# v17.0.1 (v17.0.0 was yanked)
FetchContent_Declare(
  llvm_cmake
    URL
        https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.1/cmake-17.0.1.src.tar.xz
    URL_HASH
        SHA256=46e745d9bdcd2e18719a47b080e65fd476e1f6c4bbaa5947e4dee057458b78bc
)

FetchContent_Declare(
  OpenMP
    URL
        https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.1/openmp-17.0.1.src.tar.xz
    URL_HASH
        SHA256=d4a25c04d1bc035990a85f172bfe29a38f21ff87448f7fbae165fa780cb95717
    OVERRIDE_FIND_PACKAGE
)

set(
    OPENMP_STANDALONE_BUILD
        TRUE
)
set(
    LIBOMP_INSTALL_ALIASES
        OFF
)

FetchContent_MakeAvailable(
    llvm_cmake
    OpenMP
)

target_compile_options(
  omp
    INTERFACE
        -Xclang
        -fopenmp
)

target_link_directories(
  omp
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_BINARY_DIR}/_deps/openmp-build/runtime/src>
        $<INSTALL_INTERFACE:/include>
)

add_library(
  OpenMP::OpenMP_C
    ALIAS
        omp
)
