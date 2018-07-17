# swmm-python

## Build Notes 

Hints for building SWIG wrapper for SWMM Toolkit on Windows. This package
is currently under active development. The build process is likely to change. 


### Dependencies
- Python 3.6.5 64 bit 
- Visual Studio 14 2015
- CMake
- SWIG


### Build Process
The idea here is to build the SWMM library seperately link it with the SWIG 
wrapper. This approach uses implicit linking, therefore, an import library 
must be created. CMake does this automatically using the Generate Export Header 
function. Once built the SWMM library and headers are manually copied to the 
swmm-toolkit directory. To run, the resulting swmm-toolkit.pyd needs the 
swmm5.dll.   


Step 1 - Build SWMM Library

Build the SWMM Library using CMake generator "Visual Studio 14 2015 Win64"
Be sure "generate export header" section of the SWMM Project CMakeLists.txt 
is not commented out. 


Step 2 - Copy SWMM Library

In the swmm-toolkit directory create two directories include and lib. Copy 
swmm5.h and toolkitAPI.h to include. And copy swmm5.dll, swmm5.lib and 
swmm5.exp to lib. These are the locations defined in the setup.py file. 


Step 3 - Build SWMM Toolkit

Execute the command `python setup.py build` 


Step 4 - Running SWMM Toolkit

Install the pyd and the dll in the same directory and add the directory to 
the python path. 


#### Common Problems
When I used the Developer Command Prompt for Visual Studio 2015 the build 
fails with linking errors. Use a regular Command Prompt to build. 
