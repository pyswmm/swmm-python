# swmm-toolkit

`swmm-toolkit` contains SWIG generated Python wrappers for the swmm-solver and swmm-output libraries. 


## Build Status

[![Build Wheels](https://github.com/pyswmm/swmm-python/actions/workflows/build_wheel.yml/badge.svg)](https://github.com/pyswmm/swmm-python/actions/workflows/build_wheel.yml)


## Installation

[![version](https://img.shields.io/pypi/v/swmm-toolkit.svg?maxAge=3600)](https://pypi.org/project/swmm-toolkit/) [![Downloads](https://pepy.tech/badge/swmm-toolkit)](https://pepy.tech/project/swmm-toolkit)

  ``pip install swmm-toolkit``

## Community

[![Discord](https://img.shields.io/badge/Discord-Join%20Chat-7289da?logo=discord&logoColor=white)](https://discord.com/channels/1412143058463756421/1412144907312955532)

Join the discussion!  We will do everything we can to help you!

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
