

import os
from string import Template

import pytest

from swmm.toolkit import solver as smtk
from swmm.toolkit import output as smo


DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
INPUT_FILE_EXAMPLE_N = os.path.join(DATA_PATH, 'Example6.inp')
REPORT_FILE_TEST = os.path.join(DATA_PATH, 'test.rpt')
OUTPUT_FILE_TEST = os.path.join(DATA_PATH, 'test.out')


def test_integrated():

    for i in range(1,6):
        template = Template('Example$N.inp')
        example = template.substitute(N = i)
        example_n = os.path.join(DATA_PATH, example)

        #handle = smtk.alloc_project()
        #smtk.open(handle, INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)

        smtk.run(example_n, REPORT_FILE_TEST, OUTPUT_FILE_TEST)

        #smtk.report(handle)
        massbal = smtk.get_mass_bal_err()

        #smtk.close(handle)
        #smtk.free_project(handle)


        _handle = smo.init()
        smo.open(_handle, OUTPUT_FILE_TEST)
        ver = smo.get_version(_handle)
        size = smo.get_proj_size(_handle)
        units = smo.get_units(_handle)
        smo.close(_handle)


def test_opencloseopenclose():
    smtk.run(INPUT_FILE_EXAMPLE_N, REPORT_FILE_TEST, OUTPUT_FILE_TEST)

    handle_1 = smo.init()
    smo.open(handle_1, OUTPUT_FILE_TEST)
    smo.close(handle_1)
    handle_2 = smo.init()
    smo.open(handle_2, OUTPUT_FILE_TEST)
    smo.close(handle_2)
