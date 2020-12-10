/*
 *  output_rename.i - Rename mapping for swmm-output
 *
 *  Created:    2/12/2020
 *
 *  Author:     See AUTHORS
 *
*/


// RENAME FUNCTIONS ACCORDING TO PEP8
%rename(init)                   SMO_init;
%rename(open)                   SMO_open;
%rename(close)                  SMO_close;
%rename(get_version)            SMO_getVersion;
%rename(get_proj_size)          SMO_getProjectSize;

%rename(get_units)              SMO_getUnits;
%rename(get_start_date)         SMO_getStartDate;
%rename(get_times)              SMO_getTimes;
%rename(get_elem_name)          SMO_getElementName;

%rename(get_subcatch_series)    SMO_getSubcatchSeries;
%rename(get_node_series)        SMO_getNodeSeries;
%rename(get_link_series)        SMO_getLinkSeries;
%rename(get_system_series)      SMO_getSystemSeries;

%rename(get_subcatch_attribute) SMO_getSubcatchAttribute;
%rename(get_node_attribute)     SMO_getNodeAttribute;
%rename(get_link_attribute)     SMO_getLinkAttribute;
%rename(get_system_attribute)   SMO_getSystemAttribute;

%rename(get_subcatch_result)    SMO_getSubcatchResult;
%rename(get_node_result)        SMO_getNodeResult;
%rename(get_link_result)        SMO_getLinkResult;
%rename(get_system_result)      SMO_getSystemResult;
