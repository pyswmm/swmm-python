/*
 *  solver_toolkitapi_rename.i - Rename mapping for swmm-solver tookitapi 
 *
 *  Created:    08/17/2020
 *
 *  Author:     Jennifer Wu
 *              Xylem Inc.
 *
*/


// RENAME FUNCTIONS ACCORDING TO PEP8
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
%rename(get_node_type)                              swmm_getNodeType;
%rename(get_node_parameter)                         swmm_getNodeParam;
%rename(set_node_parameter)                         swmm_setNodeParam;
%rename(get_link_type)                              swmm_getLinkType;
%rename(get_link_connections)                       swmm_getLinkConnections;
%rename(get_link_direction)                         swmm_getLinkDirection;
%rename(get_link_parameter)                         swmm_getLinkParam;
%rename(set_link_parameter)                         swmm_setLinkParam;
%rename(get_subcatch_connection)                    swmm_getSubcatchOutConnection;
%rename(get_subcatch_parameter)                     swmm_getSubcatchParam;
%rename(set_subcatch_parameter)                     swmm_setSubcatchParam;