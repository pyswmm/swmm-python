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

SWIG_ADD_LIBRARY(output
    TYPE
        SHARED
    LANGUAGE
        python
    SOURCES
        output.i
    )

set_property(TARGET output
    PROPERTY
        SWIG_COMPILE_DEFINITIONS EXPORT_OUT_API
    )

target_link_libraries(output
    PUBLIC
        Python::Python
        swmm-output
    )

install(
    FILES
        "__init__.py"
        "output_enum.py"
        "output_metadata.py"
        "$<TARGET_FILE:output>"
        "${CMAKE_CURRENT_BINARY_DIR}/output.py"
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

SWIG_ADD_LIBRARY(solver
    LANGUAGE
        python
    SOURCES
        solver.i
    )

target_link_libraries(solver
    PUBLIC
        Python::Python
        swmm5
    )

install(
    FILES
        "$<TARGET_FILE:solver>"
        "${CMAKE_CURRENT_BINARY_DIR}/solver.py"
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
