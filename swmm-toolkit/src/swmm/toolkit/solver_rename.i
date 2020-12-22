/*
 *  solver_rename.i - Rename mapping for swmm-solver
 *
 *  Created:    2/26/2020
 *  
 *  Author:     See AUTHORS
 *
 *  Purpose: Renames functions according to PEP8
*/


// RENAME STATS STRUCTS
%rename (NodeStats)                         SM_NodeStats;
%rename (StorageStats)                      SM_StorageStats;
%rename (OutfallStats)                      SM_OutfallStats;
%rename (LinkStats)                         SM_LinkStats;
%rename (PumpStats)                         SM_PumpStats;
%rename (SubcatchStats)                     SM_SubcatchStats;
%rename (RoutingTotals)                     SM_RoutingTotals;
%rename (RunoffTotals)                      SM_RunoffTotals;


// RENAME CANONICAL API AS NECESSARY
%rename(swmm_get_mass_balance)              swmm_getMassBalErr;
%rename(swmm_get_version)                   swmm_getVersion;


// RENAME NEW API
%rename(project_get_index)                  swmm_project_findObject;
%rename(project_get_id)                     swmm_getObjectId;
%rename(project_get_count)                  swmm_countObjects;


%rename(simulation_get_datetime)            swmm_getSimulationDateTime;
%rename(simulation_get_current_datetime)    swmm_getCurrentDateTime;
%rename(simulation_set_datetime)            swmm_setSimulationDateTime;
%rename(simulation_get_setting)             swmm_getSimulationAnalysisSetting;
%rename(simulation_get_parameter)           swmm_getSimulationParam;
%rename(simulation_get_unit)                swmm_getSimulationUnit;


%rename(node_get_type)                      swmm_getNodeType;
%rename(node_get_parameter)                 swmm_getNodeParam;
%rename(node_set_parameter)                 swmm_setNodeParam;
%rename(node_get_result)                    swmm_getNodeResult;
%rename(node_get_pollutant)                 swmm_getNodePollut;
%rename(node_get_total_inflow)              swmm_getNodeTotalInflow;
%rename(node_set_total_inflow)              swmm_setNodeInflow;
%rename(node_get_stats)                     swmm_getNodeStats;


%rename(storage_get_stats)                  swmm_getStorageStats;


%rename(outfall_set_stage)                  swmm_setOutfallStage;
%rename(outfall_get_stats)                  swmm_getOutfallStats;


%rename(link_get_type)                      swmm_getLinkType;
%rename(link_get_connections)               swmm_getLinkConnections;
%rename(link_get_direction)                 swmm_getLinkDirection;
%rename(link_get_parameter)                 swmm_getLinkParam;
%rename(link_set_parameter)                 swmm_setLinkParam;
%rename(link_get_result)                    swmm_getLinkResult;
%rename(link_get_pollutant)                 swmm_getLinkPollut;
%rename(link_set_target_setting)            swmm_setLinkSetting;
%rename(link_get_stats)                     swmm_getLinkStats;


%rename(pump_get_stats)                     swmm_getPumpStats;


%rename(subcatch_get_connection)            swmm_getSubcatchOutConnection;
%rename(subcatch_get_parameter)             swmm_getSubcatchParam;
%rename(subcatch_set_parameter)             swmm_setSubcatchParam;
%rename(subcatch_get_result)                swmm_getSubcatchResult;
%rename(subcatch_get_pollutant)             swmm_getSubcatchPollut;
%rename(subcatch_get_stats)                 swmm_getSubcatchStats;


%rename(system_get_routing_totals)          swmm_getSystemRoutingTotals;
%rename(system_get_runoff_totals)           swmm_getSystemRunoffTotals;


%rename(lid_usage_get_count)                swmm_getLidUCount;
%rename(lid_usage_get_parameter)            swmm_getLidUParam;
%rename(lid_usage_set_parameter)            swmm_setLidUParam;
%rename(lid_usage_get_option)               swmm_getLidUOption;
%rename(lid_usage_set_option)               swmm_setLidUOption;
%rename(lid_usage_get_flux_rate)            swmm_getLidUFluxRates;
%rename(lid_usage_get_result)               swmm_getLidUResult;
%rename(lid_control_get_overflow)           swmm_getLidCOverflow;
%rename(lid_control_get_parameter)          swmm_getLidCParam;
%rename(lid_control_set_parameter)          swmm_setLidCParam;
%rename(lid_group_get_result)               swmm_getLidGResult;


%rename(raingage_get_precipitation)         swmm_getGagePrecip;
%rename(raingage_set_precipitation)         swmm_setGagePrecip;


%rename(swmm_version_info)                  swmm_getVersionInfo;
