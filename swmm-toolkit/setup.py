# -*- coding: utf-8 -*-

#
# setup.py - Setup script for swmm-toolkit python package
#
# Created:    7/2/2018
# Modified:   2/21/2020
#
# Author:     Michael E. Tryby
#             US EPA - ORD/NRMRL
#
# Usage:
#   python setup.py build -- -G"Visual Studio 15 2017 Win64" ..
#


from skbuild import setup


setup(
    name = 'swmm-toolkit',
    version = '0.4.0',

    cmake_args = ['-GVisual Studio 14 2015 Win64'],

    package_dir={'': 'src'},
    packages=['swmm.toolkit'],

    package_data = {
        'swmm.toolkit':['*solver*','*output*', '*.dylib', '*.dll', '*.so'],
    },

    zip_safe=False
)
