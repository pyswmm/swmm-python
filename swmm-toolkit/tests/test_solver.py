#
#  test_toolkit.py
#
#  Created:    Aug  8, 2018
#  Updated:    Apr 20, 2020
#
#  Author:     Michael E. Tryby
#              US EPA - ORD/NRMRL
#


import os

import pytest

from swmm.toolkit import solver, swmm_enum, toolkit_enum

DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
INPUT_FILE_EXAMPLE_1 = os.path.join(DATA_PATH, 'test_Example1.inp')
REPORT_FILE_TEST = os.path.join(DATA_PATH, 'temp_Example1.rpt')
OUTPUT_FILE_TEST = os.path.join(DATA_PATH, 'temp_Example1.out')
INPUT_FILE_FAIL = os.path.join(DATA_PATH, 'temp_nodata.inp')


# def test_allocfree():
#     _handle = solver.alloc_project()
#     assert(_handle != None)
#     _handle = solver.free_project(_handle)
#     assert(_handle == None)


def test_run():
    # _handle = solver.alloc_project()
    solver.run(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)
    # solver.free_project(_handle)


def test_openclose():
    # _handle = solver.alloc_project()
    solver.open(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)
    solver.close()
    # solver.free_project(_handle)


def test_errorhandling():
    with pytest.raises(Exception):
        solver.open(INPUT_FILE_FAIL, REPORT_FILE_TEST, OUTPUT_FILE_TEST)


@pytest.fixture()
def handle(request):
    # _handle = solver.alloc_project()
    solver.open(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)

    def close():
        solver.close()
        # solver.free_project(_handle)

    request.addfinalizer(close)
    # return _handle


def test_step(handle):
    solver.start(0)

    while True:
        time = solver.step()

        if time == 0.:
            break

    solver.end()

    solver.report()


def test_simulation_unit(handle):
    simulation_system_unit_option = solver.get_simulation_unit(0)
    simulation_flow_unit_option = solver.get_simulation_unit(1)
    assert simulation_system_unit_option == swmm_enum.UnitSystem.US.value
    assert simulation_flow_unit_option == swmm_enum.FlowUnits.CFS.value


def test_find_object(handle):
    rg_index = solver.find_object(0, 'RG1')
    sub_index_0 = solver.find_object(1, '2')
    sub_index_1 = solver.find_object(1, '3')
    node_index = solver.find_object(2, '24')
    link_index = solver.find_object(3, '16')
    assert rg_index == 0
    assert sub_index_0 == 0
    assert sub_index_1 == 1
    assert node_index == 12
    assert link_index == 12


def test_find_object(handle):
    rg_count = solver.count_object(0)
    sub_count = solver.count_object(1)
    assert rg_count == 1
    assert sub_count == 8


def test_api_error_message(handle):
    error_message_501 = solver.get_error_message(501)
    assert error_message_501 == '\n API Key Error: Object Type Outside Bonds'


def test_simulation_datetime(handle):
    from datetime import datetime

    year, month, day, hour, minute, second = solver.get_simulation_datetime(toolkit_enum.TimeProperty.START_DATE)
    assert datetime(1998, 1, 1) == datetime(year, month, day, hour, minute, second)
    year, month, day, hour, minute, second = solver.get_simulation_datetime(toolkit_enum.TimeProperty.END_DATE)
    assert datetime(1998, 1, 2, 12) == datetime(year, month, day, hour, minute, second)
    year, month, day, hour, minute, second = solver.get_simulation_datetime(toolkit_enum.TimeProperty.REPORT_DATE)
    assert datetime(1998, 1, 1) == datetime(year, month, day, hour, minute, second)

    solver.set_simulation_datetime(toolkit_enum.TimeProperty.START_DATE, 2020, 1, 1, 12, 59, 59)
    year, month, day, hour, minute, second = solver.get_simulation_datetime(toolkit_enum.TimeProperty.START_DATE)
    assert datetime(2020, 1, 1, 12, 59, 59) == datetime(year, month, day, hour, minute, second)


def test_simulation_analysis_setting(handle):
    allow_ponding = solver.get_simulation_analysis_setting(0)
    skip_steady = solver.get_simulation_analysis_setting(1)
    ignore_rain = solver.get_simulation_analysis_setting(2)
    ignore_gw = solver.get_simulation_analysis_setting(5)
    assert allow_ponding == 0
    assert skip_steady == 0
    assert ignore_rain == 0
    assert ignore_gw == 1


def test_simulation_parameter(handle):
    route_step = solver.set_simulation_parameter(0)
    min_route_step = solver.set_simulation_parameter(1)
    min_slope = solver.set_simulation_parameter(6)
    head_tolerance = solver.set_simulation_parameter(11)
    assert route_step == 60
    assert min_route_step == 0.5
    assert min_slope == 0
    assert head_tolerance ==  0


def test_get_object_index(handle):
    node_index = solver.get_object_index(toolkit_enum.ObjectType.NODE, '6')
    sub_index = solver.get_object_index(toolkit_enum.ObjectType.SUBCATCH, '20')
