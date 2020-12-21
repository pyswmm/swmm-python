#
#  test_toolkit.py
#
#  Created:    Aug  8, 2018
#  Updated:    Apr 20, 2020
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
INPUT_FILE_EXAMPLE_2 = os.path.join(DATA_PATH, 'test_Example2.inp')
REPORT_FILE_TEST_2 = os.path.join(DATA_PATH, 'temp_Example2.rpt')
OUTPUT_FILE_TEST_2 = os.path.join(DATA_PATH, 'temp_Example2.out')
INPUT_FILE_FAIL = os.path.join(DATA_PATH, 'temp_nodata.inp')


def test_run():
    solver.swmm_run(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST_1, OUTPUT_FILE_TEST_1)


def test_openclose():
    solver.swmm_open(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST_1, OUTPUT_FILE_TEST_1)
    solver.swmm_close()


def test_errorhandling():
    with pytest.raises(Exception):
        solver.swmm_open(INPUT_FILE_FAIL, REPORT_FILE_TEST_1, OUTPUT_FILE_TEST_1)


@pytest.fixture()
def handle(request):
    solver.swmm_open(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST_1, OUTPUT_FILE_TEST_1)

    def close():
        solver.swmm_close()

    request.addfinalizer(close)


@pytest.fixture()
def run_sim(request):
    solver.swmm_open(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST_1, OUTPUT_FILE_TEST_1)
    solver.swmm_start(0)

    def close():
        solver.swmm_end()
        solver.swmm_close()

    request.addfinalizer(close)


@pytest.fixture()
def lid_handle(request):
    solver.swmm_open(INPUT_FILE_EXAMPLE_2, REPORT_FILE_TEST_2, OUTPUT_FILE_TEST_2)


    def close():
        solver.swmm_close()

    request.addfinalizer(close)


@pytest.fixture()
def run_lid_sim(request):
    solver.swmm_open(INPUT_FILE_EXAMPLE_2, REPORT_FILE_TEST_2, OUTPUT_FILE_TEST_2)
    solver.swmm_start(0)

    def close():
        solver.swmm_end()
        solver.swmm_close()

    request.addfinalizer(close)


def test_step(handle):
    solver.swmm_start(0)

    while True:
        time = solver.swmm_step()
        if time == 0:
            break

    solver.swmm_end()
    solver.swmm_report()


def test_version(handle):
    major, minor, patch = solver.swmm_version_info()
    print(major, minor, patch)
    assert major == '5'
    

def test_simulation_unit(handle):
    simulation_system_unit_option = solver.simulation_get_unit(shared_enum.UnitProperty.SYSTEM_UNIT)
    simulation_flow_unit_option = solver.simulation_get_unit(shared_enum.UnitProperty.FLOW_UNIT)
    assert simulation_system_unit_option == shared_enum.UnitSystem.US.value
    assert simulation_flow_unit_option == shared_enum.FlowUnits.CFS.value


def test_object_find(handle):
    rg_index = solver.project_get_index(shared_enum.ObjectType.GAGE, 'RG1')
    sub_index_0 = solver.project_get_index(shared_enum.ObjectType.SUBCATCH, '2')
    sub_index_1 = solver.project_get_index(shared_enum.ObjectType.SUBCATCH, '3')
    node_index = solver.project_get_index(shared_enum.ObjectType.NODE, '24')
    link_index = solver.project_get_index(shared_enum.ObjectType.LINK, '16')
    assert rg_index == 0
    assert sub_index_0 == 0
    assert sub_index_1 == 1
    assert node_index == 12
    assert link_index == 12


def test_error_message_handling(handle):
    with pytest.raises(Exception) as exc_info:
        solver.project_get_index(shared_enum.ObjectType.SUBCATCH, 'sloth')

    assert 'API Key Error: Object index out of Bounds' in str(exc_info.value)


def test_object_count(handle):
    rg_count = solver.project_get_count(shared_enum.ObjectType.GAGE)
    sub_count = solver.project_get_count(shared_enum.ObjectType.SUBCATCH)
    assert rg_count == 1
    assert sub_count == 8


#def test_api_error_message(handle):
#    error_message_501 = solver.error_get_message(501)
#    assert error_message_501 == '\n API Key Error: Object Type Outside Bonds'


def test_simulation_datetime(handle):
    from datetime import datetime

    year, month, day, hour, minute, second = solver.simulation_get_datetime(shared_enum.TimeProperty.START_DATE)
    assert datetime(1998, 1, 1) == datetime(year, month, day, hour, minute, second)
    year, month, day, hour, minute, second = solver.simulation_get_datetime(shared_enum.TimeProperty.END_DATE)
    assert datetime(1998, 1, 2, 12) == datetime(year, month, day, hour, minute, second)
    year, month, day, hour, minute, second = solver.simulation_get_datetime(shared_enum.TimeProperty.REPORT_DATE)
    assert datetime(1998, 1, 1) == datetime(year, month, day, hour, minute, second)

    solver.simulation_set_datetime(shared_enum.TimeProperty.START_DATE, 2020, 1, 1, 12, 59, 59)
    year, month, day, hour, minute, second = solver.simulation_get_datetime(shared_enum.TimeProperty.START_DATE)
    assert datetime(2020, 1, 1, 12, 59, 59) == datetime(year, month, day, hour, minute, second)


def test_simulation_get_current_datetime(run_sim):
    from datetime import datetime
    current_datetime = datetime(*solver.simulation_get_current_datetime())
    assert current_datetime == datetime(1998, 1, 1)


def test_simulation_analysis_setting(handle):
    allow_ponding = solver.simulation_get_setting(0)
    skip_steady = solver.simulation_get_setting(1)
    ignore_rain = solver.simulation_get_setting(2)
    ignore_gw = solver.simulation_get_setting(5)
    assert allow_ponding == 0
    assert skip_steady == 0
    assert ignore_rain == 0
    assert ignore_gw == 1


def test_simulation_parameter(handle):
    route_step = solver.simulation_get_parameter(0)
    min_route_step = solver.simulation_get_parameter(1)
    min_slope = solver.simulation_get_parameter(6)
    head_tolerance = solver.simulation_get_parameter(11)
    assert route_step == 60
    assert min_route_step == 0.5
    assert min_slope == 0
    assert head_tolerance ==  0


def test_object_get_index(handle):
    with pytest.raises(Exception) as exc_info:
        node_index = solver.project_get_index(shared_enum.ObjectType.NODE, '6')
        sub_index = solver.project_get_index(shared_enum.ObjectType.SUBCATCH, '20')

#    assert node_index == -1
#    assert sub_index == -1

    node_index = solver.project_get_index(shared_enum.ObjectType.NODE, '20')
    sub_index = solver.project_get_index(shared_enum.ObjectType.SUBCATCH, '6')

    assert node_index == 8
    assert sub_index == 5


def test_object_get_id(handle):
    node_name = solver.project_get_id(shared_enum.ObjectType.NODE, 8)
    sub_name = solver.project_get_id(shared_enum.ObjectType.SUBCATCH, 5)
    assert node_name == '20'
    assert sub_name == '6'


def test_link_get_type(handle):
    link_type = solver.link_get_type(2)
    assert link_type == shared_enum.LinkType.CONDUIT


def test_link_get_connections(handle):
    us_node, ds_node = solver.link_get_connections(4)
    assert us_node == 9
    assert ds_node == 10

    us_node, ds_node = solver.link_get_connections(0)
    assert us_node == 0
    assert ds_node == 1


def test_link_get_direction(handle):
    for index in range(0, 13):
        link_direction = solver.link_get_direction(index)
        assert link_direction == shared_enum.LinkDirection.UPSTREAM_TO_DOWNSTREAM.value


def test_link_param(handle):
    offset_1 = solver.link_get_parameter(0, shared_enum.LinkProperty.OFFSET_1)
    offset_2 = solver.link_get_parameter(0, shared_enum.LinkProperty.OFFSET_2)
    initial_flow = solver.link_get_parameter(0, shared_enum.LinkProperty.INITIAL_FLOW)
    flow_limit = solver.link_get_parameter(0, shared_enum.LinkProperty.FLOW_LIMIT)
    inlet_loss = solver.link_get_parameter(0, shared_enum.LinkProperty.INLET_LOSS)
    outlet_loss = solver.link_get_parameter(0, shared_enum.LinkProperty.OUTLET_LOSS)
    average_loss = solver.link_get_parameter(0, shared_enum.LinkProperty.AVERAGE_LOSS)

    assert offset_1 == 0
    assert offset_2 == 0
    assert initial_flow == 0
    assert flow_limit == 0
    assert inlet_loss == 0
    assert outlet_loss == 0
    assert average_loss == 0

    solver.link_set_parameter(0, shared_enum.LinkProperty.OFFSET_1, 0.2)
    solver.link_set_parameter(0, shared_enum.LinkProperty.OFFSET_2, 0.1)
    solver.link_set_parameter(0, shared_enum.LinkProperty.INITIAL_FLOW, 0.1)
    solver.link_set_parameter(0, shared_enum.LinkProperty.FLOW_LIMIT, 1)
    solver.link_set_parameter(0, shared_enum.LinkProperty.INLET_LOSS, 0.5)
    solver.link_set_parameter(0, shared_enum.LinkProperty.OUTLET_LOSS, 1.0)
    solver.link_set_parameter(0, shared_enum.LinkProperty.AVERAGE_LOSS, 0.2)

    offset_1 = solver.link_get_parameter(0, shared_enum.LinkProperty.OFFSET_1)
    offset_2 = solver.link_get_parameter(0, shared_enum.LinkProperty.OFFSET_2)
    initial_flow = solver.link_get_parameter(0, shared_enum.LinkProperty.INITIAL_FLOW)
    flow_limit = solver.link_get_parameter(0, shared_enum.LinkProperty.FLOW_LIMIT)
    inlet_loss = solver.link_get_parameter(0, shared_enum.LinkProperty.INLET_LOSS)
    outlet_loss = solver.link_get_parameter(0, shared_enum.LinkProperty.OUTLET_LOSS)
    average_loss = solver.link_get_parameter(0, shared_enum.LinkProperty.AVERAGE_LOSS)

    assert offset_1 == 0.2
    assert offset_2 == 0.1
    assert initial_flow == 0.1
    assert flow_limit == 1
    assert inlet_loss == 0.5
    assert outlet_loss == 1.0
    assert average_loss == 0.2


def test_link_get_result(run_sim):
    flow = solver.link_get_result(0, shared_enum.LinkResult.FLOW)
    depth = solver.link_get_result(0, shared_enum.LinkResult.DEPTH)
    assert flow == 0.0
    assert depth == 0.0
    for i in range(0, 100):
        solver.swmm_step()
    flow = solver.link_get_result(0, shared_enum.LinkResult.FLOW)
    depth = solver.link_get_result(0, shared_enum.LinkResult.DEPTH)
    assert flow == pytest.approx(1.054, 0.1)
    assert depth == pytest.approx(0.268, 0.1)


def test_link_get_pollutant(run_sim):
    pollut = solver.link_get_pollutant(0, shared_enum.NodePollutant.QUALITY)
    tss, lead = tuple(pollut)
    assert tss == 0.0
    assert lead == 0.0

    for i in range(0, 250):
        solver.swmm_step()
    pollut = solver.link_get_pollutant(0, shared_enum.NodePollutant.QUALITY)

    tss, lead = tuple(pollut)

    assert tss == pytest.approx(14.7179, 0.1)
    assert lead == pytest.approx(2.9435, 0.1)


def test_link_set_target_setting(run_sim):
    target_setting = solver.link_get_result(0, shared_enum.LinkResult.TARGET_SETTING)
    assert target_setting == 1.0
    solver.link_set_target_setting(0, 0.5)
    target_setting = solver.link_get_result(0, shared_enum.LinkResult.TARGET_SETTING)
    assert target_setting == 0.5

    for i in range(0, 250):
        solver.swmm_step()

    target_setting = solver.link_get_result(0, shared_enum.LinkResult.TARGET_SETTING)
    target_setting == 0.5


def test_link_get_stats(run_sim):
    while True:
        time = solver.swmm_step()
        if time == 0:
            break

    link_stats = solver.link_get_stats(0)


def test_pump_get_stats(run_sim):
    index = solver.project_get_index(shared_enum.ObjectType.LINK, 'P1')
    while True:
        time = solver.swmm_step()
        if time == 0:
            break

    stats = solver.pump_get_stats(index)


def test_node_get_type(handle):
    node_type = solver.node_get_type(8)
    assert node_type == shared_enum.NodeType.JUNCTION
    node_index = solver.project_get_index(shared_enum.ObjectType.NODE, '18')
    node_type = solver.node_get_type(node_index)
    assert node_type == shared_enum.NodeType.OUTFALL


def test_node_param(handle):
    invert_elevation = solver.node_get_parameter(0, shared_enum.NodeProperty.INVERT_ELEVATION)
    full_depth = solver.node_get_parameter(0, shared_enum.NodeProperty.FULL_DEPTH)
    surcharge_depth = solver.node_get_parameter(0, shared_enum.NodeProperty.SURCHARGE_DEPTH)
    pond_area = solver.node_get_parameter(0, shared_enum.NodeProperty.POND_AREA)
    initial_depth = solver.node_get_parameter(0, shared_enum.NodeProperty.INITIAL_DEPTH)

    assert invert_elevation == 1000
    assert full_depth == 3
    assert surcharge_depth == 0
    assert pond_area == 0
    assert initial_depth == 0

    solver.node_set_parameter(0, shared_enum.NodeProperty.INVERT_ELEVATION, 90)
    solver.node_set_parameter(0, shared_enum.NodeProperty.FULL_DEPTH, 10)
    solver.node_set_parameter(0, shared_enum.NodeProperty.SURCHARGE_DEPTH, 100)
    solver.node_set_parameter(0, shared_enum.NodeProperty.POND_AREA, 100)
    solver.node_set_parameter(0, shared_enum.NodeProperty.INITIAL_DEPTH, 1)

    invert_elevation = solver.node_get_parameter(0, shared_enum.NodeProperty.INVERT_ELEVATION)
    full_depth = solver.node_get_parameter(0, shared_enum.NodeProperty.FULL_DEPTH)
    surcharge_depth = solver.node_get_parameter(0, shared_enum.NodeProperty.SURCHARGE_DEPTH)
    pond_area = solver.node_get_parameter(0, shared_enum.NodeProperty.POND_AREA)
    initial_depth = solver.node_get_parameter(0, shared_enum.NodeProperty.INITIAL_DEPTH)

    assert invert_elevation == 90
    assert full_depth == 10
    assert surcharge_depth == 100
    assert pond_area == 100
    assert initial_depth == 1


def test_node_get_result(run_sim):
    total_inflow = solver.node_get_result(0, shared_enum.NodeResult.TOTAL_INFLOW)
    total_outflow = solver.node_get_result(0, shared_enum.NodeResult.TOTAL_OUTFLOW)
    assert total_inflow == 0.0
    assert total_outflow == 0.0
    for i in range(0, 100):
        solver.swmm_step()
    total_inflow = solver.node_get_result(0, shared_enum.NodeResult.TOTAL_INFLOW)
    total_outflow = solver.node_get_result(0, shared_enum.NodeResult.TOTAL_OUTFLOW)
    assert total_inflow == pytest.approx(1.07, 0.1)
    assert total_outflow == pytest.approx(1.07, 0.1)


def test_node_get_pollutant(run_sim):
    pollut = solver.node_get_pollutant(0, shared_enum.NodePollutant.QUALITY)
    tss, lead = tuple(pollut)
    assert tss == 0.0
    assert lead == 0.0

    for i in range(0, 250):
        solver.swmm_step()
    pollut = solver.node_get_pollutant(0, shared_enum.NodePollutant.QUALITY)

    tss, lead = tuple(pollut)
    assert tss == pytest.approx(14.7179, 0.1)
    assert lead == pytest.approx(2.9435, 0.1)


def test_node_total_inflow(run_sim):
    total_inflow = solver.node_get_total_inflow(0)
    assert total_inflow == 0.0

    for i in range(0, 550):
        solver.swmm_step()

    total_inflow = solver.node_get_total_inflow(0)
    assert total_inflow == pytest.approx(42639.814, 0.1)

    solver.node_set_total_inflow(0, 1.0)

    for i in range(0, 550):
        solver.swmm_step()

    total_inflow = solver.node_get_total_inflow(0)
    assert total_inflow == pytest.approx(75644.471, 0.1)


def test_outfall_set_stage(run_sim):
    head = solver.node_get_result(13, shared_enum.NodeResult.HEAD)
    head == 975

    for i in range(0, 100):
        solver.swmm_step()

    head = solver.node_get_result(13, shared_enum.NodeResult.HEAD)
    assert head == pytest.approx(975.519, 0.1)

    solver.outfall_set_stage(13, 1000)
    solver.swmm_step()


def test_subcatch_param(handle):
    width = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.WIDTH)
    area = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.AREA)
    impervious_fraction = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.IMPERVIOUS_FRACTION)
    slope = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.SLOPE)
    curb_length = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.CURB_LENGTH)

    assert width == 500
    assert area == 10
    assert impervious_fraction == 50/100
    assert slope == 0.01/100
    assert curb_length == 0

    solver.subcatch_set_parameter(0, shared_enum.SubcatchProperty.WIDTH, 100)
    solver.subcatch_set_parameter(0, shared_enum.SubcatchProperty.AREA, 50)
    #solver.subcatch_set_parameter(0, shared_enum.SubcatchProperty.IMPERVIOUS_FRACTION, 100)
    solver.subcatch_set_parameter(0, shared_enum.SubcatchProperty.SLOPE, 0.1)
    solver.subcatch_set_parameter(0, shared_enum.SubcatchProperty.CURB_LENGTH, 10)

    width = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.WIDTH)
    area = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.AREA)
    #impervious_fraction = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.IMPERVIOUS_FRACTION)
    slope = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.SLOPE)
    curb_length = solver.subcatch_get_parameter(0, shared_enum.SubcatchProperty.CURB_LENGTH)

    assert width == 100
    assert area == 50
    #assert impervious_fraction == 100/100
    assert slope == 0.1
    assert curb_length == 10


def test_subcatch_get_connection(handle):
    object_type, object_index = solver.subcatch_get_connection(0)
    assert object_type == shared_enum.ObjectType.NODE
    assert object_index == 1

    object_type, object_index = solver.subcatch_get_connection(1)
    assert object_type == shared_enum.ObjectType.NODE
    assert object_index == 2
    object_type, object_index = solver.subcatch_get_connection(2)
    assert object_type == shared_enum.ObjectType.NODE
    assert object_index == 0
    object_type, object_index = solver.subcatch_get_connection(3)
    assert object_type == shared_enum.ObjectType.NODE
    assert object_index == 10


def test_subcatch_get_result(run_sim):
    rain = solver.subcatch_get_result(0, shared_enum.SubcatchResult.RAIN)
    evaporation = solver.subcatch_get_result(0, shared_enum.SubcatchResult.EVAPORATION)
    assert rain == 0.0
    assert evaporation == 0.0
    for i in range(0, 100):
        solver.swmm_step()
    rain = solver.subcatch_get_result(0, shared_enum.SubcatchResult.RAIN)
    evaporation = solver.subcatch_get_result(0, shared_enum.SubcatchResult.EVAPORATION)
    assert rain == pytest.approx(0.25, 0.1)
    assert evaporation == pytest.approx(0.0, 0.1)


def test_subcatch_get_pollutant(run_sim):
    pollut = solver.subcatch_get_pollutant(0, shared_enum.SubcatchPollutant.BUILD_UP)
    tss, lead = tuple(pollut)
    assert tss == 0.0
    assert lead == 0.0

    for i in range(0, 250):
        solver.swmm_step()
    pollut = solver.subcatch_get_pollutant(0, shared_enum.SubcatchPollutant.BUILD_UP)

    tss, lead = tuple(pollut)
    assert tss == pytest.approx(44.246, 0.1)
    assert lead == 0.0


def test_subcatch_get_stats(run_sim):
    while True:
        time = solver.swmm_step()
        if time == 0:
            break

    stats = solver.subcatch_get_stats(0)


def test_lid_usage_get_count(lid_handle):
    subcatch_usage_1 = solver.lid_usage_get_count(0)
    subcatch_usage_2 = solver.lid_usage_get_count(1)

    assert subcatch_usage_1 == 1
    assert subcatch_usage_2 == 0


def test_lid_usage_parameter(lid_handle):
    unit_area = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.UNIT_AREA)
    top_width = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.TOP_WIDTH)
    #bottom_width = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.BOTTOM_WIDTH)
    initial_saturation = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.INITIAL_SATURATION)
    from_impervious = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.FROM_IMPERVIOUS)
    from_pervious = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.FROM_PERVIOUS)

    assert unit_area == 50
    assert top_width == 10
    #assert bottom_width == pytest.approx(0)
    assert initial_saturation == 0
    assert from_impervious == 25
    assert from_pervious == 0

    solver.lid_usage_set_parameter(0, 0, shared_enum.LidUsageProperty.UNIT_AREA, 100)
    solver.lid_usage_set_parameter(0, 0, shared_enum.LidUsageProperty.TOP_WIDTH, 20)
    #solver.lid_usage_set_parameter(0, 0, shared_enum.LidUsageProperty.BOTTOM_WIDTH, 20)
    solver.lid_usage_set_parameter(0, 0, shared_enum.LidUsageProperty.INITIAL_SATURATION, 10)
    solver.lid_usage_set_parameter(0, 0, shared_enum.LidUsageProperty.FROM_IMPERVIOUS, 50)
    solver.lid_usage_set_parameter(0, 0, shared_enum.LidUsageProperty.FROM_PERVIOUS, 10)

    unit_area = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.UNIT_AREA)
    top_width = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.TOP_WIDTH)
    #bottom_width = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.BOTTOM_WIDTH)
    initial_saturation = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.INITIAL_SATURATION)
    from_impervious = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.FROM_IMPERVIOUS)
    from_pervious = solver.lid_usage_get_parameter(0, 0, shared_enum.LidUsageProperty.FROM_PERVIOUS)

    assert unit_area == 100
    assert top_width == 20
    #assert bottom_width == 0
    assert initial_saturation == 10
    assert from_impervious == 50
    assert from_pervious == 10


def test_lid_usage_option(lid_handle):
    index = solver.lid_usage_get_option(0, 0, shared_enum.LidUsageOption.INDEX)
    number = solver.lid_usage_get_option(0, 0, shared_enum.LidUsageOption.NUMBER)
    to_perv = solver.lid_usage_get_option(0, 0, shared_enum.LidUsageOption.TO_PERV)
    drain_subcatch = solver.lid_usage_get_option(0, 0, shared_enum.LidUsageOption.DRAIN_SUBCATCH)
    drain_node = solver.lid_usage_get_option(0, 0, shared_enum.LidUsageOption.DRAIN_NODE)

    assert index == 0
    assert number == 100
    assert to_perv == 1
    assert drain_subcatch == -1
    assert drain_node == 0

    solver.lid_usage_set_option(0, 0, shared_enum.LidUsageOption.NUMBER, 200)

    number = solver.lid_usage_get_option(0, 0, shared_enum.LidUsageOption.NUMBER)
    assert number == 200


def test_lid_usage_get_flux_rate(run_lid_sim):
    while True:
        time = solver.swmm_step()
        if time == 0:
            break

    rate = solver.lid_usage_get_flux_rate(0, 0, shared_enum.LidLayer.SURFACE)


def test_lid_usage_get_result(run_lid_sim):
    while True:
        time = solver.swmm_step()
        if time == 0:
            break

    result = solver.lid_usage_get_result(0, 0, shared_enum.LidResult.SURFACE_OUTFLOW)


def test_lid_group_get_result(run_lid_sim):
    index = solver.project_get_index(shared_enum.ObjectType.SUBCATCH, 'wBC')
    while True:
        time = solver.swmm_step()
        if time == 0:
            break

    result = solver.lid_group_get_result(index, shared_enum.LidResult.OLD_DRAIN_FLOW)


def test_lid_control_get_overflow(lid_handle):
    overflow_option = solver.lid_control_get_overflow(0)
    # BC surface is greater than zero
    assert overflow_option == 0


def test_lid_control_parameter(lid_handle):
    alpha = solver.lid_control_get_parameter(0, shared_enum.LidLayer.SURFACE, shared_enum.LidLayerProperty.ALPHA)
    surface_thickness = solver.lid_control_get_parameter(0, shared_enum.LidLayer.SURFACE, shared_enum.LidLayerProperty.THICKNESS)
    soil_thickness = solver.lid_control_get_parameter(0, shared_enum.LidLayer.SOIL, shared_enum.LidLayerProperty.THICKNESS)
    storage_thickness = solver.lid_control_get_parameter(0, shared_enum.LidLayer.STORAGE, shared_enum.LidLayerProperty.THICKNESS)

    assert alpha == 1.49
    assert surface_thickness == 6
    assert soil_thickness == 12
    assert storage_thickness == 12

    solver.lid_control_set_parameter(0, shared_enum.LidLayer.SURFACE, shared_enum.LidLayerProperty.THICKNESS, 12)
    surface_thickness = solver.lid_control_get_parameter(0, shared_enum.LidLayer.SURFACE, shared_enum.LidLayerProperty.THICKNESS)
    assert surface_thickness == 12


def test_gage_precipitation(run_sim):
    total = solver.raingage_get_precipitation(0, shared_enum.RainResult.TOTAL)
    snowfall = solver.raingage_get_precipitation(0, shared_enum.RainResult.SNOWFALL)
    rainfall = solver.raingage_get_precipitation(0, shared_enum.RainResult.RAINFALL)
    assert total == 0.0
    assert snowfall == 0.0
    assert rainfall == 0.0

    for i in range(0, 250):
        solver.swmm_step()

    total = solver.raingage_get_precipitation(0, shared_enum.RainResult.TOTAL)
    snowfall = solver.raingage_get_precipitation(0, shared_enum.RainResult.SNOWFALL)
    rainfall = solver.raingage_get_precipitation(0, shared_enum.RainResult.RAINFALL)
    assert total == 0.4
    assert snowfall == 0.0
    assert rainfall == 0.4

    solver.raingage_set_precipitation(0, 1.0)

    for i in range(0, 250):
        solver.swmm_step()

    total = solver.raingage_get_precipitation(0, shared_enum.RainResult.TOTAL)
    snowfall = solver.raingage_get_precipitation(0, shared_enum.RainResult.SNOWFALL)
    rainfall = solver.raingage_get_precipitation(0, shared_enum.RainResult.RAINFALL)
    assert total == 1.0
    assert snowfall == 0.0
    assert rainfall == 1.0
