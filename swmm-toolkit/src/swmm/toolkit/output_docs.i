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
"
) SMO_init;

%feature("autodoc",
"Open binary output file and reads prologue and epilogue.

Parameters
----------
p_handle: SMO_Handle
path: char const *
"
) SMO_open;

%feature("autodoc",
"Close binary output file and perform cleanup. 

Parameters
----------
p_handle: SMO_Handle
"
) SMO_close;

%feature("autodoc",
"Get the SWMM version that produced the binary output file. 

Parameters
----------
p_handle: SMO_Handle
"
) SMO_getVersion;

%feature("autodoc",
"Project element counts.

Parameters
----------
p_handle: SMO_Handle
"
) SMO_getProjectSize;


%feature("autodoc",
"Project unit flags for unit_system, flow, and pollutants.

Parameters
----------
p_handle: SMO_Handle
"
) SMO_getUnits;

%feature("autodoc",
"Analysis start date.

Parameters
----------
p_handle: SMO_Handle
"
) SMO_getStartDate;

%feature("autodoc",
"Analysis step size and number of periods.

Parameters
----------
p_handle: SMO_Handle
code: SMO_time
"
) SMO_getTimes;

%feature("autodoc",
"Given an element index returns the element name.

Parameters
----------
p_handle: SMO_Handle
type: SMO_elementType
elementIndex: int
"
) SMO_getElementName;


%feature("autodoc",
"Get time series results for particular attribute. Specify series start and 
length using timeIndex and length respectively.

Parameters
----------
p_handle: SMO_Handle
subcatchIndex: int
attr: SMO_subcatchAttribute
startPeriod: int
endPeriod: int
"
) SMO_getSubcatchSeries;

%feature("autodoc",
"Get time series results for particular attribute. Specify series start and 
length using timeIndex and length respectively.

Parameters
----------
p_handle: SMO_Handle
nodeIndex: int
attr: SMO_nodeAttribute
startPeriod: int
endPeriod: int
"
) SMO_getNodeSeries;

%feature("autodoc",
"Get time series results for particular attribute. Specify series start and 
length using timeIndex and length respectively.

Parameters
----------
p_handle: SMO_Handle
linkIndex: int
attr: SMO_linkAttribute
startPeriod: int
endPeriod: int
"
) SMO_getLinkSeries;

%feature("autodoc",
"Get time series results for particular attribute. Specify series start and 
length using timeIndex and length respectively.

Parameters
----------
p_handle: SMO_Handle
attr: SMO_systemAttribute
startPeriod: int
endPeriod: int
"
) SMO_getSystemSeries;


%feature("autodoc",
"For all subcatchments at given time, get a particular attribute.

Parameters
----------
p_handle: SMO_Handle
timeIndex: int
attr: SMO_subcatchAttribute
"
) SMO_getSubcatchAttribute;

%feature("autodoc",
"For all nodes at given time, get a particular attribute.

Parameters
----------
p_handle: SMO_Handle
timeIndex: int
attr: SMO_nodeAttribute
"
) SMO_getNodeAttribute;

%feature("autodoc",
"For all links at given time, get a particular attribute.

Parameters
----------
p_handle: SMO_Handle
timeIndex: int
attr: SMO_linkAttribute
"
) SMO_getLinkAttribute;

%feature("autodoc",
"For the system at given time, get a particular attribute.

Parameters
----------
p_handle: SMO_Handle
timeIndex: int
attr: SMO_systemAttribute
"
) SMO_getSystemAttribute;


%feature("autodoc",
"For a subcatchment at given time, get all attributes.

Parameters
----------
p_handle: SMO_Handle
timeIndex: int
subcatchIndex: int
"
) SMO_getSubcatchResult;

%feature("autodoc",
"For a node at given time, get all attributes.

Parameters
----------
p_handle: SMO_Handle
timeIndex: int
nodeIndex: int
"
) SMO_getNodeResult;

%feature("autodoc",
"For a link at given time, get all attributes.

Parameters
----------
p_handle: SMO_Handle
timeIndex: int
linkIndex: int
"
) SMO_getLinkResult;

%feature("autodoc",
"For the system at given time, get all attributes.

Parameters
----------
p_handle: SMO_Handle
timeIndex: int
dummyIndex: int
"
) SMO_getSystemResult;
