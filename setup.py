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
    from setuptools import setup, Extension, find_packages
    from setuptools.command.build_ext import build_ext
except ImportError:
    from distutils.core import setup, Extension
    from distutils.command.build_ext import build_ext

toolkit_ext = Extension("toolkit.lib._toolkit",
            include_dirs = ['toolkit/include/'],           
            libraries = ['swmm5'],
            library_dirs = ['toolkit/lib/'],      
            sources = ['toolkit/toolkit.i'],
            swig_opts = ['-py3'],
            language = 'C'
            )

setup(
    name = "swmm-python", 
    version = "0.0.1",
    ext_modules = [toolkit_ext],

    packages = ['toolkit'],
 #   package_dir = {'toolkit':'toolkit'},
#    py_modules = ['toolkit.toolkit'],
    package_data = {'toolkit':['lib/swmm5.dll']},
    exclude_package_data = {'toolkit':['toolkit.i']},

    include_package_data = True, 
    zip_safe = False, 

    install_requires = ['enum34']
)
