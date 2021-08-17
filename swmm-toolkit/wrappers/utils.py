'''
Created on Fri Jun 18 09:55:14 2021

@author: Mehmet B. Ercan 
'''



from swmm.toolkit import output, shared_enum
import julian, datetime
import pandas as pd


def find_linkid_index(handle,link_id):
    i = 0
    while True:
        if output.get_elem_name(handle, shared_enum.ElementType.LINK, i) == link_id:
            break
        i+=1
    return i 

def find_nodeid_index(handle,node_id):
    i = 0
    while True:
        if output.get_elem_name(handle, shared_enum.ElementType.NODE, i) == node_id:
            break
        i+=1
    return i 

def get_date_time_array(handle):
    report_start_date_time = output.get_start_date(handle)
    num_steps = output.get_times(handle, shared_enum.Time.NUM_PERIODS)
    report_step = output.get_times(handle, shared_enum.Time.REPORT_STEP)
    date_times = []
    for ind in range(num_steps):
        if ind == 0:
            datetime_dbl = report_start_date_time + (ind * 1.0 * report_step / 86400.0) + 2415018.5
            date_time_0 = julian.from_jd(datetime_dbl, 'jd')
            date_times.append(date_time_0)
        else:
            date_time = date_time_0 + datetime.timedelta(seconds=report_step)*ind
            date_times.append(date_time)
    return date_times, num_steps


def get_ts_from_model(swmm_out, object_ids, attribute, object_type='link'):
    '''
    Parameters (---- it only works with link and nodes for now ----)
    ----------
    swmm_out : SWMM model output file 
    object_ids : SWMM model node/link ID (eg. ['a','b'] : list of links or nodes) 
    attribute : python  swmm library attribute for type of data 
        (eg. for link flow rate: output.LinkAttribute.FLOW_RATE)

    Returns
    -------
    Pandas dataframe time series for the "object_ids"

    '''

    # open handle
    handle = output.init()
    output.open(handle, swmm_out)
    # Get Date Time array
    date_times, num_steps = get_date_time_array(handle)
    
    # Extract time series data
    objectid_values = {}
    for objid in object_ids:
        start_index=0
        if object_type == 'link':
            link_index = find_linkid_index(handle, objid)
            values = output.get_link_series(handle,link_index, attribute, start_index, num_steps)
        elif object_type == 'node':
            node_index = find_nodeid_index(handle, objid)
            values = output.get_node_series(handle,node_index, attribute, start_index, num_steps)
        else:
            values = []
        objectid_values[objid] = values

    # close handle
    output.close(handle)

    # read model time series into pandas dataframe
    df = pd.DataFrame(objectid_values, index = date_times) 
    return df


