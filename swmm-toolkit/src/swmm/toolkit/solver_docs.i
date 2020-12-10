


// PUBLIC STRUCTS
%feature("autodoc", 
"Node Statistics

Attributes
----------
avgDepth
    average node depth (level)
maxDepth
    max node depth (level) (from routing step)
maxDepthDate
    date of maximum depth
maxRptDepth
    max node depth (level) (from reporting step)
volFlooded
    total volume flooded (volume)
timeFlooded
    total time flooded
timeSurcharged
    total time surcharged
timeCourantCritical
    total time courant critical
totLatFlow
    total lateral inflow (volume)
maxLatFlow
    maximum lateral inflow (flowrate)
maxInflow
    maximum total inflow (flowrate)
maxOverflow
    maximum flooding (flowrate)
maxPondedVol
    maximum ponded volume (volume)
maxInflowDate
    date of maximum inflow
maxOverflowDate
    date of maximum overflow
" 
) SM_NodeStats();

%feature("autodoc", 
"Storage Statistics

Attributes
----------
initVol
    initial volume (volume)
avgVol
    average volume (volume) (from routing step)
maxVol
    maximum volume (volume) (from routing step)
maxFlow
    maximum total inflow (flowrate) (from routing step)
evapLosses
    evaporation losses (volume)
exfilLosses
    exfiltration losses (volume)
maxVolDate
    date of maximum volume
" 
) SM_StorageStats();

%feature("autodoc", 
"Outfall Statistics

Attributes
----------
avgFlow
    average flow (flowrate)
maxFlow
    maximum flow (flowrate) (from routing step)
totalLoad
    total pollutant load (mass)
totalPeriods
    total simulation steps (from routing step)
" 
) SM_OutfallStats();

%feature("autodoc", 
"Link Statistics

.. rubric:: Flow 'Classes'

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
maxFlow
    maximum flow (flowrate) (from routing step)
maxFlowDate
    date of maximum flowrate
maxVeloc
    maximum velocity (from routing step)
maxDepth
    maximum depth (level)
timeNormalFlow
    time in normal flow
timeInletControl
    time under inlet control
timeSurcharged
    time surcharged
timeFullUpstream
    time full upstream
timeFullDnstream
    time full downstream
timeFullFlow
    time full flow
timeCapacityLimited
    time capacity limited
timeInFlowClass
    time in flow class (See: Flow Classes)
timeCourantCritical
    time courant critical
flowTurns
    number of flow turns
flowTurnSign
    number of flow turns sign
" 
) SM_LinkStats();

%feature("autodoc", 
"Pump Statistics

Attributes
----------
utilized
    time utilized
minFlow
    minimum flowrate
avgFlow
    average flowrate
maxFlow
    maximum flowrate
volume
    total pumping volume (volume)
energy
    total energy demand
offCurveLow
    hysteresis low (off depth wrt curve)
offCurveHigh
    hysteresis high (on depth wrt curve)
startUps
    number of start ups
totalPeriods
    total simulation steps (from routing step)
" 
) SM_PumpStats();

%feature("autodoc", 
"Subcatchment Statistics

Attributes
----------
precip
    total precipication (length)
runon
    total runon (volume)
evap
    total evaporation (volume)
infil
    total infiltration (volume)
runoff
    total runoff (volume)
maxFlow
    maximum runoff rate (flowrate)
" 
) SM_SubcatchStats();

%feature("autodoc", 
"Routing Totals

Attributes
----------
dwInflow
    dry weather inflow
wwInflow
    wet weather inflow
gwInflow
    groundwater inflow
iiInflow
    RDII inflow
exInflow
    direct inflow
flooding
    internal flooding
outflow
    external outflow
evapLoss
    evaporation loss
seepLoss
    seepage loss
reacted
    reaction losses
initStorage
    initial storage volume
finalStorage
    final storage volume
pctError
    continuity error
" 
) SM_RoutingTotals();

%feature("autodoc", 
"Runoff Totals

Attributes
----------
rainfall
    rainfall total (depth)
evap
    evaporation loss (volume)
infil
    infiltration loss (volume)
runoff
    runoff volume (volume)
drains
    LID drains (volume)
runon
    runon from outfalls (volume)
initStorage
    inital surface storage (depth)
finalStorage
    final surface storage (depth)
initSnowCover
    initial snow cover (depth)
finalSnowCover
    final snow cover (depth)
snowRemoved
    snow removal (depth)
pctError
    continuity error (%)
" 
) SM_RunoffTotals();


// CANONICAL API
%feature("autodoc", 
"Opens SWMM input file, reads in network data, runs, and closes

swmm_run(f1, f2, f3) -> int

Parameters
----------
f1: char const *
f2: char const *
f3: char const *
"
) swmm_run;

%feature("autodoc",
"Opens SWMM input file & reads in network data

swmm_open(f1, f2, f3) -> int

Parameters
----------
f1: char const *
f2: char const *
f3: char const *
"
) swmm_open;

%feature("autodoc",
"Start SWMM simulation

swmm_start(saveFlag) -> int

Parameters
----------
saveFlag: int
"
) swmm_start;

%feature("autodoc",
"Step SWMM simulation forward
    
swmm_step() -> int
"
) swmm_step;

%feature("autodoc",
"End SWMM simulation   
    
swmm_end() -> int
"
) swmm_end;

%feature("autodoc",
"Write text report file

swmm_report() -> int
"
) swmm_report;

%feature("autodoc",
"Get routing errors

swmm_get_mass_balance() -> int
"
) swmm_getMassBalErr;

%feature("autodoc",
"Frees all memory and files used by SWMM
    
swmm_close() -> int
"
) swmm_close;

%feature("autodoc",
"Get Legacy SWMM version number

swmm_get_version() -> int
"
) swmm_getVersion;


// TOOLKIT API
%feature("autodoc",
"Get full semantic version number info

swmm_version_info() -> int
"
) swmm_getVersionInfo;

%feature("autodoc",
"Finds the index of an object given its ID.

project_get_index(type, id) -> int

Parameters
----------
type: SM_ObjectType
id: char *
"
) swmm_project_findObject;

%feature("autodoc", 
"project_get_id(type, index) -> int

Parameters
----------
type: SM_ObjectType
index: int
"
) swmm_getObjectId;

%feature("autodoc", 
"project_get_count(type) -> int

Parameters
----------
type: SM_ObjectType
"
) swmm_countObjects;


%feature("autodoc", 
"simulation_get_datetime(type) -> int

Parameters
----------
type: SM_TimePropety
"
) swmm_getSimulationDateTime;

%feature("autodoc", 
"simulation_get_current_datetime() -> int
"
) swmm_getCurrentDateTime;

%feature("autodoc", 
"simulation_set_datetime(type, year, month, day, hour, minute, second) -> int

Parameters
----------
type: SM_TimePropety
year: int
month: int
day: int
hour: int
minute: int
second: int
"
) swmm_setSimulationDateTime;

%feature("autodoc", 
"simulation_get_setting(type) -> int

Parameters
----------
type: SM_SimOption
"
) swmm_getSimulationAnalysisSetting;

%feature("autodoc", 
"simulation_get_parameter(type) -> int

Parameters
----------
type: SM_SimSetting
"
) swmm_getSimulationParam;

%feature("autodoc",
"Gets Simulation Unit
simulation_get_unit(type) -> int

Parameters
----------
type: SM_Units
"
) swmm_getSimulationUnit;


%feature("autodoc", 
"node_get_type(index) -> int

Parameters
----------
index: int
"
) swmm_getNodeType;

%feature("autodoc", 
"node_get_parameter(index, param) -> int

Parameters
----------
index: int
param: SM_NodeProperty
"
) swmm_getNodeParam;

%feature("autodoc", 
"node_set_parameter(index, param, value) -> int

Parameters
----------
index: int
param: SM_NodeProperty
value: double
"
) swmm_setNodeParam;

%feature("autodoc", 
"node_get_result(index, type) -> int

Parameters
----------
index: int
type: SM_NodeResult
"
) swmm_getNodeResult;

%feature("autodoc", 
"node_get_pollutant(index, type) -> int

Parameters
----------
index: int
type: SM_NodePollut
"
) swmm_getNodePollut;

%feature("autodoc", 
"node_get_total_inflow(index) -> int

Parameters
----------
index: int
"
) swmm_getNodeTotalInflow;

%feature("autodoc", 
"node_set_total_inflow(index, flowrate) -> int

Parameters
----------
index: int
flowrate: double
"
) swmm_setNodeInflow;

%feature("autodoc", 
"node_get_stats(index) -> int

Parameters
----------
index: int
"
) swmm_getNodeStats;


%feature("autodoc", 
"storage_get_stats(index) -> int

Parameters
----------
index: int
"
) swmm_getStorageStats;


%feature("autodoc", 
"outfall_set_stage(index, stage) -> int

Parameters
----------
index: int
stage: double
"
) swmm_setOutfallStage;

%feature("autodoc", 
"outfall_get_stats(index) -> int

Parameters
----------
index: int
"
) swmm_getOutfallStats;


%feature("autodoc", 
"link_get_type(index) -> int

Parameters
----------
index: int
"
) swmm_getLinkType;

%feature("autodoc", 
"link_get_connections(index) -> int

Parameters
----------
index: int
"
) swmm_getLinkConnections;

%feature("autodoc", 
"link_get_direction(index) -> int

Parameters
----------
index: int
"
) swmm_getLinkDirection;

%feature("autodoc", 
"link_get_parameter(index, param) -> int

Parameters
----------
index: int
param: SM_LinkProperty
"
) swmm_getLinkParam;

%feature("autodoc", 
"link_set_parameter(index, param, value) -> int

Parameters
----------
index: int
param: SM_LinkProperty
value: double
"
) swmm_setLinkParam;

%feature("autodoc", 
"link_get_result(index, type) -> int

Parameters
----------
index: int
type: SM_LinkResult
"
) swmm_getLinkResult;

%feature("autodoc", 
"link_get_pollutant(index, type) -> int

Parameters
----------
index: int
type: SM_LinkPollut
"
) swmm_getLinkPollut;

%feature("autodoc", 
"link_set_target_setting(index, setting) -> int

Parameters
----------
index: int
setting: double
"
) swmm_setLinkSetting;

%feature("autodoc", 
"link_get_stats(index) -> int

Parameters
----------
index: int
"
) swmm_getLinkStats;


%feature("autodoc", 
"pump_get_stats(index) -> int

Parameters
----------
index: int
"
) swmm_getPumpStats;


%feature("autodoc", 
"subcatch_get_connection(index) -> int

Parameters
----------
index: int
"
) swmm_getSubcatchOutConnection;

%feature("autodoc", 
"subcatch_get_parameter(index, param) -> int

Parameters
----------
index: int
param: SM_SubcProperty
"
) swmm_getSubcatchParam;

%feature("autodoc", 
"subcatch_set_parameter(index, param, value) -> int

Parameters
----------
index: int
param: SM_SubcProperty
value: double
"
) swmm_setSubcatchParam;

%feature("autodoc", 
"subcatch_get_result(index, type) -> int

Parameters
----------
index: int
type: SM_SubcResult
"
) swmm_getSubcatchResult;

%feature("autodoc", 
"subcatch_get_pollutant(index, type) -> int

Parameters
----------
index: int
type: SM_SubcPollut
"
) swmm_getSubcatchPollut;

%feature("autodoc", 
"subcatch_get_stats(index) -> int

Parameters
----------
index: int
"
) swmm_getSubcatchStats;


%feature("autodoc", 
"system_get_routing_totals() -> int
"
) swmm_getSystemRoutingTotals;

%feature("autodoc", 
"system_get_runoff_totals() -> int
"
) swmm_getSystemRunoffTotals;


%feature("autodoc", 
"lid_usage_get_count(index) -> int

Parameters
----------
index: int
"
) swmm_getLidUCount;

%feature("autodoc", 
"lid_usage_get_parameter(index, lidIndex, param) -> int

Parameters
----------
index: int
lidIndex: int
param: SM_LidUProperty
"
) swmm_getLidUParam;

%feature("autodoc", 
"lid_usage_set_parameter(index, lidIndex, param, value) -> int

Parameters
----------
index: int
lidIndex: int
param: SM_LidUProperty
value: double
"
) swmm_setLidUParam;

%feature("autodoc", 
"lid_usage_get_option(index, lidIndex, param) -> int

Parameters
----------
index: int
lidIndex: int
param: SM_LidUOptions
"
) swmm_getLidUOption;

%feature("autodoc", 
"lid_usage_set_option(index, lidIndex, param, value) -> int

Parameters
----------
index: int
lidIndex: int
param: SM_LidUOptions
value: int
"
) swmm_setLidUOption;

%feature("autodoc", 
"lid_usage_get_flux_rate(index, lidIndex, layerIndex) -> int

Parameters
----------
index: int
lidIndex: int
layerIndex: SM_LidLayer
"
) swmm_getLidUFluxRates;

%feature("autodoc", 
"lid_usage_get_result(index, lidIndex, type) -> int

Parameters
----------
index: int
lidIndex: int
type: SM_LidResult
"
) swmm_getLidUResult;

%feature("autodoc", 
"lid_control_get_overflow(lidControlIndex) -> int

Parameters
----------
lidControlIndex: int
"
) swmm_getLidCOverflow;

%feature("autodoc", 
"lid_control_get_parameter(lidControlIndex, layerIndex, param) -> int

Parameters
----------
lidControlIndex: int
layerIndex: SM_LidLayer
param: SM_LidLayerProperty
"
) swmm_getLidCParam;

%feature("autodoc", 
"lid_control_set_parameter(lidControlIndex, layerIndex, param, value) -> int

Parameters
----------
lidControlIndex: int
layerIndex: SM_LidLayer
param: SM_LidLayerProperty
value: double
"
) swmm_setLidCParam;

%feature("autodoc", 
"lid_group_get_result(index, type) -> int

Parameters
----------
index: int
type: SM_LidResult
"
) swmm_getLidGResult;


%feature("autodoc", 
"raingage_get_precipitation(index, type) -> int

Parameters
----------
index: int
type: SM_GagePrecip
"
) swmm_getGagePrecip;

%feature("autodoc", 
"raingage_set_precipitation(index, total_precip) -> int

Parameters
----------
index: int
total_precip: double
"
) swmm_setGagePrecip;
