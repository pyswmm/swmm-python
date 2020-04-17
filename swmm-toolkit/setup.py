#
# setup.py - Setup script for swmm-toolkit python package
#
# Created:    7/2/2018
# Modified:   4/17/2020
#
# Author:     Michael E. Tryby
#             US EPA - ORD/NRMRL
#
# Suggested Usage:
#   python setup.py build
#   python setup.py bdist_wheel
#

import platform

from skbuild import setup


# Determine platform
platform_system = platform.system()


# Set Platform specific cmake args here
if platform_system == "Windows":
    cmake_args = ["-GVisual Studio 14 2015 Win64"]

elif platform_system == "Darwin":
    cmake_args = ["-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.10"] #python v3.7

else:
    cmake_args = ["-GNinja"]


setup(
    name = "swmm-toolkit",
    version = "0.4.0",

    cmake_args = cmake_args,

    package_dir = {"": "src"},
    packages = ["swmm.toolkit"],

    include_package_data = True,

    zip_safe = False,

    install_requires = [
        "aenum"
    ]
)
