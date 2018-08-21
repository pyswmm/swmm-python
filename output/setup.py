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


setup(
    name = "swmm-output",
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
    packages = ['swmm.output'],  
    py_modules = ['output'],
    package_data = {'swmm.output':['*swmm-output.dll', '*swmm-output.so']},
    
    install_requires = [
        'aenum'
    ]
)
