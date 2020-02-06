# -*- coding: utf-8 -*-

#
# setup.py - Setup script for swmm-toolkit python package
#
# Created:    7/2/2018
# Modified:   2/6/2020
#
# Author:     Michael E. Tryby
#             US EPA - ORD/NRMRL
#


from skbuild import setup


setup(
    name = 'swmm-toolkit',
    version = '0.4.0',

    package_dir={"":"swmm"},
    packages=['swmm.solver', 'swmm.output'],
    py_modules = ['solver', 'output'],

    package_data = {'swmm.solver':['*solver.*', '*.dylib', '*.dll', '*.so'],
                    'swmm.output':['*output.*', '*.dylib', '*.dll', '*.so']},

    zip_safe=False
)
