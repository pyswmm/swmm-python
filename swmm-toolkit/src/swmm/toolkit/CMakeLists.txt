#
# CMakeLists.txt - CMake configuration file for swmm.toolkit python package
#
# Created:   Feb 6, 2020
# Modified:  Apr 3, 2020
#
# Author: Michael E. Tryby
#         US EPA ORD/CESER
#


set(CMAKE_SWIG_FLAGS -py3)


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
        $<$<BOOL:APPLE>:-undefineddynamic_lookup>
)

target_link_libraries(output
    PUBLIC
        Python::Module
        swmm-output
)

set_target_properties(output
    PROPERTIES
        SWIG_COMPILE_DEFINITIONS EXPORT_OUT_API
        MACOSX_RPATH TRUE
        SKIP_BUILD_RPATH FALSE
        BUILD_WITH_INSTALL_RPATH FALSE
        INSTALL_RPATH "@loader_path/../../../.."
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

install(
    TARGETS
        swmm-output LIBRARY
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
        $<$<BOOL:APPLE>:-undefineddynamic_lookup>
)

target_link_libraries(solver
    PUBLIC
        Python::Module
        swmm5
)

set_target_properties(solver
    PROPERTIES
        SWIG_COMPILE_DEFINITIONS EXPORT_OUT_API
        MACOSX_RPATH TRUE
        SKIP_BUILD_RPATH FALSE
        BUILD_WITH_INSTALL_RPATH FALSE
        INSTALL_RPATH "@loader_path/../../../.."
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

install(
    TARGETS
        swmm5 LIBRARY
    DESTINATION
        "src/swmm/toolkit"
)


set(CMAKE_INSTALL_SYSTEM_RUNTIME_DESTINATION "src/swmm/toolkit")
set(CMAKE_INSTALL_OPENMP_LIBRARIES TRUE)
include(InstallRequiredSystemLibraries)
