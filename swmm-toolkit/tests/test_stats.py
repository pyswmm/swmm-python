
import os
import ctypes

import pytest
import numpy 

from swmm.toolkit import solver as swmm
from swmm.toolkit import toolkit_enum


DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
INPUT_FILE_EXAMPLE_1 = os.path.join(DATA_PATH, 'test_Example1.inp')
REPORT_FILE_TEST_1 = os.path.join(DATA_PATH, 'temp_Example.rpt')
OUTPUT_FILE_TEST_1 = os.path.join(DATA_PATH, 'temp_Example.out')


@pytest.fixture()
def before_end(request):
    swmm.solver_open(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST_1, OUTPUT_FILE_TEST_1)
    swmm.solver_start(0)
    
    while True:
        time = swmm.solver_step()
        if time == 0:
            break
    
    def close():
        swmm.solver_end()
        swmm.solver_close()

    request.addfinalizer(close)


def test_node_get_stats(before_end):
    while True:
        time = swmm.solver_step()
        if time == 0:
            break

    node_stats = swmm.node_get_stats(5)
    assert node_stats.maxDepth  == pytest.approx(1.15, 0.1)


def test_storage_get_stats(before_end):
    node_index = swmm.project_get_index(toolkit_enum.ObjectType.NODE, 'SU1')
    while True:
        time = swmm.solver_step()
        if time == 0:
            break

    stor_stats = swmm.storage_get_stats(node_index)
    assert stor_stats.avgVol == pytest.approx(0, 0.1)


def test_outfall_stats(before_end):
    id = '18'

    index = swmm.project_get_index(toolkit_enum.ObjectType.NODE, id)

    stats = swmm.outfall_get_stats(index)
    assert stats.totalLoad != None


def test_get_routing_totals(before_end):

    stats = swmm.system_get_routing_totals()
    assert stats != None


def test_get_runoff_totals(before_end):

    stats = swmm.system_get_runoff_totals()
    assert stats != None
