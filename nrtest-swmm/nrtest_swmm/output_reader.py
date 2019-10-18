# -*- coding: utf-8 -*-

#
#  output_reader.py
#
#  Date Created: 11/14/2017
#  Date Modified: 10/17/2019
#
#  Author:       Michael E. Tryby
#                US EPA - ORD/NRMRL
#
'''
The module output_reader provides the class used to implement the output
generator.
'''

# project import
from swmm.output import output as oapi


def output_generator(path_ref):
    '''
    The output_generator is designed to iterate over a swmm binary file and
    yield element results. It is useful for comparing contents of binary files
    for numerical regression testing.

    The generator yields a numpy array containing the SWMM element result.

    Arguments:
        path_ref - path to result file

    Raises:
        SWMM_OutputReaderError()
        ...
    '''

    with OutputReader(path_ref) as sor:

        for period_index in range(0, sor.report_periods()):
            for element_type in oapi.ElementType:
                for element_index in range(0, sor.element_count(element_type)):

                    yield (sor.element_result(element_type, period_index, element_index),
                            (element_type, period_index, element_index))


class OutputReader():
    '''
    Provides minimal interface needed to implement the SWMM output generator.
    '''

    def __init__(self, filename):
        self.filepath = filename
        self.handle = None
        self.count = None
        self.get_element_result = {
            oapi.ElementType.SUBCATCH: oapi.getsubcatchresult,
            oapi.ElementType.NODE: oapi.getnoderesult,
            oapi.ElementType.LINK: oapi.getlinkresult,
            oapi.ElementType.SYSTEM: oapi.getsystemresult
        }

    def __enter__(self):
        self.handle = oapi.init()
        oapi.open(self.handle, self.filepath)
        self.count = oapi.getprojectsize(self.handle)
        return self

    def __exit__(self, type, value, traceback):
        oapi.close(self.handle)

    def report_periods(self):
        return oapi.gettimes(self.handle, oapi.Time.NUM_PERIODS)

    def element_count(self, element_type):
        return self.count[element_type.value]

    def element_result(self, element_type, time_index, element_index):
        return self.get_element_result[element_type](self.handle, time_index, element_index)
