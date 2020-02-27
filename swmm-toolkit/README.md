# swmm-toolkit

`swmm-toolkit` contains SWIG generated Python wrappers for the swmm-solver and swmm-output libraries. 


## Features

`swmm-toolkit` makes SWMM a fully fledged Python extension with:  

 - Python integration at the speed of C
 - full access to library APIs
 - Pythonic naming, enums, exceptions, and return value handling 


## Installation


## Basic Usage

Run a SWMM simulation. 
```
from swmm.toolkit import solver

solver.run('input_file.inp', 'report_file.rpt', 'output_file.out')
```
