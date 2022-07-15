# swmm-toolkit

`swmm-toolkit` contains SWIG generated Python wrappers for the swmm-solver and swmm-output libraries. 


## Build Status

![Build Wheels](https://github.com/SWMM-Project/swmm-python/workflows/Build%20Wheels/badge.svg)


## Installation

[![version](https://img.shields.io/pypi/v/swmm-toolkit.svg?maxAge=3600)](https://pypi.org/project/swmm-toolkit/) [![Downloads](https://pepy.tech/badge/swmm-toolkit)](https://pepy.tech/project/swmm-toolkit)

  ``pip install swmm-toolkit``


## Features

`swmm-toolkit` makes SWMM a fully fledged Python extension with:  
 - Compatibility with USEPA SWMM
 - Python integration at the speed of C
 - Full access to library APIs
 - Pythonic naming, enums, exceptions, and return value handling 
 
 
## Basic Usage

Run a SWMM simulation. 
```
from swmm.toolkit import solver

solver.run('input_file.inp', 'report_file.rpt', 'output_file.out')
```
