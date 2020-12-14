/*
 *  solver_docs.i - Documentation for swmm-solver
 *
 *  Created:    12/10/2020
 *  
 *  Author:     See AUTHORS
 *
*/


%define SOLVER_MODULE_DOCS
"Solver Module
"
%enddef


// PUBLIC STRUCTS
%feature("autodoc", 
"Node Statistics

Attributes
----------
avgDepth: double
    average node depth (level)
maxDepth: double
    max node depth (level) (from routing step)
maxDepthDate: DateTime
    date of maximum depth
maxRptDepth: double
    max node depth (level) (from reporting step)
volFlooded: double
    total volume flooded (volume)
timeFlooded: double
    total time flooded
timeSurcharged: double
    total time surcharged
timeCourantCritical: double
    total time courant critical
totLatFlow: double
    total lateral inflow (volume)
maxLatFlow: double
    maximum lateral inflow (flowrate)
maxInflow: double
    maximum total inflow (flowrate)
maxOverflow: double
    maximum flooding (flowrate)
maxPondedVol: double
    maximum ponded volume (volume)
maxInflowDate: DateTime
    date of maximum inflow
maxOverflowDate: DateTime
    date of maximum overflow
" 
) SM_NodeStats();


%feature("autodoc", 
"Storage Statistics

Attributes
----------
initVol: double
    initial volume (volume)
avgVol: double
    average volume (volume) (from routing step)
maxVol: double
    maximum volume (volume) (from routing step)
maxFlow: double
    maximum total inflow (flowrate) (from routing step)
evapLosses: double
    evaporation losses (volume)
exfilLosses: double
    exfiltration losses (volume)
maxVolDate: DateTime
    date of maximum volume
" 
) SM_StorageStats();


%feature("autodoc", 
"Outfall Statistics

Attributes
----------
avgFlow: double
    average flow (flowrate)
maxFlow: double
    maximum flow (flowrate) (from routing step)
totalLoad: double *
    total pollutant load (mass)
totalPeriods: double
    total simulation steps (from routing step)
" 
) SM_OutfallStats(int);


%feature("autodoc", 
"Link Statistics

.. rubric:: 'Flow Classes'

===========   ===========================
Flow Class    Description                
===========   ===========================
DRY           dry conduit
UP_DRY        upstream end is dry
DN_DRY        downstream end is dry
SUBCRITICAL   sub-critical flow
SUPCRITICAL   super-critical flow
UP_CRITICAL   free-fall at upstream end
DN_CRITICAL   free-fall at downstream end
===========   ===========================

Attributes
----------
maxFlow: double
    maximum flow (flowrate) (from routing step)
maxFlowDate: double
    date of maximum flowrate
maxVeloc: double
    maximum velocity (from routing step)
maxDepth: double
    maximum depth (level)
timeNormalFlow: double
    time in normal flow
timeInletControl: double
    time under inlet control
timeSurcharged: double
    time surcharged
timeFullUpstream: double
    time full upstream
timeFullDnstream: double
    time full downstream
timeFullFlow: double
    time full flow
timeCapacityLimited: double
    time capacity limited
timeInFlowClass: double[7]
    time in flow class (See: 'Flow Classes')
timeCourantCritical: double
    time courant critical
flowTurns: double
    number of flow turns
flowTurnSign: double
    number of flow turns sign
" 
) SM_LinkStats();


%feature("autodoc", 
"Pump Statistics

Attributes
----------
utilized: double
    time utilized
minFlow: double
    minimum flowrate
avgFlow: double
    average flowrate
maxFlow: double
    maximum flowrate
volume: double
    total pumping volume (volume)
energy: double
    total energy demand
offCurveLow: double
    hysteresis low (off depth wrt curve)
offCurveHigh: double
    hysteresis high (on depth wrt curve)
startUps: int
    number of start ups
totalPeriods: int
    total simulation steps (from routing step)
" 
) SM_PumpStats();


%feature("autodoc", 
"Subcatchment Statistics

Attributes
----------
precip: double
    total precipication (length)
runon: double
    total runon (volume)
evap: double
    total evaporation (volume)
infil: double
    total infiltration (volume)
runoff: double
    total runoff (volume)
maxFlow: double
    maximum runoff rate (flowrate)
" 
) SM_SubcatchStats();


%feature("autodoc", 
"System Flow Routing Totals

Attributes
----------
dwInflow: double
    dry weather inflow
wwInflow: double
    wet weather inflow
gwInflow: double
    groundwater inflow
iiInflow: double
    RDII inflow
exInflow: double
    direct inflow
flooding: double
    internal flooding
outflow: double
    external outflow
evapLoss: double
    evaporation loss
seepLoss: double
    seepage loss
reacted: double
    reaction losses
initStorage: double
    initial storage volume
finalStorage: double
    final storage volume
pctError: double
    continuity error
" 
) SM_RoutingTotals();


%feature("autodoc", 
"System Runoff Totals

Attributes
----------
rainfall: double
    rainfall total (depth)
evap: double
    evaporation loss (volume)
infil: double
    infiltration loss (volume)
runoff: double
    runoff volume (volume)
drains: double
    LID drains (volume)
runon: double
    runon from outfalls (volume)
initStorage: double
    inital surface storage (depth)
finalStorage: double
    final surface storage (depth)
initSnowCover: double
    initial snow cover (depth)
finalSnowCover: double
    final snow cover (depth)
snowRemoved: double
    snow removal (depth)
pctError: double
    continuity error (%)
" 
) SM_RunoffTotals();


// CANONICAL API
%feature("autodoc", 
"Opens SWMM input file, reads in network data, runs, and closes

Parameters
----------
f1: char const *
    pointer to name of input file (must exist)
f2: char const *
    pointer to name of report file (to be created)
f3: char const *
    pointer to name of binary output file (to be created)
"
) swmm_run;


%feature("autodoc",
"Opens SWMM input file & reads in network data

Parameters
----------
f1: char const *
    pointer to name of input file (must exist)
f2: char const *
    pointer to name of report file (to be created)
f3: char const *
    pointer to name of binary output file (to be created)
"
) swmm_open;


%feature("autodoc",
"Start SWMM simulation

Parameters
----------
saveFlag: int
    TRUE or FALSE to save timeseries to report file
"
) swmm_start;


%feature("autodoc",
"Step SWMM simulation forward

Returns
-------
elapsedTime: double
    elapsed simulation time [milliseconds]
"
) swmm_step;


%feature("autodoc",
"End SWMM simulation   
"
) swmm_end;


%feature("autodoc",
"Write text report file
"
) swmm_report;


%feature("autodoc",
"Get routing errors

Returns
-------
runoffErr: float *
    Runoff routing error
flowErr: float * 
    Flow routing error
qualErr: float * 
    Quality routing error
"
) swmm_getMassBalErr;


%feature("autodoc",
"Frees all memory and files used by SWMM
"
) swmm_close;


%feature("autodoc",
"Get Legacy SWMM version number

Returns
-------
version: int
    Version number
"
) swmm_getVersion;


// TOOLKIT API
%feature("autodoc",
"Get full semantic version number info

Returns
-------
major: char ** 
    sematic version major number
minor: char ** 
    sematic version minor number
patch: char ** 
    sematic version patch number
"
) swmm_getVersionInfo;


%feature("autodoc",
"Finds the index of an object given its ID.

Parameters
----------
type: SM_ObjectType
    type An object type (see :ref: SM_ObjectType)
id: char *
    id The object ID

Returns
-------    
index: int *
    The objects index
"
) swmm_project_findObject;


%feature("autodoc", 
"Gets Object ID

Parameters
----------
type: SM_ObjectType
    type Option code (see :ref: SM_ObjectType)
index: int
    index of the Object

Returns
-------
id: char **
    The string ID of object.
"
) swmm_getObjectId;


%feature("autodoc", 
"Gets Object Count

Parameters
----------
type: SM_ObjectType
    Option code (see :ref: SM_ObjectType)

Returns
-------
count: int *
    Option value
"
) swmm_countObjects;


%feature("autodoc", 
"Get the simulation datetime information

Parameters
----------
type: SM_TimePropety
    The property type code (See :ref: SM_TimePropety)

Returns
-------
year: int *
    The year
month: int *
    The month
day: int *
    The day
hour: int *
    The hour
minute: int *
    The minute
second: int *
    The seconds
"
) swmm_getSimulationDateTime;


%feature("autodoc", 
"Get the current simulation datetime information.

Returns
-------
year: int *
    The year
month: int *
    The month
day: int *
    The day
hour: int *
    The hour
minute: int *
    The minute
second: int *
    The seconds
"
) swmm_getCurrentDateTime;


%feature("autodoc", 
"Set simulation datetime information.

Parameters
----------
type: SM_TimePropety 
    type The property type code (See :ref: SM_TimePropety)
year: int
    The year
month: int
    The month
day: int
    The day
hour: int
    The hour
minute: int
    The minute
second: int
    The seconds
"
) swmm_setSimulationDateTime;


%feature("autodoc", 
"Gets Simulation Analysis Setting

Parameters
----------
type: SM_SimOption
    Option code (see :ref: SM_SimOption)

Returns
-------
value: int *
    Option value
"
) swmm_getSimulationAnalysisSetting;


%feature("autodoc", 
"Gets Simulation Analysis Setting

Parameters
----------
type: SM_SimSetting
    Option code (see :ref: SM_SimSetting)

Returns
-------
value: double *
    Option value
"
) swmm_getSimulationParam;


%feature("autodoc",
"Gets Simulation Unit

Parameters
----------
type: SM_Units
    Option code (see :ref: SM_Units)

Returns
-------
value: int *
    Option value
"
) swmm_getSimulationUnit;


%feature("autodoc", 
"Get the type of node with specified index.

Parameters
----------
index: int
    The index of a node

Returns
-------
Ntype: SM_NodeType *
    The type code for the node (:ref: SM_NodeType). 
    id must be pre-allocated by the caller.
"
) swmm_getNodeType;


%feature("autodoc", 
"Get a property value for specified node.

Parameters
----------
index: int
    The index of a node
param: SM_NodeProperty
    The property type code (See :ref: SM_NodeProperty)

Returns
-------
value: double *
    The value of the node's property
"
) swmm_getNodeParam;


%feature("autodoc", 
"Set a property value for specified node.

Parameters
----------
index: int
    The index of a node
param: SM_NodeProperty
    The property type code (See :ref: SM_NodeProperty)
value: double
    The new value of the node's property
"
) swmm_setNodeParam;


%feature("autodoc", 
"Get a result value for specified node.

Parameters
----------
index: int
    The index of a node
type: SM_NodeResult
    The property type code (See :ref: SM_NodeResult)

Returns
-------
result: double *
    The result of the node's property
"
) swmm_getNodeResult;


%feature("autodoc", 
"Gets pollutant values for a specified node.

Parameters
----------
index: int
    The index of a node
type: SM_NodePollut
    The property type code (see :ref: SM_NodePollut)

Returns
-------
PollutArray: double *
    result array
"
) swmm_getNodePollut;


%feature("autodoc", 
"Get the cumulative inflow for a node.

Parameters
----------
index: int
    The index of a node

Returns
-------
value: double *
    The total inflow.
"
) swmm_getNodeTotalInflow;


%feature("autodoc", 
"Set an inflow rate to a node. The inflow rate is held constant until the 
caller changes it.

Parameters
----------
index: int
    The node index.
flowrate: double
    The new node inflow rate.
"
) swmm_setNodeInflow;


%feature("autodoc", 
"Get a node statistics.

Parameters
----------
index: int
    The index of a node

Returns
-------
nodeStats: SM_NodeStats * 
    The Node Stats struct (see :ref: SM_NodeStats) pre-allocated by the caller.
"
) swmm_getNodeStats;


%feature("autodoc", 
"Get a storage statistics.

Parameters
----------
index: int
    The index of a storage node

Returns
-------
storageStats: SM_StorageStats * 
    The storage Stats struct (see :ref: SM_StorageStats) pre-allocated by the caller.
"
) swmm_getStorageStats;


%feature("autodoc", 
"Set outfall stage.

Parameters
----------
index: int
    The outfall node index.
stage: double
    The outfall node stage (head).
"
) swmm_setOutfallStage;


%feature("autodoc", 
"Get outfall statistics.

Parameters
----------
index: int
    The index of a outfall node

Returns
-------
outfallStats: SM_OutfallStats * 
    The outfall Stats struct (see :ref: SM_OutfallStats).
    pre-allocated by the caller. Caller is also responsible for freeing the
    SM_OutfallStats structure using swmm_freeOutfallStats(). This frees any
    pollutants array.
"
) swmm_getOutfallStats;


%feature("autodoc", 
"Get the type of link with specified index.

Parameters
----------
index: int
    The index of a link

Returns
-------
Ltype: SM_LinkType *
    The type code for the link (:ref: SM_LinkType).
"
) swmm_getLinkType;


%feature("autodoc", 
"Get the link Connection Node Indeces. If the conduit has a negative slope, 
the dynamic wave solver will automatically reverse the nodes. 

Parameters
----------
index: int
    The index of a link

Returns
-------
Node1: int *
    The upstream node index.
Node2: int *
    The downstream node index.
"
) swmm_getLinkConnections;


%feature("autodoc", 
"Get the link flow direction

Parameters
----------
index: int
    The index of a link

Returns
-------
value: char *
    The link flow direction.
"
) swmm_getLinkDirection;


%feature("autodoc", 
"Get a property value for specified link.

Parameters
----------
index: int
    The index of a link
param: SM_LinkProperty
    The property type code (See :ref: SM_LinkProperty)

Returns
-------
value: double *
    The value of the link's property
"
) swmm_getLinkParam;


%feature("autodoc", 
"Set a property value for specified link.

Parameters
----------
index: int
    The index of a link
param: SM_LinkProperty
    The property type code (See :ref: SM_LinkProperty)
value: double
    The new value of the link's property
"
) swmm_setLinkParam;


%feature("autodoc", 
"Get a result value for specified link.

Parameters
----------
index: int
    The index of a link
type: SM_LinkResult
    The property type code (See :ref: SM_LinkResult)

Returns
-------
result: double *
    The result of the link's property
"
) swmm_getLinkResult;


%feature("autodoc", 
"Gets pollutant values for a specified link.

Parameters
----------
index: int
    The index of a link
type: SM_LinkPollut
    The property type code (see :ref: SM_LinkPollut)

Returns
-------
PollutArray: double *
    result array
"
) swmm_getLinkPollut;


%feature("autodoc", 
"Set a link setting (pump, orifice, or weir). Setting for an orifice and a 
weir should be [0, 1]. A setting for a pump can range from [0, inf). However, 
if a pump is set to 1, it will pump at its maximum curve setting.

Parameters
----------
index: int
    The link index.
setting: double
    The new setting for the link.
"
) swmm_setLinkSetting;


%feature("autodoc", 
"Get link statistics.

Parameters
----------
index: int
    The link index.

Returns
-------
linkStats: SM_LinkStats *
    The link Stats struct (see :ref: SM_LinkStats). pre-allocated by the caller.
"
) swmm_getLinkStats;


%feature("autodoc", 
"Get pump statistics.

Parameters
----------
index: int
    The index of a pump

Returns
-------
pumpStats: SM_PumpStats *
    The link Stats struct (see :ref: SM_PumpStats). pre-allocated by the caller.
"
) swmm_getPumpStats;


%feature("autodoc", 
"Get the Subcatchment connection. Subcatchments can load to a node, another 
subcatchment, or itself.

Parameters
----------
index: int
    The index of a Subcatchment

Returns
-------
type: SM_ObjectType
    The type of object loading (See :ref: SM_ObjectType)
out_index: int *
    The object index
"
) swmm_getSubcatchOutConnection;


%feature("autodoc", 
"Get a property value for specified subcatchment.

Parameters
----------
index: int
    The index of a subcatchment
param: SM_SubcProperty
    The property type code (See :ref: SM_SubcProperty)

Returns
-------
value: double *
    The value of the subcatchment's property
"
) swmm_getSubcatchParam;


%feature("autodoc", 
"Set a property value for specified subcatchment.

Parameters
----------
index: int
    The index of a subcatchment
param: SM_SubcProperty
    The property type code (See :ref: SM_SubcProperty)
value: double
    The new value of the subcatchment's property
"
) swmm_setSubcatchParam;


%feature("autodoc", 
"Get a result value for specified subcatchment.

Parameters
----------
index: int
    The index of a subcatchment
type: SM_SubcResult
    The property type code (See :ref: SM_SubcResult)

Returns
-------
result: double *
    The result of the subcatchment's property
"
) swmm_getSubcatchResult;


%feature("autodoc", 
"Gets pollutant values for a specified subcatchment.

Parameters
----------
index: int
    The index of a subcatchment
type: SM_SubcPollut
    The property type code (see :ref: SM_SubcPollut)

Returns
-------
PollutArray: double **
    result array
"
) swmm_getSubcatchPollut;


%feature("autodoc", 
"Get subcatchment statistics.

Parameters
----------
index: int
    The index of a subcatchment

Returns
-------
subcatchStats: SM_SubcatchStats *
    The link Stats struct (see :ref: SM_SubcatchStats).
    pre-allocated by the caller. Caller is also responsible for freeing the
    SM_SubcatchStats structure using swmm_freeSubcatchStats(). This frees any
    pollutants array.
"
) swmm_getSubcatchStats;


%feature("autodoc", 
"Get system routing totals.

Returns
-------
routingTot: SM_RoutingTotals *
    The system Routing Stats struct (see :ref: SM_RoutingTotals).
    pre-allocated by the caller.
"
) swmm_getSystemRoutingTotals;


%feature("autodoc", 
"Get system runoff totals.

Returns
-------
runoffTot: SM_RunoffTotals *
    The system Runoff Stats struct (see :ref: SM_RunoffTotals).
    pre-allocated by the caller.
"
) swmm_getSystemRunoffTotals;


%feature("autodoc", 
"Get the number of lid units on a subcatchment.

Parameters
----------
index: int
    The index of a subcatchment

Returns
-------
value: int *
    The number of lid units on a subcatchment
"
) swmm_getLidUCount;


%feature("autodoc", 
"Get a property value for a specified lid unit on a specified subcatchment

Parameters
----------
index: int
    The index of a subcatchment
lidIndex: int
    The index of specified lid unit
param: SM_LidUProperty
    The property type code (See :ref: SM_LidUProperty)

Returns
-------
value: double
    The value of the lid unit's property
"
) swmm_getLidUParam;


%feature("autodoc", 
"Set a property value for a specified lid unit on a specified subcatchment

Parameters
----------
index: int
    The index of a subcatchment
lidIndex: int
    The index of specified lid unit
param: SM_LidUProperty
    The property type code (See :ref: SM_LidUProperty)
value: double
    The new value of the lid unit's property
"
) swmm_setLidUParam;


%feature("autodoc", 
"Get the lid option for a specified lid unit on a specified subcatchment

Parameters
----------
index: int
    The index of a subcatchment
lidIndex: int
    The index of specified lid unit
param: SM_LidUOptions
    The lid option type code (See :ref: SM_LidUOptions)

Returns
-------
value: int *
    The value of the option for the lid unit
"
) swmm_getLidUOption;


%feature("autodoc", 
"Set the lid option for a specified lid unit on a specified subcatchment

Parameters
----------
index: int
    The index of a subcatchment
lidIndex: int
    The index of specified lid unit
param: SM_LidUOptions
    The lid option type code (See :ref: SM_LidUOptions)
value: int
    The new value of the option for the lid unit
"
) swmm_setLidUOption;


%feature("autodoc", 
"Get the lid unit water balance simulated value at current time

Parameters
----------
index: int
    The index of a subcatchment
lidIndex: int
    The index of specified lid unit
layerIndex: SM_LidLayer
    The index of specified lid layer (See :ref: SM_LidLayer)

Returns
-------
result: double * 
    The result for the specified lid unit
"
) swmm_getLidUFluxRates;


%feature("autodoc", 
"Get the lid unit of a specified subcatchment result at current time

Parameters
----------
index: int
    The index of a subcatchment
lidIndex: int
    The index of specified lid unit
type: SM_LidResult
    The result type code (See :ref: SM_LidResult)

Returns
-------
result: double *
    The result for the specified lid unit
"
) swmm_getLidUResult;


%feature("autodoc", 
"Get the lid control surface immediate overflow condition

Parameters
----------
lidControlIndex: int
    The index of specified lid control

Returns
-------
condition: int *
    The value of surface immediate overflow condition
"
) swmm_getLidCOverflow;


%feature("autodoc", 
"Get a property value for specified lid control

Parameters
----------
lidControlIndex: int
    The index of specified lid control
layerIndex: SM_LidLayer
    The index of specified lid layer (See :ref: SM_LidLayer)
param: SM_LidLayerProperty
    The property type code (See :ref: SM_LidLayerProperty)

Returns
-------
value: double 
    The value of lid control's property
"
) swmm_getLidCParam;


%feature("autodoc", 
"Set a property value for specified lid control

Parameters
----------
lidControlIndex: int
    The index of specified lid control
layerIndex: SM_LidLayer
    The index of specified lid layer (See :ref: SM_LidLayer)
param: SM_LidLayerProperty
    The property type code (See :ref: SM_LidLayerProperty)
value: double
    The new value for the lid control's property
"
) swmm_setLidCParam;


%feature("autodoc", 
"Get the lid group of a specified subcatchment result at current time

Parameters
----------
index: int
    The index of a subcatchment
type: SM_LidResult
    The result type code (See :ref: SM_LidResult)

Returns
-------
result: double *
    The result for the specified lid group
"
) swmm_getLidGResult;


%feature("autodoc", 
"Get precipitation rates for a gage.

Parameters
----------
index: int
    The index of gage
type: SM_GagePrecip
    The property type code (see :ref: SM_GagePrecip)

Returns
-------
GageArray: double *
    precipitation rate
"
) swmm_getGagePrecip;


%feature("autodoc", 
"Set a total precipitation intensity to the gage.

Parameters
----------
index: int
    The gage index.
total_precip: double
    The new total precipitation intensity.
"
) swmm_setGagePrecip;
