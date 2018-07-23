# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014 Bryant E. McDonnell
#
# Licensed under the terms of the BSD2 License
# See LICENSE.txt for details
# -----------------------------------------------------------------------------

# Local imports
import os

from swmm import toolkit as swmm

from swmm.tests.data import MODEL_NODE_INFLOWS_PATH


def test_run():
    """Testing Run"""
    prj = swmm.swmm_alloc_project()
    inp = MODEL_NODE_INFLOWS_PATH
    rpt = inp.replace('.inp', '.rpt')
    out = inp.replace('.inp', '.out')
    
    swmm.swmm_run_project(prj, inp, rpt, out)
    prj = swmm.swmm_free_project()

    #Check that rpt and out were created
    assert(os.path.isfile(rpt) == True)
    assert(os.path.isfile(out) == True)
    os.remove(rpt)
    os.remove(out)


def test_open():
    """Testing Run with disaggregated APIs"""
    prj = swmm.swmm_alloc_project()

    inp = MODEL_NODE_INFLOWS_PATH
    rpt = inp.replace('.inp', '.rpt')
    out = inp.replace('.inp', '.out')
    
    swmm.swmm_open_project(prj, inp, rpt, out)
    swmm.swmm_start_project(prj, 0)

    while True:
        elapsed_time = swmm.swmm_step_project(prj)
        if not elapsed_time:
            break
    swmm.swmm_end_project(prj)
    swmm.swmm_close_project(prj)
    
    #Check that rpt and out were created
    assert(os.path.isfile(rpt) == True)
    assert(os.path.isfile(out) == True)
    os.remove(rpt)
    os.remove(out)

if __name__ == "__main__":
    test_run()
    test_open()
