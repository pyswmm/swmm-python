

import os
from string import Template

import pytest

from swmm.toolkit import toolkit as smtk
from swmm.output import output as smo


DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
INPUT_FILE_EXAMPLE_N = os.path.join(DATA_PATH, 'Example6.inp')
REPORT_FILE_TEST = os.path.join(DATA_PATH, 'test.rpt')
OUTPUT_FILE_TEST = os.path.join(DATA_PATH, 'test.out')


def test_integrated():

    for i in range(1,6):
        template = Template('Example$N.inp')
        example = template.substitute(N = i)
        example_n = os.path.join(DATA_PATH, example)

        handle = smtk.alloc_project()
        #smtk.open(handle, INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)

        smtk.run(handle, example_n, REPORT_FILE_TEST, OUTPUT_FILE_TEST)

        #smtk.report(handle)
        massbal = smtk.getmassbalerr(handle)

        #smtk.close(handle)
        smtk.free_project(handle)


        _handle = smo.init()
        smo.open(_handle, OUTPUT_FILE_TEST)
        size = smo.getprojectsize(_handle)
        units = smo.getunits(_handle)
        smo.close(_handle)
