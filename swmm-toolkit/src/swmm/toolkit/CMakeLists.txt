#
# CMakeLists.txt - CMake configuration file for swmm.toolkit python package
#
# Created:   Feb 6, 2020
# Updated:   Dec 29, 2020
#
#  Author:   See AUTHORS
#


set(CMAKE_SWIG_FLAGS -py3)

# Determine filename suffix for python extension
if(WIN32)
    set(LIB_EXT "pyd")
else()
    set(LIB_EXT "so")
endif()

set(Python_EXTENSION ".${Python_SOABI}.${LIB_EXT}")


# Location of package at runtime on MacOS/Linux
if(APPLE)
    set(LIB_ROOT "@loader_path")
else()
    set(LIB_ROOT "$ORIGIN")
endif()

# Inserting line continuation '\' in this long path string breaks wheel repair
set(PACKAGE_RPATH 
    "${LIB_ROOT}/../../../..;${LIB_ROOT}/../../../../extern;${LIB_ROOT}/../../../lib;${LIB_ROOT}/../../swmm_toolkit-${CMAKE_PROJECT_VERSION}.data/data/lib"
)


#############################################################
####################    OUTPUT TARGET    ####################
#############################################################

set_property(SOURCE output.i
    PROPERTY
        USE_TARGET_INCLUDE_DIRECTORIES ON
)

swig_add_library(output
    TYPE
        MODULE
    LANGUAGE
        python
    SOURCES
        output.i
)

target_link_options(output
    PUBLIC
        $<$<BOOL:${APPLE}>:-undefineddynamic_lookup>
)

target_include_directories(output
    PUBLIC
        ${Python_INCLUDE_DIRS}
)

target_link_libraries(output
    PUBLIC
        $<$<BOOL:$<C_COMPILER_ID:MSVC>>:Python::Module>
        swmm-output
)

set_target_properties(output
    PROPERTIES
        SUFFIX ${Python_EXTENSION}
        SWIG_COMPILE_DEFINITIONS EXPORT_OUT_API
        MACOSX_RPATH TRUE
        SKIP_BUILD_RPATH FALSE
        BUILD_WITH_INSTALL_RPATH FALSE
        INSTALL_RPATH "${PACKAGE_RPATH}"
        INSTALL_RPATH_USE_LINK_PATH TRUE
)

install(
    FILES
        "__init__.py"
        "shared_enum.py"
        "output_metadata.py"
        "${CMAKE_CURRENT_BINARY_DIR}/output.py"
    DESTINATION
        "src/swmm/toolkit"
)

install(
    TARGETS
        output
    DESTINATION
        "src/swmm/toolkit"
)

#############################################################
####################    SOLVER TARGET    ####################
#############################################################

set_property(SOURCE solver.i
    PROPERTY
        USE_TARGET_INCLUDE_DIRECTORIES ON
)

swig_add_library(solver
    TYPE
        MODULE
    LANGUAGE
        python
    SOURCES
        solver.i
)

target_link_options(solver
    PUBLIC
        $<$<BOOL:${APPLE}>:-undefineddynamic_lookup>
)

target_include_directories(solver
    PUBLIC
        ${Python_INCLUDE_DIRS}
)

target_link_libraries(solver
    PUBLIC
        $<$<BOOL:$<C_COMPILER_ID:MSVC>>:Python::Module>
        swmm5
)

set_target_properties(solver
    PROPERTIES
        SUFFIX ${Python_EXTENSION}
        MACOSX_RPATH TRUE
        SKIP_BUILD_RPATH FALSE
        BUILD_WITH_INSTALL_RPATH FALSE
        INSTALL_RPATH "${PACKAGE_RPATH}"
        INSTALL_RPATH_USE_LINK_PATH TRUE
)


# Stages extension module for package build
install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/solver.py"
    DESTINATION
        "src/swmm/toolkit"
)


# Stages extension library for package build
install(
    TARGETS
        solver
    DESTINATION
        "src/swmm/toolkit"
)
