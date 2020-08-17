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

from swmm.toolkit import solver

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


def test_open_api_funcs():
    solver.open(INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)
    simulation_unit_option = solver.swmm_getSimulationUnit(0)
    solver.close()
