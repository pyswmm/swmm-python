#
# CMakeLists.txt - CMake configuration file for swmm.toolkit python package
#
# Created:   Feb 6, 2020
# Modified:  Apr 17, 2020
#
# Author: Michael E. Tryby
#         US EPA ORD/CESER
#


set(CMAKE_SWIG_FLAGS -py3)

# Determine filename suffix for python extension
if(WIN32)
    set(Python_EXTENSION ".${Python_SOABI}.pyd")
else()
    set(Python_EXTENSION ".${Python_SOABI}.so")
endif()


# Location of package at runtime on Linux/MacOS
if(APPLE)
    set(PACKAGE_RPATH "@loader_path/../../../..")
else()
    set(PACKAGE_RPATH "$ORIGIN/../../../..")
endif()


#######   OUTPUT TARGET   #######

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

target_link_libraries(output
    PUBLIC
        Python::Module
        swmm-output
)

set_target_properties(output
    PROPERTIES
        SUFFIX ${Python_EXTENSION}
        SWIG_COMPILE_DEFINITIONS EXPORT_OUT_API
        MACOSX_RPATH TRUE
        SKIP_BUILD_RPATH FALSE
        BUILD_WITH_INSTALL_RPATH FALSE
        INSTALL_RPATH ${PACKAGE_RPATH}
        INSTALL_RPATH_USE_LINK_PATH TRUE
)

install(
    FILES
        "__init__.py"
        "output_enum.py"
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


#######   SOLVER TARGET   #######

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

target_link_libraries(solver
    PUBLIC
        Python::Module
        swmm5
)

set_target_properties(solver
    PROPERTIES
        SUFFIX ${Python_EXTENSION}
        MACOSX_RPATH TRUE
        SKIP_BUILD_RPATH FALSE
        BUILD_WITH_INSTALL_RPATH FALSE
        INSTALL_RPATH ${PACKAGE_RPATH}
        INSTALL_RPATH_USE_LINK_PATH TRUE
)

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/solver.py"
    DESTINATION
        "src/swmm/toolkit"
)

install(
    TARGETS
        solver
    DESTINATION
        "src/swmm/toolkit"
)


set(CMAKE_INSTALL_SYSTEM_RUNTIME_DESTINATION "src/swmm/toolkit")
set(CMAKE_INSTALL_OPENMP_LIBRARIES TRUE)
include(InstallRequiredSystemLibraries)
