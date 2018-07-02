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

setup(
    name = "swmm-toolkit", 
    version = "0.0.1",
    ext_modules = [
        Extension("_swmm_toolkit",
            include_dirs = ['include/'],           
            libraries = ['swmm5'],
            library_dirs = ['lib/'],      
            sources = ['src/swmm_toolkit.i'],
            swig_opts=['-py3'],
            language = 'C'
        )
    ],
    package_dir = {'':'src'},  
    py_modules = ['swmm_toolkit'],
      
    install_requires = [
        'enum34'
    ]

)
