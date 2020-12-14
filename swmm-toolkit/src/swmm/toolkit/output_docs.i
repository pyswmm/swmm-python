/*
 *  output_docs.i - Documentation for swmm-output
 *
 *  Created:    12/10/2020
 *  
 *  Author:     See AUTHORS
 *
*/


%define OUTPUT_MODULE_DOCS
"Output Module
"
%enddef


%feature("autodoc", 
"Initialize pointer for output handle.

Returns
-------
p_handle: SMO_Handle *
    A SWMM output handle
"
) SMO_init;

%feature("autodoc",
"Open binary output file and reads prologue and epilogue.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
path: char const *
    the name of the binary output file to be opened.
"
) SMO_open;

%feature("autodoc",
"Close binary output file and perform cleanup. 

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
"
) SMO_close;

%feature("autodoc",
"Get the SWMM version that produced the binary output file. 

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle

Returns
-------
version: int *
    The SWMM version number found in the output file prologue.

"
) SMO_getVersion;

%feature("autodoc",
"Project element counts.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle

Returns
-------
elementCount:int **
    array of element count values
length:int *
    array size
"
) SMO_getProjectSize;


%feature("autodoc",
"Project unit flags for unit_system, flow, and pollutants.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle

Returns
-------
unitFlag: int **
    Array of unit flag values
length: int *
    Array length
"
) SMO_getUnits;

%feature("autodoc",
"Analysis start date.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle

Returns
-------
date: double *
    SWMM simulation start date (encoded)
"
) SMO_getStartDate;

%feature("autodoc",
"Analysis step size and number of periods.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
code: SMO_time
    A time parameter code (see :ref: SMO_Time)

Returns
-------
time: int *
    Time value
"
) SMO_getTimes;

%feature("autodoc",
"Given an element index returns the element name.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
type: SMO_elementType
    The type of the element being queried
elementIndex: int
    The index of the element being queried

Returns
-------
name: char **
    Element name array
length: int *
    Length of array
"
) SMO_getElementName;


%feature("autodoc",
"Get time series results for particular attribute. Specify series start and 
length using timeIndex and length respectively.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
subcatchIndex: int
attr: SMO_subcatchAttribute
startPeriod: int
endPeriod: int

Returns
-------
outValueArray: float **
    array of time series values
length: int *
    length of array
"
) SMO_getSubcatchSeries;

%feature("autodoc",
"Get time series results for particular attribute. Specify series start and 
length using timeIndex and length respectively.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
nodeIndex: int
attr: SMO_nodeAttribute
startPeriod: int
endPeriod: int

Returns
-------
outValueArray: float **
    array of time series values
length: int *
    length of array
"
) SMO_getNodeSeries;

%feature("autodoc",
"Get time series results for particular attribute. Specify series start and 
length using timeIndex and length respectively.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
linkIndex: int
attr: SMO_linkAttribute
startPeriod: int
endPeriod: int

Returns
-------
outValueArray: float **
    array of time series values
length: int *
    length of array
"
) SMO_getLinkSeries;

%feature("autodoc",
"Get time series results for particular attribute. Specify series start and 
length using timeIndex and length respectively.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
attr: SMO_systemAttribute
startPeriod: int
endPeriod: int

Returns
-------
outValueArray: float **
    array of time series values
length: int *
    length of array
"
) SMO_getSystemSeries;


%feature("autodoc",
"For all subcatchments at given time, get a particular attribute.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
timeIndex: int
attr: SMO_subcatchAttribute

Returns
-------
outValueArray: float **
    the array of subcatchment attribute values
length: int *
    length of array
"
) SMO_getSubcatchAttribute;

%feature("autodoc",
"For all nodes at given time, get a particular attribute.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
timeIndex: int
attr: SMO_nodeAttribute

Returns
-------
outValueArray: float **
    the array of node attribute values
length: int *
    length of array
"
) SMO_getNodeAttribute;

%feature("autodoc",
"For all links at given time, get a particular attribute.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
timeIndex: int
attr: SMO_linkAttribute

Returns
-------
outValueArray: float **
    the array of link attribute values
length: int *
    length of array
"
) SMO_getLinkAttribute;

%feature("autodoc",
"For the system at given time, get a particular attribute.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
timeIndex: int
attr: SMO_systemAttribute

Returns
-------
outValueArray: float **
    the array of system attribute values
length: int *
    length of array
"
) SMO_getSystemAttribute;


%feature("autodoc",
"For a subcatchment at given time, get all attributes.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
timeIndex: int
subcatchIndex: int

Returns
-------
outValueArray: float **
    the array of subcatchment result values
length: int *
    length of array
"
) SMO_getSubcatchResult;

%feature("autodoc",
"For a node at given time, get all attributes.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
timeIndex: int
nodeIndex: int

Returns
-------
outValueArray: float **
    the array of node result values
length: int *
    length of array
"
) SMO_getNodeResult;

%feature("autodoc",
"For a link at given time, get all attributes.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
timeIndex: int
linkIndex: int

Returns
-------
outValueArray: float **
    the array of link result values
length: int *
    length of array
"
) SMO_getLinkResult;

%feature("autodoc",
"For the system at given time, get all attributes.

Parameters
----------
p_handle: SMO_Handle
    A SWMM output handle
timeIndex: int
dummyIndex: int

Returns
-------
outValueArray: float **
    the array of system result values
length: int *
    length of array
"
) SMO_getSystemResult;
