#
#   test_output.py
#
#   Created: 8/7/2018
#   Author: Michael E. Tryby
#           US EPA - ORD/NRMRL
#
#   Unit testing for SWMM Output API using pytest.
#
import os

import pytest
import numpy as np

from swmm.toolkit import output, output_enum, output_metadata


DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
OUTPUT_FILE_EXAMPLE1 = os.path.join(DATA_PATH, 'Example1.out')


def test_openclose():
    _handle = output.init()
    output.open(_handle, OUTPUT_FILE_EXAMPLE1)
    output.close(_handle)


@pytest.fixture()
def handle(request):
    _handle = output.init()
    output.open(_handle, OUTPUT_FILE_EXAMPLE1)

    def close():
        output.close(_handle)

    request.addfinalizer(close)
    return _handle


def test_outputmetadata(handle):

    om = output_metadata.OutputMetadata(handle)

    ref = {
        output_enum.SubcatchAttribute.RAINFALL:           ("Rainfall",                "in/hr"),
        output_enum.SubcatchAttribute.SNOW_DEPTH:         ("Snow Depth",              "in"),
        output_enum.SubcatchAttribute.EVAP_LOSS:          ("Evaporation Loss",        "in/day"),
        output_enum.SubcatchAttribute.INFIL_LOSS:         ("Infiltration Loss",       "in/hr"),
        output_enum.SubcatchAttribute.RUNOFF_RATE:        ("Runoff Rate",             "cu ft/sec"),
        output_enum.SubcatchAttribute.GW_OUTFLOW_RATE:    ("Groundwater Flow Rate",   "cu ft/sec"),
        output_enum.SubcatchAttribute.GW_TABLE_ELEV:      ("Groundwater Elevation",   "ft"),
        output_enum.SubcatchAttribute.SOIL_MOISTURE:      ("Soil Moisture",           "%"),
        output_enum.SubcatchAttribute.POLLUT_CONC_0:      ("TSS",                     "mg/L"),
        output_enum.SubcatchAttribute.POLLUT_CONC_1:      ("Lead",                    "ug/L"),

        output_enum.NodeAttribute.INVERT_DEPTH:           ("Invert Depth",            "ft"),
        output_enum.NodeAttribute.HYDRAULIC_HEAD:         ("Hydraulic Head",          "ft"),
        output_enum.NodeAttribute.PONDED_VOLUME:          ("Ponded Volume",           "cu ft"),
        output_enum.NodeAttribute.LATERAL_INFLOW:         ("Lateral Inflow",          "cu ft/sec"),
        output_enum.NodeAttribute.TOTAL_INFLOW:           ("Total Inflow",            "cu ft/sec"),
        output_enum.NodeAttribute.FLOODING_LOSSES:        ("Flooding Loss",           "cu ft/sec"),
        output_enum.NodeAttribute.POLLUT_CONC_0:          ("TSS",                     "mg/L"),
        output_enum.NodeAttribute.POLLUT_CONC_1:          ("Lead",                    "ug/L"),

        output_enum.LinkAttribute.FLOW_RATE:              ("Flow Rate",               "cu ft/sec"),
        output_enum.LinkAttribute.FLOW_DEPTH:             ("Flow Depth",              "ft"),
        output_enum.LinkAttribute.FLOW_VELOCITY:          ("Flow Velocity",           "ft/sec"),
        output_enum.LinkAttribute.FLOW_VOLUME:            ("Flow Volume",             "cu ft"),
        output_enum.LinkAttribute.CAPACITY:               ("Capacity",                "%"),
        output_enum.LinkAttribute.POLLUT_CONC_0:          ("TSS",                     "mg/L"),
        output_enum.LinkAttribute.POLLUT_CONC_1:          ("Lead",                    "ug/L"),

        output_enum.SystemAttribute.AIR_TEMP:             ("Temperature",             "deg F"),
        output_enum.SystemAttribute.RAINFALL:             ("Rainfall",                "in/hr"),
        output_enum.SystemAttribute.SNOW_DEPTH:           ("Snow Depth",              "in"),
        output_enum.SystemAttribute.EVAP_INFIL_LOSS:      ("Evap and Infil Losses",   "in/hr"),
        output_enum.SystemAttribute.RUNOFF_FLOW:          ("Runoff Flow Rate",        "cu ft/sec"),
        output_enum.SystemAttribute.DRY_WEATHER_INFLOW:   ("Dry Weather Inflow",      "cu ft/sec"),
        output_enum.SystemAttribute.GW_INFLOW:            ("Groundwater Inflow",      "cu ft/sec"),
        output_enum.SystemAttribute.RDII_INFLOW:          ("RDII Inflow",             "cu ft/sec"),
        output_enum.SystemAttribute.DIRECT_INFLOW:        ("Direct Inflow",           "cu ft/sec"),
        output_enum.SystemAttribute.TOTAL_LATERAL_INFLOW: ("Total Lateral Inflow",    "cu ft/sec"),
        output_enum.SystemAttribute.FLOOD_LOSSES:         ("Flood Losses",            "cu ft/sec"),
        output_enum.SystemAttribute.OUTFALL_FLOWS:        ("Outfall Flow",            "cu ft/sec"),
        output_enum.SystemAttribute.VOLUME_STORED:        ("Volume Stored",           "cu ft"),
        output_enum.SystemAttribute.EVAP_RATE:            ("Evaporation Rate",        "in/day")
    }

    for attr in output_enum.SubcatchAttribute:
        temp = om.get_attribute_metadata(attr)
        assert temp == ref[attr]

    for attr in output_enum.NodeAttribute:
        temp = om.get_attribute_metadata(attr)
        assert temp == ref[attr]

    for attr in output_enum.LinkAttribute:
        temp = om.get_attribute_metadata(attr)
        assert temp == ref[attr]

    for attr in output_enum.SystemAttribute:
        temp = om.get_attribute_metadata(attr)
        assert temp == ref[attr]


def test_getversion(handle):

  assert output.getversion(handle) == 51000


def test_getprojectsize(handle):

   assert output.getprojectsize(handle) == [8, 14, 13, 1, 2]


# def test_getflowunits(handle):
#
#    assert output.getunits(handle)[0] == output.FlowUnits.CFS.value
#
#
# def test_getpollutantunits(handle):
#
#    assert output.getunits(handle)[2:] == [output.ConcUnits.MG.value, output.ConcUnits.UG.value]


def test_getstartdate(handle):

    assert output.getstartdate(handle) == 35796


def test_gettimes(handle):

    assert output.gettimes(handle, output_enum.Time.REPORT_STEP) == 3600
    assert output.gettimes(handle, output_enum.Time.NUM_PERIODS) == 36


def test_getelementname(handle):

    assert output.getelementname(handle, output_enum.ElementType.NODE, 1) == "10"


def test_getsubcatchseries(handle):

    ref_array = np.array([0.0,
                          1.2438242,
                          2.5639679,
                          4.524055,
                          2.5115132,
                          0.69808137,
                          0.040894926,
                          0.011605669,
                          0.00509294,
                          0.0027438672])

    test_array = output.getsubcatchseries(handle, 1, output_enum.SubcatchAttribute.RUNOFF_RATE, 0, 10)

    assert len(test_array) == 10
    assert np.allclose(test_array, ref_array)


def test_getsubcatchattribute(handle):

    ref_array = np.array([0.125,
                          0.125,
                          0.125,
                          0.125,
                          0.125,
                          0.225,
                          0.225,
                          0.225])

    test_array = output.getsubcatchattribute(handle, 1, output_enum.SubcatchAttribute.INFIL_LOSS)

    assert len(test_array) == 8
    assert np.allclose(test_array, ref_array)


def test_getsubcatchresult(handle):

    ref_array = np.array([0.5,
                          0.0,
                          0.0,
                          0.125,
                          1.2438242,
                          0.0,
                          0.0,
                          0.0,
                          33.481991,
                          6.6963983])

    test_array = output.getsubcatchresult(handle, 1, 1)

    assert len(test_array) == 10
    assert np.allclose(test_array, ref_array)


def test_getnoderesult(handle):

    ref_array = np.array([0.296234,
                          995.296204,
                          0.0,
                          1.302650,
                          1.302650,
                          0.0,
                          15.361463,
                          3.072293])

    test_array = output.getnoderesult(handle, 2, 2)

    assert len(test_array) == 8
    assert np.allclose(test_array, ref_array)


def test_getlinkresult(handle):

    ref_array = np.array([4.631762,
                          1.0,
                          5.8973422,
                          314.15927,
                          1.0,
                          19.070757,
                          3.8141515])

    test_array = output.getlinkresult(handle, 3, 3)

    assert len(test_array) == 7
    assert np.allclose(test_array, ref_array)


def test_getsystemresult(handle):

    ref_array = np.array([70.0,
                          0.1,
                          0.0,
                          0.19042271,
                          14.172027,
                          0.0,
                          0.0,
                          0.0,
                          0.0,
                          14.172027,
                          0.55517411,
                          13.622702,
                          2913.0793,
                          0.0])

    test_array = output.getsystemresult(handle, 4, 4)

    assert len(test_array) == 14
    assert np.allclose(test_array, ref_array)
