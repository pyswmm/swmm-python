# -*- coding: utf-8 -*-

#
#  __init__.py - SWMM toolkit package
#
#  Created:    Aug 9, 2018
#  Updated:    May 20, 2020
#
#  Author:     Michael E. Tryby
#              US EPA - ORD/NRMRL
#

'''
A low level pythonic API for the swmm-output and swmm-output dlls using SWIG.
'''


__author__ = "Michael Tryby"
__copyright__ = "None"
__credits__ = "Colleen Barr, Sam Hatchett"
__license__ = "CC0 1.0 Universal"

__version__ = "0.5.0"
__date__ = "May 20, 2020"

__maintainer__ = "Michael Tryby"
__email__ = "tryby.michael@epa.gov"
__status__  = "Development"


import os
import platform


# Adds directory containing swmm libraries to path
if platform.system() == "Windows":
    libdir = os.path.join(os.path.dirname(__file__), "../../../../bin")

    if hasattr(os, 'add_dll_directory'):
        os.add_dll_directory(libdir)
    else:
        os.environ["PATH"] = libdir + ";" + os.environ["PATH"]
