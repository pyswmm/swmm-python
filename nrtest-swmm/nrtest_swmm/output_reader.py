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

# system import
from itertools import islice

# project import
from swmm.toolkit import output, shared_enum


def output_generator(path_ref):
    '''
    The output_generator is designed to iterate over a swmm binary file and
    yield element results. It is useful for comparing contents of binary files
    for numerical regression testing.

    The generator yields a list containing the SWMM element result.

    Arguments:
        path_ref - path to result file

    Raises:
        SWMM_OutputReaderError()
        ...
    '''

    with OutputReader(path_ref) as reader:

        for period_index in range(0, reader.report_periods()):
            for element_type in islice(shared_enum.ElementType, 4):
                for element_index in range(0, reader.element_count(element_type)):

                    yield (reader.element_result(element_type, period_index, element_index),
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
            shared_enum.ElementType.SUBCATCH: output.get_subcatch_result,
            shared_enum.ElementType.NODE: output.get_node_result,
            shared_enum.ElementType.LINK: output.get_link_result,
            shared_enum.ElementType.SYSTEM: output.get_system_result
        }

    def __enter__(self):
        self.handle = output.init()
        output.open(self.handle, self.filepath)
        self.count = output.get_proj_size(self.handle)
        return self

    def __exit__(self, type, value, traceback):
        output.close(self.handle)

    def report_periods(self):
        return output.get_times(self.handle, shared_enum.Time.NUM_PERIODS)

    def element_count(self, element_type):
        return self.count[element_type]

    def element_result(self, element_type, time_index, element_index):
        return self.get_element_result[element_type](self.handle, time_index, element_index)
