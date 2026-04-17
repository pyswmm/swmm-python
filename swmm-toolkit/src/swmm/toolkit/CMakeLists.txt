#
# CMakeLists.txt - CMake configuration file for swmm.toolkit python package
#
# Created:   Feb 6, 2020
# Updated:   Sep 2, 2025
#
#  Author:   See AUTHORS
#

################################################################################
#################    CMAKELISTS FOR SWMM-TOOLKIT EXT BUILD    ##################
################################################################################


# set(CMAKE_SWIG_FLAGS -py3)

# Determine filename suffix for python extension
if(WIN32)
    set(SOABI "")
    set(LIB_EXT "pyd")
else()
    set(SOABI ".abi3")
    set(LIB_EXT "so")
endif()

# turn off stable ABI if NO_STABLE_ABI is 1 or true
set(PY_LIMITED_API_DEF "Py_LIMITED_API=0x03090000")
string(TOLOWER "$ENV{NO_STABLE_ABI}" _abi_val)
if(_abi_val STREQUAL "1" OR _abi_val STREQUAL "true")
    set(PY_LIMITED_API_DEF "")
    if(NOT Python3_SOABI)
        execute_process(
            COMMAND ${Python3_EXECUTABLE} -c
                "import sysconfig; print(sysconfig.get_config_var('SOABI') or '')"
            OUTPUT_VARIABLE Python3_SOABI
            OUTPUT_STRIP_TRAILING_WHITESPACE
        )
    endif()
    set(SOABI ".${Python3_SOABI}")
endif()

set(PYTHON_SUFFIX "${SOABI}.${LIB_EXT}")

# Location of package at runtime on MacOS/Linux
if(APPLE)
    set(LIB_ROOT "@loader_path")
else()
    set(LIB_ROOT "$ORIGIN")
endif()

# For scikit-build-core, use SKBUILD_PLATLIB_DIR instead of hardcoded paths
if(DEFINED SKBUILD_PLATLIB_DIR)
    # scikit-build-core is being used
    set(PYTHON_INSTALL_DIR "${SKBUILD_PLATLIB_DIR}/swmm/toolkit")
else()
    # Fallback for direct CMake builds or legacy scikit-build
    set(PYTHON_INSTALL_DIR "src/swmm/toolkit")
endif()


if(WIN32)
    # Explicitly add the Python libs directory to the linker search path for windows
    # Not sure why I need to do this for windows only, but it got the stable ABI to build
    link_directories(${Python3_LIBRARY_DIRS})
endif()

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
        ${Python3_INCLUDE_DIRS}
)

target_link_libraries(output
    PUBLIC
        swmm-output
)

set_target_properties(output
    PROPERTIES
        SUFFIX ${PYTHON_SUFFIX}
        SWIG_COMPILE_DEFINITIONS EXPORT_OUT_API=
        MACOSX_RPATH TRUE
        SKIP_BUILD_RPATH FALSE
        BUILD_WITH_INSTALL_RPATH FALSE
        INSTALL_RPATH ${LIB_ROOT}
        INSTALL_RPATH_USE_LINK_PATH TRUE
        COMPILE_DEFINITIONS "${PY_LIMITED_API_DEF}"
)

install(
    FILES
        "__init__.py"
        "shared_enum.py"
        "output_metadata.py"
        "${CMAKE_CURRENT_BINARY_DIR}/output.py"
    DESTINATION
        "${PYTHON_INSTALL_DIR}"
    COMPONENT python
)

install(
    TARGETS
        output
        swmm-output
    DESTINATION
        "${PYTHON_INSTALL_DIR}"
    COMPONENT python
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
        ${Python3_INCLUDE_DIRS}
)

target_link_libraries(solver
    PUBLIC
        swmm5
)

set_target_properties(solver
    PROPERTIES
        SUFFIX ${PYTHON_SUFFIX}
        SWIG_COMPILE_DEFINITIONS EXPORT_TOOLKIT=
        MACOSX_RPATH TRUE
        SKIP_BUILD_RPATH FALSE
        BUILD_WITH_INSTALL_RPATH FALSE
        INSTALL_RPATH ${LIB_ROOT}
        INSTALL_RPATH_USE_LINK_PATH TRUE
        COMPILE_DEFINITIONS "${PY_LIMITED_API_DEF}"
)

# Stages python module for package build
install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/solver.py"
    DESTINATION
        "${PYTHON_INSTALL_DIR}"
    COMPONENT python
)

# Stages extension library for package build
install(
    TARGETS
        solver
        swmm5
    DESTINATION
        "${PYTHON_INSTALL_DIR}"
    COMPONENT python
)

#############################################################
####################    SUFFIX TESTS     ####################
#############################################################

# Verify that each extension module was linked with a valid Python ABI suffix.
# Guards against the double-dot bug (_solver..so) that occurs when
# CMake's FindPython3 fails to populate Python3_SOABI.
# Run with: cmake --build <build_dir> && ctest --test-dir <build_dir>

foreach(_ext_target output solver)
    add_test(
        NAME ExtensionSuffix_${_ext_target}
        COMMAND ${Python3_EXECUTABLE} -c
            "import importlib.machinery, os; \
p = r'$<TARGET_FILE:${_ext_target}>'; \
valid = importlib.machinery.EXTENSION_SUFFIXES; \
assert os.path.exists(p), f'Extension not found: {p!r}'; \
assert '..' not in os.path.basename(p), \
    f'Double-dot ABI bug in {p!r} -- Python3_SOABI was empty at configure time'; \
assert any(p.endswith(s) for s in valid), \
    f'Invalid suffix in {p!r}, expected one of {valid}'; \
print('PASS:', p)"
    )
endforeach()

# Copy libomp.dylib on macOS if using scikit-build-core
if(APPLE AND DEFINED SKBUILD_PLATLIB_DIR)
    install(
        FILES
            "${SKBUILD_PLATLIB_DIR}/lib/libomp.dylib"
        DESTINATION
            "${PYTHON_INSTALL_DIR}"
        COMPONENT python
        OPTIONAL
    )
# Copy copy dlls from build dir to python install dir
elseif(WIN32 AND DEFINED SKBUILD_PLATLIB_DIR)
    install(
        DIRECTORY "${SKBUILD_PLATLIB_DIR}/bin/"
        DESTINATION "${PYTHON_INSTALL_DIR}"
        COMPONENT python
        FILES_MATCHING PATTERN "*.dll"
    )
endif()

