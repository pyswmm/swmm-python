
import os, sys
import pytest
import pandas as pd

from swmm.toolkit import shared_enum

HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(HERE,'..','wrappers'))
from utils import get_ts_from_model
DATA_PATH = os.path.join(HERE, 'data')
OUTPUT_FILE_EXAMPLE1 = os.path.join(DATA_PATH, 'test_Example1.out')
CONDUIT_IDs = ['15', '6']
NODE_IDs = ['21', '24']



def test_get_ts_from_model_link():
    df = get_ts_from_model(OUTPUT_FILE_EXAMPLE1, CONDUIT_IDs, shared_enum.LinkAttribute.FLOW_RATE, 
                        object_type='link')

    df_dict = {'15': {pd.Timestamp('1998-01-01 00:00:00'): 0.0, 
    pd.Timestamp('1998-01-01 01:00:00'): 5.613319396972656, 
    pd.Timestamp('1998-01-01 02:00:00'): 11.292198181152344}, 
    '6': {pd.Timestamp('1998-01-01 00:00:00'): 0.0, 
    pd.Timestamp('1998-01-01 01:00:00'): 2.4767236709594727, 
    pd.Timestamp('1998-01-01 02:00:00'): 4.6317620277404785}}

    df_1 = df.iloc[0:3]
    df_2 = pd.DataFrame(df_dict)
    pd.testing.assert_frame_equal(df_1, df_2)

def test_get_ts_from_model_node():
    df = get_ts_from_model(OUTPUT_FILE_EXAMPLE1, NODE_IDs, shared_enum.NodeAttribute.TOTAL_INFLOW, 
                        object_type='node')

    df_dict = {'21': {pd.Timestamp('1998-01-01 00:00:00'): 0.0, 
    pd.Timestamp('1998-01-01 01:00:00'): 2.577545166015625, 
    pd.Timestamp('1998-01-01 02:00:00'): 4.874996662139893}, 
    '24': {pd.Timestamp('1998-01-01 00:00:00'): 0.0, 
    pd.Timestamp('1998-01-01 01:00:00'): 5.915661334991455, 
    pd.Timestamp('1998-01-01 02:00:00'): 11.939848899841309}}

    df_1 = df.iloc[0:3]
    df_2 = pd.DataFrame(df_dict)
    pd.testing.assert_frame_equal(df_1, df_2)
