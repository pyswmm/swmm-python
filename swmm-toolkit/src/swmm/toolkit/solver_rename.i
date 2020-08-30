/*
 *  solver_rename.i - Rename mapping for swmm-solver
 *
 *  Created:    2/26/2020
 *
 *  Author:     Michael E. Tryby
 *              US EPA - ORD/CESER
 *  Author:     Jennifer Wu
 *              Xylem Inc.
 *
*/


// RENAME FUNCTIONS ACCORDING TO PEP8
%rename(run)                                        swmm_run;
%rename(open)                                       swmm_open;
%rename(start)                                      swmm_start;
%rename(step)                                       swmm_step;
%rename(end)                                        swmm_end;
%rename(report)                                     swmm_report;
%rename(get_mass_bal_err)                           swmm_getMassBalErr;
%rename(close)                                      swmm_close;
%rename(get_version)                                swmm_getVersion;
%rename(get_error_message)                          swmm_getAPIError;
%rename(get_simulation_unit)                        swmm_getSimulationUnit;
%rename(find_object)                                swmm_project_findObject;
%rename(count_object)                               swmm_countObjects;
%rename(get_object_index)                           swmm_getObjectIndex;
%rename(get_object_id)                              swmm_getObjectId;
%rename(get_simulation_datetime)                    swmm_getSimulationDateTime;
%rename(set_simulation_datetime)                    swmm_setSimulationDateTime;
%rename(get_simulation_analysis_setting)            swmm_getSimulationAnalysisSetting;
%rename(get_simulation_parameter)                   swmm_getSimulationParam;
%rename(get_current_datetime)                       swmm_getCurrentDateTime;
%rename(get_node_type)                              swmm_getNodeType;
%rename(get_node_parameter)                         swmm_getNodeParam;
%rename(set_node_parameter)                         swmm_setNodeParam;
%rename(get_node_result)                            swmm_getNodeResult;
%rename(get_node_pollutant)                         swmm_getNodePollut;
%rename(get_node_total_inflow)                      swmm_getNodeTotalInflow;
%rename(set_node_total_inflow)                      swmm_setNodeInflow;
%rename(set_outfall_stage)                          swmm_setOutfallStage;
%rename(get_node_stats)                             swmm_getNodeStats;
%rename(get_storage_stats)                          swmm_getStorageStats;
%rename(get_outfall_stats)                          swmm_getOutfallStats;
%rename(get_link_type)                              swmm_getLinkType;
%rename(get_link_connections)                       swmm_getLinkConnections;
%rename(get_link_direction)                         swmm_getLinkDirection;
%rename(get_link_parameter)                         swmm_getLinkParam;
%rename(set_link_parameter)                         swmm_setLinkParam;
%rename(get_link_result)                            swmm_getLinkResult;
%rename(get_link_pollutant)                         swmm_getLinkPollut;
%rename(set_link_target_setting)                    swmm_setLinkSetting;
%rename(get_link_stats)                             swmm_getLinkStats;
%rename(get_pump_stats)                             swmm_getPumpStats;
%rename(get_subcatch_connection)                    swmm_getSubcatchOutConnection;
%rename(get_subcatch_parameter)                     swmm_getSubcatchParam;
%rename(set_subcatch_parameter)                     swmm_setSubcatchParam;
%rename(get_subcatch_result)                        swmm_getSubcatchResult;
%rename(get_subcatch_pollutant)                     swmm_getSubcatchPollut;
%rename(get_lid_usage_count)                        swmm_getLidUCount;
%rename(get_lid_usage_parameter)                    swmm_getLidUParam;
%rename(set_lid_usage_parameter)                    swmm_setLidUParam;
%rename(get_lid_usage_option)                       swmm_getLidUOption;
%rename(set_lid_usage_option)                       swmm_setLidUOption;
%rename(get_lid_control_overflow)                   swmm_getLidCOverflow;
%rename(get_lid_control_parameter)                  swmm_getLidCParam;
%rename(set_lid_control_parameter)                  swmm_setLidCParam;
%rename(get_rain_precipitation)                     swmm_getGagePrecip;
%rename(set_rain_precipitation)                      swmm_setGagePrecip;