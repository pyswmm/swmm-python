#
#   test_output.py
#
#   Created: 8/7/2018
#   Author: Michael E. Tryby
#           US EPA - ORD/NRMRL
#
#   Unit testing for SWMM Output API using pytest.
#

import pytest
import numpy as np

from swmm.output import output as smo

from data import OUTPUT_FILE_EXAMPLE1


def test_openclose():
    _handle = smo.init()
    smo.open(_handle, OUTPUT_FILE_EXAMPLE1)
    smo.close(_handle)

    
@pytest.fixture()
def handle(request):    
    _handle = smo.init()
    smo.open(_handle, OUTPUT_FILE_EXAMPLE1)
    
    def close():
        smo.close(_handle)
    
    request.addfinalizer(close)    
    return _handle    


def test_getversion(handle):
  
  assert smo.getversion(handle) == 51000


def test_getprojectsize(handle):
    
    assert smo.getprojectsize(handle) == [8, 14, 13, 2]


def test_getpollutantunits(handle):
    
    assert smo.getpollutantunits(handle) == [0, 1]
    

def test_getstartdate(handle):
    
    assert smo.getstartdate(handle) == 35796
    

def test_gettimes(handle):
    
    assert smo.gettimes(handle, smo.Time.NUM_PERIODS) == 36


def test_getelementname(handle):
    
    assert smo.getelementname(handle, smo.ElementType.NODE, 1) == "10"
    

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
                                
    test_array = smo.getsubcatchseries(handle, 1, smo.SubcatchAttribute.RUNOFF_RATE, 0, 10)  
    
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
    
    test_array = smo.getsubcatchattribute(handle, 1, smo.SubcatchAttribute.INFIL_LOSS)

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
    
    test_array = smo.getsubcatchresult(handle, 1, 1)
    
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

    test_array = smo.getnoderesult(handle, 2, 2)
    
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

    test_array = smo.getlinkresult(handle, 3, 3)
    
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

    test_array = smo.getsystemresult(handle, 4, 4)
    
    assert len(test_array) == 14
    assert np.allclose(test_array, ref_array)
    