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

try:
    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext
except ImportError:
    from distutils.core import setup, Extension
    from distutils.command.build_ext import build_ext


microlib_name = 'swmm.toolkit'

setup(
    name = microlib_name,
    version = '0.2.0-dev',

    ext_modules = [
        Extension('swmm.toolkit._toolkit',
            sources = ['swmm/toolkit/toolkit.i'],
            swig_opts=['-py3'],
            include_dirs = ['swmm/toolkit/'],
            library_dirs = ['swmm/toolkit/'],
            libraries = ['swmm5'],
            extra_compile_args = ["/D WITH_GENX"],
            language = 'C'
        )
    ],
    namespace_packages=['swmm'],
    packages=[microlib_name],
    py_modules = ['toolkit'],
    package_data = {microlib_name:['*swmm5.dll', '*swmm5.so']},
)
