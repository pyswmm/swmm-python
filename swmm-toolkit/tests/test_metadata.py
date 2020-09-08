
#
#   test_metadata.py
#
#   Created:  Apr 8, 2020
#   Modified: Apr 20, 2020
#
#   Author: Michael E. Tryby
#           US EPA - ORD/CESER
#
#   Unit testing for SWMM output metadata using pytest.
#


import os

import pytest

from swmm.toolkit import output, toolkit_enum, output_metadata


DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
OUTPUT_FILE_EXAMPLE1 = os.path.join(DATA_PATH, 'test_Example1.out')


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
        toolkit_enum.SubcatchAttribute.RAINFALL:           ("Rainfall",                "in/hr"),
        toolkit_enum.SubcatchAttribute.SNOW_DEPTH:         ("Snow Depth",              "in"),
        toolkit_enum.SubcatchAttribute.EVAP_LOSS:          ("Evaporation Loss",        "in/day"),
        toolkit_enum.SubcatchAttribute.INFIL_LOSS:         ("Infiltration Loss",       "in/hr"),
        toolkit_enum.SubcatchAttribute.RUNOFF_RATE:        ("Runoff Rate",             "cu ft/sec"),
        toolkit_enum.SubcatchAttribute.GW_OUTFLOW_RATE:    ("Groundwater Flow Rate",   "cu ft/sec"),
        toolkit_enum.SubcatchAttribute.GW_TABLE_ELEV:      ("Groundwater Elevation",   "ft"),
        toolkit_enum.SubcatchAttribute.SOIL_MOISTURE:      ("Soil Moisture",           "%"),
        toolkit_enum.SubcatchAttribute.POLLUT_CONC_0:      ("TSS",                     "mg/L"),
        toolkit_enum.SubcatchAttribute.POLLUT_CONC_1:      ("Lead",                    "ug/L"),

        toolkit_enum.NodeAttribute.INVERT_DEPTH:           ("Invert Depth",            "ft"),
        toolkit_enum.NodeAttribute.HYDRAULIC_HEAD:         ("Hydraulic Head",          "ft"),
        toolkit_enum.NodeAttribute.PONDED_VOLUME:          ("Ponded Volume",           "cu ft"),
        toolkit_enum.NodeAttribute.LATERAL_INFLOW:         ("Lateral Inflow",          "cu ft/sec"),
        toolkit_enum.NodeAttribute.TOTAL_INFLOW:           ("Total Inflow",            "cu ft/sec"),
        toolkit_enum.NodeAttribute.FLOODING_LOSSES:        ("Flooding Loss",           "cu ft/sec"),
        toolkit_enum.NodeAttribute.POLLUT_CONC_0:          ("TSS",                     "mg/L"),
        toolkit_enum.NodeAttribute.POLLUT_CONC_1:          ("Lead",                    "ug/L"),

        toolkit_enum.LinkAttribute.FLOW_RATE:              ("Flow Rate",               "cu ft/sec"),
        toolkit_enum.LinkAttribute.FLOW_DEPTH:             ("Flow Depth",              "ft"),
        toolkit_enum.LinkAttribute.FLOW_VELOCITY:          ("Flow Velocity",           "ft/sec"),
        toolkit_enum.LinkAttribute.FLOW_VOLUME:            ("Flow Volume",             "cu ft"),
        toolkit_enum.LinkAttribute.CAPACITY:               ("Capacity",                "%"),
        toolkit_enum.LinkAttribute.POLLUT_CONC_0:          ("TSS",                     "mg/L"),
        toolkit_enum.LinkAttribute.POLLUT_CONC_1:          ("Lead",                    "ug/L"),

        toolkit_enum.SystemAttribute.AIR_TEMP:             ("Temperature",             "deg F"),
        toolkit_enum.SystemAttribute.RAINFALL:             ("Rainfall",                "in/hr"),
        toolkit_enum.SystemAttribute.SNOW_DEPTH:           ("Snow Depth",              "in"),
        toolkit_enum.SystemAttribute.EVAP_INFIL_LOSS:      ("Evap and Infil Losses",   "in/hr"),
        toolkit_enum.SystemAttribute.RUNOFF_FLOW:          ("Runoff Flow Rate",        "cu ft/sec"),
        toolkit_enum.SystemAttribute.DRY_WEATHER_INFLOW:   ("Dry Weather Inflow",      "cu ft/sec"),
        toolkit_enum.SystemAttribute.GW_INFLOW:            ("Groundwater Inflow",      "cu ft/sec"),
        toolkit_enum.SystemAttribute.RDII_INFLOW:          ("RDII Inflow",             "cu ft/sec"),
        toolkit_enum.SystemAttribute.DIRECT_INFLOW:        ("Direct Inflow",           "cu ft/sec"),
        toolkit_enum.SystemAttribute.TOTAL_LATERAL_INFLOW: ("Total Lateral Inflow",    "cu ft/sec"),
        toolkit_enum.SystemAttribute.FLOOD_LOSSES:         ("Flood Losses",            "cu ft/sec"),
        toolkit_enum.SystemAttribute.OUTFALL_FLOWS:        ("Outfall Flow",            "cu ft/sec"),
        toolkit_enum.SystemAttribute.VOLUME_STORED:        ("Volume Stored",           "cu ft"),
        toolkit_enum.SystemAttribute.EVAP_RATE:            ("Evaporation Rate",        "in/day")
    }

    for attr in toolkit_enum.SubcatchAttribute:
        temp = om.get_attribute_metadata(attr)
        assert temp == ref[attr]

    for attr in toolkit_enum.NodeAttribute:
        temp = om.get_attribute_metadata(attr)
        assert temp == ref[attr]

    for attr in toolkit_enum.LinkAttribute:
        temp = om.get_attribute_metadata(attr)
        assert temp == ref[attr]

    for attr in toolkit_enum.SystemAttribute:
        temp = om.get_attribute_metadata(attr)
        assert temp == ref[attr]
