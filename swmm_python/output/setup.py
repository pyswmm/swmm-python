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


from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext


setup(
    name = 'swmm_output',
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
    packages = ['swmm.output'],
    package_data = {'swmm.output':['./*swmm-output.dll', './*swmm-output.so']},

    install_requires = [
        'aenum'
    ]
)
