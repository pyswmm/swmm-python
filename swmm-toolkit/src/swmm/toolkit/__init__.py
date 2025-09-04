# -*- coding: utf-8 -*-

#
#  __init__.py - SWMM toolkit package
#
#  Created:    Aug 9, 2018
#  Updated:    September 4, 2025
#
#  Author:     See AUTHORS
#

"""
A low level pythonic API for the swmm-output and swmm-solver dlls using SWIG.
"""


__author__ = "See AUTHORS"
__credits__ = "Colleen Barr"
__license__ = "CC0 1.0 Universal"

__version__ = "0.16.0"
__date__ = "September 4, 2025"

__maintainer__ = "Michael Tryby"
__email__ = "michael.tryby@gmail.com"
__status__  = "Production/Stable"


import os
import platform
import sys


# Adds directory containing swmm libraries to path
if platform.system() == "Windows":
    libdir = os.path.join(os.path.dirname(__file__), "../../swmm_toolkit")

    if hasattr(os, 'add_dll_directory'):
        conda_exists = os.path.exists(os.path.join(sys.prefix, 'conda-meta'))
        if conda_exists:
            os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = "1"
        os.add_dll_directory(libdir)
    else:
        os.environ["PATH"] = libdir + ";" + os.environ["PATH"]
