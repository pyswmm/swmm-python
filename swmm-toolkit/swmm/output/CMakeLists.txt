#
# CMakeLists.txt - CMake configuration file for swmm.output python package
#
# Created:   Feb 6, 2020
# Modified:
#
# Author: Michael E. Tryby
#         US EPA ORD/CESER
#


set_property(SOURCE output.i
    PROPERTY
        USE_TARGET_INCLUDE_DIRECTORIES ON
    )

SWIG_ADD_LIBRARY(output
    LANGUAGE
        python
    SOURCES
        output.i
    )

target_link_libraries(output
    PUBLIC
        Python::Python
        swmm-output
    )

install(
    FILES
        "$<TARGET_FILE:output>"
        "${CMAKE_CURRENT_BINARY_DIR}/output.py"
    DESTINATION
        "swmm/output"
)

install(
    TARGETS
        swmm-output RUNTIME
    DESTINATION
        "swmm/output"
)


set(CMAKE_INSTALL_SYSTEM_RUNTIME_DESTINATION "swmm/output")
include(InstallRequiredSystemLibraries)
