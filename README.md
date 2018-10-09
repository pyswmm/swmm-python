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
The idea here is to build the SWMM library seperately and link it with the SWIG 
wrapper. This approach uses implicit linking, therefore, an import library 
must be created. CMake does this automatically using the Generate Export Header 
function. Once built the SWMM library and headers are manually copied to the 
swmm-toolkit directory. To run, the resulting swmm-toolkit.pyd needs the 
swmm5.dll.   


Step 1 - Build SWMM Library

Checkout the feature-reentrancy branch of the OWA SWMM project. Build the SWMM 
Library using CMake generator "Visual Studio 14 2015 Win64". Be sure "generate 
export header" section of the SWMM Project CMakeLists.txt is not commented out. 


Step 2 - Copy SWMM Library

In the swmm\toolkit directory copy swmm5.h and toolkitAPI.h, swmm5.dll, 
swmm5.lib, and swmm5.exp all together in the same folder. The setup.py file
is configured to find them there. 


Step 3 - Build SWMM Toolkit

Execute the command `python setup.py build` 


Step 4 - Running SWMM Toolkit

Install the pyd and the dll in the same directory and add the directory to 
the python path. 


#### Common Problems
When I used the Developer Command Prompt for Visual Studio 2015 the build 
fails with linking errors. Use a regular Command Prompt to build. 
