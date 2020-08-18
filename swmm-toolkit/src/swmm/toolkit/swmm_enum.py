#
#  output_enum.py -
#
#  Created: August 20, 2020
#  Updated:
#
#  Author:     Michael E. Tryby
#              US EPA - ORD/CESER
#              Jennifer Wu
#              Xylem Inc.


from aenum import Enum, IntEnum


class UnitSystem(Enum, start = 0):
    US
    SI


class FlowUnits(Enum, start = 0):
    CFS
    GPM
    MGD
    CMS
    LPS
    MLD


class ConcUnits(Enum, start = 0):
    MG
    UG
    COUNT
    NONE
