# -*- coding: utf-8 -*-

#
# setup.py - Setup script for swmm_toolkit python extension
#
# Created:    7/2/2018
# Author:     Michael E. Tryby
#             US EPA - ORD/NRMRL
#
# Requires:
#   Platform C language compiler
#   SWIG
#


from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


setup(
    name = 'swmm.toolkit',
    version = '0.2.0.dev0',

    ext_modules = [
        Extension('swmm.toolkit._toolkit',
            sources = ['swmm/toolkit/toolkit_wrap.c'],
            include_dirs = ['swmm/toolkit/'],
            library_dirs = ['swmm/toolkit/'],
            libraries = ['swmm5'],
            extra_compile_args = ["/D WITH_GENX"],
            language = 'C'
        )
    ],
    py_modules = ['toolkit'],

    packages=['swmm.toolkit'],
    package_data = {'swmm.toolkit':['*swmm5.dll', '*swmm5.so']},

    zip_safe=False
)
