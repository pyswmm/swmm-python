#
#  test_toolkit.py
#
#  Created:    Aug  8, 2018
#  Updated:    Apr 20, 2020
#
#  Author:     Michael E. Tryby
#              US EPA - ORD/NRMRL
#              Jennifer Wu
#              Xylem Inc.


import os

import pytest

from swmm.toolkit import solver, solver_enum

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
    simulation_system_unit_option = solver.get_simulation_unit(solver_enum.UnitProperty.SYSTEM_UNIT)
    simulation_flow_unit_option = solver.get_simulation_unit(solver_enum.UnitProperty.FLOW_UNIT)
    assert simulation_system_unit_option == solver_enum.UnitSystem.US.value
    assert simulation_flow_unit_option == solver_enum.FlowUnits.CFS.value


def test_find_object(handle):
    rg_index = solver.find_object(solver_enum.ObjectProperty.GAGE, 'RG1')
    sub_index_0 = solver.find_object(solver_enum.ObjectProperty.SUBCATCH, '2')
    sub_index_1 = solver.find_object(solver_enum.ObjectProperty.SUBCATCH, '3')
    node_index = solver.find_object(solver_enum.ObjectProperty.NODE, '24')
    link_index = solver.find_object(solver_enum.ObjectProperty.LINK, '16')
    assert rg_index == 0
    assert sub_index_0 == 0
    assert sub_index_1 == 1
    assert node_index == 12
    assert link_index == 12


def test_count_object(handle):
    rg_count = solver.count_object(solver_enum.ObjectProperty.GAGE)
    sub_count = solver.count_object(solver_enum.ObjectProperty.SUBCATCH)
    assert rg_count == 1
    assert sub_count == 8


def test_api_error_message(handle):
    error_message_501 = solver.get_error_message(501)
    assert error_message_501 == '\n API Key Error: Object Type Outside Bonds'


def test_simulation_datetime(handle):
    from datetime import datetime

    year, month, day, hour, minute, second = solver.get_simulation_datetime(solver_enum.TimeProperty.START_DATE)
    assert datetime(1998, 1, 1) == datetime(year, month, day, hour, minute, second)
    year, month, day, hour, minute, second = solver.get_simulation_datetime(solver_enum.TimeProperty.END_DATE)
    assert datetime(1998, 1, 2, 12) == datetime(year, month, day, hour, minute, second)
    year, month, day, hour, minute, second = solver.get_simulation_datetime(solver_enum.TimeProperty.REPORT_DATE)
    assert datetime(1998, 1, 1) == datetime(year, month, day, hour, minute, second)

    solver.set_simulation_datetime(solver_enum.TimeProperty.START_DATE, 2020, 1, 1, 12, 59, 59)
    year, month, day, hour, minute, second = solver.get_simulation_datetime(solver_enum.TimeProperty.START_DATE)
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
    route_step = solver.get_simulation_parameter(0)
    min_route_step = solver.get_simulation_parameter(1)
    min_slope = solver.get_simulation_parameter(6)
    head_tolerance = solver.get_simulation_parameter(11)
    assert route_step == 60
    assert min_route_step == 0.5
    assert min_slope == 0
    assert head_tolerance ==  0


def test_get_object_index(handle):
    node_index = solver.get_object_index(solver_enum.ObjectProperty.NODE, '6')
    sub_index = solver.get_object_index(solver_enum.ObjectProperty.SUBCATCH, '20')

    assert node_index == -1
    assert sub_index == -1
    
    node_index = solver.get_object_index(solver_enum.ObjectProperty.NODE, '20')
    sub_index = solver.get_object_index(solver_enum.ObjectProperty.SUBCATCH, '6')

    assert node_index == 8
    assert sub_index == 5


def test_get_object_id(handle):
    node_name = solver.get_object_id(solver_enum.ObjectProperty.NODE, 8)
    sub_name = solver.get_object_id(solver_enum.ObjectProperty.SUBCATCH, 5)
    assert node_name == '20'
    assert sub_name == '6'


def test_get_node_type(handle):
    node_type = solver.get_node_type(8)
    assert node_type == solver_enum.NodeType.JUNCTION.value
    node_index = solver.get_object_index(solver_enum.ObjectProperty.NODE, '18')
    node_type = solver.get_node_type(node_index)
    assert node_type == solver_enum.NodeType.OUTFALL.value

    
def test_get_link_type(handle):
    link_type = solver.get_link_type(2)
    assert link_type == solver_enum.LinkType.CONDUIT.value


def test_get_link_connections(handle):
    us_node, ds_node = solver.get_link_connections(4)
    assert us_node == 9
    assert ds_node == 10
    
    us_node, ds_node = solver.get_link_connections(0)    
    assert us_node == 0
    assert ds_node == 1


def test_get_subcatch_connection(handle):
    pass


def test_get_link_direction(handle):
    for index in range(0, 13):
        link_direction = solver.get_link_direction(index)
        print(type(link_direction))
        # solver_enum.LinkDirection.UPSTREAM_TO_DOWNSTREAM


def test_node_param(handle):
    pass


def test_link_param(handle):
    pass


def test_sub_param(handle):
    pass




