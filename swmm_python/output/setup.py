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
            ['swmm/output/output.i'],
            include_dirs = ['swmm/output/'],
            libraries = ['swmm-output'],
            library_dirs = ['swmm/output/'],
            swig_opts=['-py3'],
            language='C'
        )
    ],
    py_modules = ['output'],
    namespace_packages=['swmm'],
#    packages = [microlib_name],
#    package_data = {microlib_name:['./*swmm-output.dll', './*swmm-output.so']},

    install_requires = [
        'aenum'
    ]
)
