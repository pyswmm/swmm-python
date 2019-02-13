# -*- coding: utf-8 -*-

#
# setup.py - Setup script for swmm_output python extension
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


microlib_name = 'swmm.output'

setup(
    name = microlib_name,
    version = "0.3.0-dev",

    ext_modules = [
        Extension("swmm.output._output",
            include_dirs = ['swmm/output/'],
            libraries = ['swmm-output'],
            library_dirs = ['swmm/output/'],
            sources = ['swmm/output/output.i'],
            swig_opts=['-py3'],
            language='C'
        )
    ],
    namespace_packages=['swmm'],
    packages = [microlib_name],
    py_modules = ['output'],
    package_data = {microlib_name:['*swmm-output.dll', '*swmm-output.so', 'output.py']},

    install_requires = [
        'aenum'
    ]
)
