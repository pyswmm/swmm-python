#
#  test_stats.py
#
#  Created:    Nov  16, 2020
#  Updated:
#
#  Author:     See AUTHORS
#

import os

import pytest

from swmm.toolkit import solver, shared_enum


DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
INPUT_FILE_EXAMPLE_1 = os.path.join(DATA_PATH, 'test_Example1.inp')
REPORT_FILE_TEST_1 = os.path.join(DATA_PATH, 'temp_Example.rpt')
OUTPUT_FILE_TEST_1 = os.path.join(DATA_PATH, 'temp_Example.out')


@pytest.fixture()
def before_end(request):
    solver.swmm_open(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST_1, OUTPUT_FILE_TEST_1)
    solver.swmm_start(0)
    
    while True:
        time = solver.swmm_step()
        if time == 0:
            break
    
    def close():
        solver.swmm_end()
        solver.swmm_close()

    request.addfinalizer(close)


def test_node_get_stats(before_end):
    while True:
        time = solver.swmm_step()
        if time == 0:
            break

    node_stats = solver.node_get_stats(5)
    assert node_stats.maxDepth  == pytest.approx(1.15, 0.1)


def test_storage_get_stats(before_end):
    node_index = solver.project_get_index(shared_enum.ObjectType.NODE, 'SU1')
    while True:
        time = solver.swmm_step()
        if time == 0:
            break

    stor_stats = solver.storage_get_stats(node_index)
    assert stor_stats.avgVol == pytest.approx(0, 0.1)


def test_outfall_stats(before_end):
    id = '18'

    index = solver.project_get_index(shared_enum.ObjectType.NODE, id)

    stats = solver.outfall_get_stats(index)
    assert stats.totalLoad != None


def test_get_routing_totals(before_end):

    stats = solver.system_get_routing_totals()
    assert stats != None


def test_get_runoff_totals(before_end):

    stats = solver.system_get_runoff_totals()
    assert stats != None
