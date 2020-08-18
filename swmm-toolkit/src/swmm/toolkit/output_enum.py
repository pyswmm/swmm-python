#
#  output_enum.py -
#
#  Created: February 21, 2020
#  Updated:
#
#  Author:     Michael E. Tryby
#              US EPA - ORD/CESER
#


from aenum import Enum, IntEnum


##class UnitSystem(Enum, start = 0):
##    US
##    SI
##
##
##class FlowUnits(Enum, start = 0):
##    CFS
##    GPM
##    MGD
##    CMS
##    LPS
##    MLD
##
##
##class ConcUnits(Enum, start = 0):
##    MG
##    UG
##    COUNT
##    NONE


class ElementType(IntEnum, start = 0):
    SUBCATCH
    NODE
    LINK
    SYSTEM
    POLLUT


class Time(Enum, start = 0):
    REPORT_STEP
    NUM_PERIODS


class SubcatchAttribute(Enum, start = 0):
    RAINFALL
    SNOW_DEPTH
    EVAP_LOSS
    INFIL_LOSS
    RUNOFF_RATE
    GW_OUTFLOW_RATE
    GW_TABLE_ELEV
    SOIL_MOISTURE
    POLLUT_CONC_0


class NodeAttribute(Enum, start = 0):
    INVERT_DEPTH
    HYDRAULIC_HEAD
    PONDED_VOLUME
    LATERAL_INFLOW
    TOTAL_INFLOW
    FLOODING_LOSSES
    POLLUT_CONC_0


class LinkAttribute(Enum, start = 0):
    FLOW_RATE
    FLOW_DEPTH
    FLOW_VELOCITY
    FLOW_VOLUME
    CAPACITY
    POLLUT_CONC_0


class SystemAttribute(Enum, start = 0):
    AIR_TEMP
    RAINFALL
    SNOW_DEPTH
    EVAP_INFIL_LOSS
    RUNOFF_FLOW
    DRY_WEATHER_INFLOW
    GW_INFLOW
    RDII_INFLOW
    DIRECT_INFLOW
    TOTAL_LATERAL_INFLOW
    FLOOD_LOSSES
    OUTFALL_FLOWS
    VOLUME_STORED
    EVAP_RATE


class BaseUnits(Enum, start = 1):
    RAIN_INT
    SNOW_DEPTH
    EVAP_RATE
    INFIL_RATE
    FLOW_RATE
    ELEV
    PERCENT
    CONCEN
    HEAD
    VOLUME
    VELOCITY
    TEMP
    UNITLESS
    NONE
