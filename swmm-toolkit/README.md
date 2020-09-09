# swmm-toolkit

`swmm-toolkit` contains SWIG generated Python wrappers for the swmm-solver and swmm-output libraries. 


## Features

`swmm-toolkit` makes SWMM a fully fledged Python extension with:  

 - Python integration at the speed of C
 - Full access to library APIs
 - Pythonic naming, enums, exceptions, and return value handling 


## Installation


## Build 
1. Initialize submodule
```cmd
git submodule init
git submodule update 
```
2. Create virtual environment
3. `pip install` from requirements.txt
4. `python setup.py build`
 
## Troubleshoot

Steps to try if `python setup.py build` fails 

### Establish working swmm-solver build
1. Create an environment variable `BOOST_ROOT_1_67_0` and set the variable to boost install location
2. Confirm swmm-solver directory is initialized
3. Confirm swmm-solver build is working 

```
cd swmm-solver 
mkdir buildprod
cd buildprod
cmake -G "Visual Studio 14 2015 Win64" ..
cmake --build . --config Release --target install 
```

## Basic Usage

Run a SWMM simulation. 
```
from swmm.toolkit import solver

solver.run('input_file.inp', 'report_file.rpt', 'output_file.out')
```
