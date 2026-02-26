#
#   test_output.py
#
#   Created: Aug 7, 2018
#   Updated: Apr 20, 2020
#
#   Author:  See AUTHORS
#
#   Unit testing for SWMM Output API using pytest.
#


import os

import pytest
import numpy as np

from swmm.toolkit import output, shared_enum, output_metadata


DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
OUTPUT_FILE_EXAMPLE1 = os.path.join(DATA_PATH, 'test_Example1.out')


def test_openclose():
    _handle = output.init()
    output.open(_handle, OUTPUT_FILE_EXAMPLE1)
    output.close(_handle)


def test_opencloseopenclose():
    _handle = output.init()
    output.open(_handle, OUTPUT_FILE_EXAMPLE1)
    output.close(_handle)
    _handle2 = output.init()
    output.open(_handle2, OUTPUT_FILE_EXAMPLE1)
    output.close(_handle2)


@pytest.fixture()
def handle(request):
    _handle = output.init()
    output.open(_handle, OUTPUT_FILE_EXAMPLE1)

    def close():
        output.close(_handle)

    request.addfinalizer(close)
    return _handle


def test_getversion(handle):

  assert output.get_version(handle) == 51000


def test_getprojectsize(handle):

   assert output.get_proj_size(handle) == [8, 14, 13, 1, 2]


# def test_getflowunits(handle):
#
#    assert output.getunits(handle)[0] == output.FlowUnits.CFS.value
#
#
# def test_getpollutantunits(handle):
#
#    assert output.getunits(handle)[2:] == [output.ConcUnits.MG.value, output.ConcUnits.UG.value]


def test_getstartdate(handle):

    assert output.get_start_date(handle) == 35796


def test_gettimes(handle):

    assert output.get_times(handle, shared_enum.Time.REPORT_STEP) == 3600
    assert output.get_times(handle, shared_enum.Time.NUM_PERIODS) == 36


def test_getelementname(handle):

    assert output.get_elem_name(handle, shared_enum.ElementType.NODE, 1) == "10"



def test_getdatetime(handle):
    date0 = output.get_date_time(handle, 0)
    date1 = output.get_date_time(handle, 1)
    assert isinstance(date0, (float, np.floating))

    step_seconds = output.get_times(handle, shared_enum.Time.REPORT_STEP)
    step_days = step_seconds / 86400.0

    # consecutive timestamps differ by exactly one report step (in days)
    assert np.isclose(date1 - date0, step_days)

    # first timestamp should be strictly after the saved start date anchor
    assert date0 > output.get_start_date(handle)


def test_getdateseries(handle):
    start, end = 0, 5
    dates = output.get_date_series(handle, start, end)

    assert len(dates) == end - start + 1

    step_days = output.get_times(handle, shared_enum.Time.REPORT_STEP) / 86400.0
    diffs = np.diff(dates)

    # monotonic and evenly spaced by report step
    assert np.allclose(diffs, step_days)
    assert np.isclose(dates[-1], dates[0] + (end - start) * step_days)


def test_decodedate(handle):
    # decoded components are plausible
    date0 = output.get_date_time(handle, 0)
    y, m, d, hh, mm, ss, dow = output.decode_date(date0)

    assert 1 <= m <= 12
    assert 1 <= d <= 31
    assert 0 <= hh <= 23
    assert 0 <= mm <= 59
    assert 0 <= ss <= 59
    assert 1 <= dow <= 7

    # consecutive decode respects the report step
    date1 = output.get_date_time(handle, 1)
    y1, m1, d1, hh1, mm1, ss1, dow1 = output.decode_date(date1)

    step_seconds = output.get_times(handle, shared_enum.Time.REPORT_STEP)
    step_hours = (step_seconds // 3600) % 24

    # minutes/seconds remain constant for steps divisible by 60s
    if step_seconds % 60 == 0:
        assert mm1 == mm
        assert ss1 == ss

    # hour advances by step_hours modulo 24 (day rollover allowed)
    assert ((hh1 - hh) % 24) == step_hours



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
                          0.0027438672,
                          0.0016718778])

    test_array = output.get_subcatch_series(handle, 1, shared_enum.SubcatchAttribute.RUNOFF_RATE, 0, 10)

    assert len(test_array) == 11
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

    test_array = output.get_subcatch_attribute(handle, 1, shared_enum.SubcatchAttribute.INFIL_LOSS)

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

    test_array = output.get_subcatch_result(handle, 1, 1)

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

    test_array = output.get_node_result(handle, 2, 2)

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

    test_array = output.get_link_result(handle, 3, 3)

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

    test_array = output.get_system_result(handle, 4, 4)

    assert len(test_array) == 14
    assert np.allclose(test_array, ref_array)

def test_getsystemattribute(handle):

    ref_array = np.array([70.0])

    test_array = output.get_system_attribute(handle, 0, shared_enum.SystemAttribute.AIR_TEMP)

    assert len(test_array) == 1
    assert np.allclose(test_array, ref_array)
