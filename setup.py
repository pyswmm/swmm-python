# -*- coding: utf-8 -*-
#
# setup.py - Setup script for swmm_toolkit python extension
# 
# Created:    7/2/2018
# Author:     Michael E. Tryby
#             US EPA - ORD/NRMRL
# Modified by: Bryant E. McDonnell (EmNet)
#
# Requires:
#   Platform C language compiler   
#   SWIG
#

import os
import sys

try:
    from setuptools import setup, Extension, find_packages
    from setuptools.command.build_ext import build_ext
except ImportError:
    from distutils.core import setup, Extension
    from distutils.command.build_ext import build_ext

toolkit_ext = Extension("swmm._toolkit",
            include_dirs = ['swmm/'],           
            libraries = ['swmm5'],
            library_dirs = ['swmm/'],      
            sources = ['swmm/toolkit.i'],
            swig_opts = ['-py3'],
            language = 'C'
            )

package_data = {}
if os.name == 'nt': # Windows
    #if sys.platform == 'win32': # <- python build
    package_data = {'swmm':['swmm5.dll']}
    package_data['swmm'].append('vcomp120.dll')      

setup(
    name = "swmm-python", 
    version = "0.2.0.dev0",
    ext_modules = [toolkit_ext],

    packages = ['swmm'],
    package_data = package_data,
    exclude_package_data = {'swmm':['toolkit.i']},

    include_package_data = False, 
    zip_safe = False, 

    install_requires = ['enum34']
)
