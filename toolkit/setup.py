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
    name = 'swmm_toolkit', 
    version = '0.0.1',

    ext_modules = [
        Extension('swmm/toolkit/_toolkit',
            include_dirs = ['swmm/toolkit/'],           
            libraries = ['swmm5'],
            library_dirs = ['swmm/toolkit/'],      
            sources = ['swmm/toolkit/toolkit.i'],
            swig_opts=['-py3'],
            language = 'C'
        )
    ],
    packages=['swmm.toolkit'],
#    package_dir = {'':'swmm'},  
    py_modules = ['toolkit'],
    package_data = {'swmm.toolkit':['libswmm5.so']},
#    exclude_package_data = {'swmm':['toolkit.i']},
     
    install_requires = [
        'enum34'
    ]
)
