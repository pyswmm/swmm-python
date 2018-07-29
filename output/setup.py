# -*- coding: utf-8 -*-

#
#  setup.py 
# 
#  Author:     Michael E. Tryby
#              US EPA - ORD/NRMRL
#
#

'''Setup up script for SWMM Output API python extension'''

try:
    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext
except ImportError:
    from distutils.core import setup, Extension
    from distutils.command.build_ext import build_ext


setup(
    name = "swmm-output",
    version = "0.1.0-alpha",

    ext_modules = [
        Extension("swmm/output/_output", 
            include_dirs = ['swmm/output/'],
            libraries = ['swmm-output'],
            library_dirs = ['swmm/output/']
            sources = ['swmm/output/output.i'],
            swig_opts=['-py3'],
            language='C'
        )
    ],
    packages = ['swmm.output'],  
    py_modules = ['output'],
    package_data = {'swmm.output':['libswmm-output.so']},
  
    install_requires = [
        'enum34'
    ]
)
