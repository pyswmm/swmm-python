# -*- coding: utf-8 -*-

#
# setup.py - Setup script for swmm-toolkit python package
#
# Created:    7/2/2018
# Modified:   4/3/2020
#
# Author:     Michael E. Tryby
#             US EPA - ORD/NRMRL
#
# Usage:
#   python setup.py build -- -G"Visual Studio 15 2017 Win64" ..
#

import platform

from skbuild import setup


# Determine platform
platform_system = platform.system()


# Set Platform specific cmake args here
if platform_system == "Windows":
    cmake_args = ["-GVisual Studio 14 2015 Win64"]

elif platform_system == "Darwin":
    cmake_args = ["-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.10"]

else:
    cmake_args = ["-GNinja"]


setup(
    name = "swmm-toolkit",
    version = "0.4.0",

    cmake_args=cmake_args,

    package_dir={"": "src"},
    packages=["swmm.toolkit"],

    include_package_data=True,

    zip_safe=False
)
