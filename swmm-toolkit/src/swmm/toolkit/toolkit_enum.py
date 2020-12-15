#
#  output_enum.py -
#
#  Created:   February 21, 2020
#  Updated:
#
#  Author:    See AUTHORS
#

from aenum import Enum, IntEnum


class UnitSystem(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~US`
    :attr:`~SI`
    ================ =================
    """
    US
    SI


class FlowUnits(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~CFS`
    :attr:`~GPM`
    :attr:`~MGD`
    :attr:`~CMS`
    :attr:`~LPS`
    :attr:`~MLD`
    ================ =================
    """
    CFS
    GPM
    MGD
    CMS
    LPS
    MLD


class ConcUnits(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~MG`
    :attr:`~UG`
    :attr:`~COUNT`
    :attr:`~NONE`
    ================ =================
    """
    MG,
    UG,
    COUNT
    NONE


class ObjectType(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ==================== ==============
    :attr:`~GAGE`
    :attr:`~SUBCATCH`
    :attr:`~NODE`
    :attr:`~LINK`
    :attr:`~POLLUT`
    :attr:`~LANDUSE`
    :attr:`~TIMEPATTERN`
    :attr:`~CURVE`
    :attr:`~TSERIES`
    :attr:`~CONTROL`
    :attr:`~TRANSECT`
    :attr:`~AQUIFER`
    :attr:`~UNITHYD`
    :attr:`~SNOWMELT`
    :attr:`~SHAPE`
    :attr:`~LID`
    ==================== ==============
    """
    GAGE
    SUBCATCH
    NODE
    LINK
    POLLUT
    LANDUSE
    TIMEPATTERN
    CURVE
    TSERIES
    CONTROL
    TRANSECT
    AQUIFER
    UNITHYD
    SNOWMELT
    SHAPE
    LID


class NodeType(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================= =================
    :attr:`~JUNCTION`
    :attr:`~OUTFALL`
    :attr:`~STORAGE`
    :attr:`~DIVIDER`
    ================= =================
    """
    JUNCTION
    OUTFALL
    STORAGE
    DIVIDER


class LinkType(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~CONDUIT`
    :attr:`~PUMP`
    :attr:`~ORIFACE`
    :attr:`~WEIR`
    :attr:`~OUTLET`
    ================ =================
    """
    CONDUIT
    PUMP
    ORIFICE
    WEIR
    OUTLET


class LinkDirection(Enum):
    """
    .. ruberic:: Enum Members

    =============================== ===
    :attr:`~UPSTREAM_TO_DOWNSTREAM`
    :attr:`~DOWNSTREAM_TO_UPSTREAM`
    =============================== ===
    """
    UPSTREAM_TO_DOWNSTREAM = 1
    DOWNSTREAM_TO_UPSTREAM = -1
    

class ElementType(IntEnum, start = 0):
    """
    .. ruberic:: Enum Members

    ================= =================
    :attr:`~SUBCATCH`
    :attr:`~NODE`
    :attr:`~LINK`
    :attr:`~SYSTEM`
    :attr:`~POLLUT`
    ================= =================
    """
    SUBCATCH
    NODE
    LINK
    SYSTEM
    POLLUT


class Time(Enum, start = 0):
    """
    .. ruberic:: Enum Members

    ==================== ==============
    :attr:`~REPORT_STEP`
    :attr:`~NUM_PERIODS`
    ==================== ==============
    """
    REPORT_STEP
    NUM_PERIODS


class SubcatchAttribute(Enum, start = 0):
    """
    .. ruberic:: Enum Members

    ========================= =========
    :attr:`~RAINFALL`
    :attr:`~SNOW_DEPTH`
    :attr:`~EVAP_LOSS`
    :attr:`~INFIL_LOSS`
    :attr:`~RUNOFF_RATE`
    :attr:`~GW_OUTFLOW_RATE`
    :attr:`~GW_TABLE_ELEV`
    :attr:`~SOIL_MOISTURE`
    :attr:`~POLLUT_CONC_0`
    ======================== ==========
    """    
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
    """
    .. ruberic:: Enum Members

    ========================= =========
    :attr:`~INVERT_DEPTH`
    :attr:`~HYDRAULIC_HEAD`
    :attr:`~PONDED_VOLUME`
    :attr:`~LATERAL_INFLOW`
    :attr:`~TOTAL_INFLOW`
    :attr:`~FLOODING_LOSSES`
    :attr:`~POLLUT_CONC_0`
    ======================== ==========
    """
    INVERT_DEPTH
    HYDRAULIC_HEAD
    PONDED_VOLUME
    LATERAL_INFLOW
    TOTAL_INFLOW
    FLOODING_LOSSES
    POLLUT_CONC_0


class LinkAttribute(Enum, start = 0):
    """
    .. ruberic:: Enum Members

    ====================== ============
    :attr:`~FLOW_RATE`
    :attr:`~FLOW_DEPTH`
    :attr:`~FLOW_VELOCITY`
    :attr:`~FLOW_VOLUME`
    :attr:`~CAPACITY`
    :attr:`~POLLUT_CONC_0`
    ====================== ============
    """
    FLOW_RATE
    FLOW_DEPTH
    FLOW_VELOCITY
    FLOW_VOLUME
    CAPACITY
    POLLUT_CONC_0


class SystemAttribute(Enum, start = 0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~AIR_TEMP`
    :attr:`~RAINFALL`
    :attr:`~SNOW_DEPTH`
    :attr:`~EVAP_INFIL_LOSS`
    :attr:`~RUNOFF_FLOW`
    :attr:`~DRY_WEATHER_INFLOW`
    :attr:`~GW_INFLOW`
    :attr:`~RDII_INFLOW`
    :attr:`~DIRECT_INFLOW`
    :attr:`~TOTAL_LATERAL_INFLOW`
    :attr:`~FLOOD_LOSSES`
    :attr:`~OUTFALL_FLOWS`
    :attr:`~VOLUME_STORED`
    :attr:`~EVAP_RATE`
    ================ =================
    """
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
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~RAIN_INT`
    :attr:`~SNOW_DEPTH`
    :attr:`~EVAP_RATE`
    :attr:`~INFIL_RATE`
    :attr:`~FLOW_RATE`
    :attr:`~ELEV`
    :attr:`~PERCENT`
    :attr:`~CONCEN`
    :attr:`~HEAD`
    :attr:`~VOLUME`
    :attr:`~VELOCITY`
    :attr:`~TEMP`
    :attr:`~UNITLESS`
    :attr:`~NONE`
    ================ =================
    """
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


#
# Solver Toolkit API Enums
#    
class TimeProperty(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~START_DATE`
    :attr:`~END_DATE`
    :attr:`~REPORT_DATE`
    ================ =================
    """
    START_DATE
    END_DATE
    REPORT_DATE


class UnitProperty(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~SYSTEM_UNIT`
    :attr:`~FLOW_UNIT`
    ================ =================
    """
    SYSTEM_UNIT
    FLOW_UNIT


class SimOption(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~ALLOW_POND`
    :attr:`~SKIP_STEADY`
    :attr:`~IGNORE_RAIN`
    :attr:`~IGNORE_RDII`
    :attr:`~IGNORE_SNOW`
    :attr:`~IGNORE_GW`
    :attr:`~IGNORE_ROUTE`
    :attr:`~IGNORE_ROUTE_QUALITY`
    ================ =================
    """
    ALLOW_POND
    SKIP_STEADY
    IGNORE_RAIN
    IGNORE_RDII
    IGNORE_SNOW
    IGNORE_GW
    IGNORE_ROUTE
    IGNORE_ROUTE_QUALITY


class SimSetting(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~ROUTE_STEP`
    :attr:`~MIN_ROUTE_STEP`
    :attr:`~LENGTH_STEP`
    :attr:`~START_DRY_DAYS`
    :attr:`~COURANT_FACTOR`
    :attr:`~MIN_SURFACE_AREA`
    :attr:`~MIN_SLOPE`
    :attr:`~RUNOFF_ERROR`
    :attr:`~GW_ERROR`
    :attr:`~FLOW_ERROR`
    :attr:`~QUALITY_ERROR`
    :attr:`~HEAD_TOLERANCE`
    :attr:`~SYSTEM_FLOW_TOLERANCE`
    :attr:`~LATERAL_FLOW_TOLERANCE`
    ================ =================
    """
    ROUTE_STEP
    MIN_ROUTE_STEP
    LENGTH_STEP
    START_DRY_DAYS
    COURANT_FACTOR
    MIN_SURFACE_AREA
    MIN_SLOPE
    RUNOFF_ERROR
    GW_ERROR
    FLOW_ERROR
    QUALITY_ERROR
    HEAD_TOLERANCE
    SYSTEM_FLOW_TOLERANCE
    LATERAL_FLOW_TOLERANCE


class NodeProperty(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~INVERT_ELEVATION`
    :attr:`~FULL_DEPTH`
    :attr:`~SURCHARGE_DEPTH`
    :attr:`~POND_AREA`
    :attr:`~INITIAL_DEPTH`
    ================ =================
    """
    INVERT_ELEVATION
    FULL_DEPTH
    SURCHARGE_DEPTH
    POND_AREA
    INITIAL_DEPTH


class NodeResult(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~TOTAL_INFLOW`
    :attr:`~TOTAL_OUTFLOW`
    :attr:`~LOSSES`
    :attr:`~VOLUME`
    :attr:`~FLOOD`
    :attr:`~DEPTH`
    :attr:`~HEAD`
    :attr:`~LATERAL_INFLOW`
    ================ =================
    """
    TOTAL_INFLOW
    TOTAL_OUTFLOW
    LOSSES
    VOLUME
    FLOOD
    DEPTH
    HEAD
    LATERAL_INFLOW


class NodePollutant(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~QUALITY`
    ================ =================
    """
    QUALITY


class LinkProperty(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~OFFSET_1`
    :attr:`~OFFSET_2`
    :attr:`~INITIAL_FLOW`
    :attr:`~FLOW_LIMIT`
    :attr:`~INLET_LOSS`
    :attr:`~OUTLET_LOSS`
    :attr:`~AVERAGE_LOSS`
    ================ =================
    """
    OFFSET_1
    OFFSET_2
    INITIAL_FLOW
    FLOW_LIMIT
    INLET_LOSS
    OUTLET_LOSS
    AVERAGE_LOSS


class LinkResult(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~FLOW`
    :attr:`~DEPTH`
    :attr:`~VOLUME`
    :attr:`~US_SURFACE_AREA`
    :attr:`~DS_SURFACE_AREA`
    :attr:`~SETTING`
    :attr:`~TARGET_SETTING`
    :attr:`~FROUDE`
    ================ =================
    """
    FLOW
    DEPTH
    VOLUME
    US_SURFACE_AREA
    DS_SURFACE_AREA
    SETTING
    TARGET_SETTING
    FROUDE


class LinkPollutant(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~QUALITY`
    :attr:`~TOTAL_LOAD`
    ================ =================
    """
    QUALITY
    TOTAL_LOAD

    
class SubcatchProperty(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~WIDTH`
    :attr:`~AREA`
    :attr:`~IMPERVIOUS_FRACTION`
    :attr:`~SLOPE`
    :attr:`~CURB_LENGTH`
    ================ =================
    """
    WIDTH
    AREA
    IMPERVIOUS_FRACTION
    SLOPE
    CURB_LENGTH


class SubcatchResult(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~RAIN`
    :attr:`~EVAPORATION`
    :attr:`~INFILTRATION`
    :attr:`~RUNON`
    :attr:`~RUNOFF`
    :attr:`~SNOW`
    ================ =================
    """
    RAIN
    EVAPORATION
    INFILTRATION
    RUNON
    RUNOFF
    SNOW


class SubcatchPollutant(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~BUILD_UP`
    :attr:`~CONCENTRATION`
    :attr:`~QUALITY`
    :attr:`~TOTAL_LOAD`
    ================ =================
    """
    BUILD_UP
    CONCENTRATION
    QUALITY
    TOTAL_LOAD

    
class LidUsageProperty(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~UNIT_AREA`
    :attr:`~TOP_WIDTH`
    :attr:`~BOTTOM_WIDTH`
    :attr:`~INITIAL_SATURATION`
    :attr:`~FROM_IMPERVIOUS`
    :attr:`~FROM_PERVIOUS`
    ================ =================
    """
    UNIT_AREA
    TOP_WIDTH
    BOTTOM_WIDTH
    INITIAL_SATURATION
    FROM_IMPERVIOUS
    FROM_PERVIOUS


class LidUsageOption(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~INDEX`
    :attr:`~NUMBER`
    :attr:`~TO_PERV`
    :attr:`~DRAIN_SUBCATCH`
    :attr:`~DRAIN_NODE`
    ================ =================
    """
    INDEX
    NUMBER
    TO_PERV
    DRAIN_SUBCATCH
    DRAIN_NODE


class LidLayer(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~SURFACE`
    :attr:`~SOIL`
    :attr:`~STORAGE`
    :attr:`~PAVEMENT`
    :attr:`~DRAIN`
    :attr:`~DRAIN_MAT`
    ================ =================
    """
    SURFACE
    SOIL
    STORAGE
    PAVEMENT
    DRAIN
    DRAIN_MAT

    
class LidLayerProperty(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~THICKNESS`
    :attr:`~VOID_FRACTION`
    :attr:`~ROUGHNESS`
    :attr:`~SURFACE_SLOPE`
    :attr:`~SIDE_SLOP`
    :attr:`~ALPHA`
    :attr:`~POROSITY`
    :attr:`~FIELD_CAPACITY`
    :attr:`~WILTING_POINT`
    :attr:`~SUCTION_HEAD`
    :attr:`~K_SATURATION`
    :attr:`~K_SLOPE`
    :attr:`~CLOG_FACTOR`
    :attr:`~IMPERVIOUS_FRACTION`
    :attr:`~DRAIN_COEFFICIENT`
    :attr:`~DRAIN_EXPONENT`
    :attr:`~DRAIN_OFFSET`
    :attr:`~DRAIN_DELAY`
    :attr:`~DRAIN_HEAD_OPEN`
    :attr:`~DRAIN_HEAD_CLOSE`
    :attr:`~DRAIN_CURVE`
    :attr:`~DRAIN_REGEN_DAYS`
    :attr:`~DRAIN_REGEN_DEGREE`
    ================ =================
    """
    THICKNESS
    VOID_FRACTION
    ROUGHNESS
    SURFACE_SLOPE
    SIDE_SLOP
    ALPHA
    POROSITY
    FIELD_CAPACITY
    WILTING_POINT
    SUCTION_HEAD
    K_SATURATION
    K_SLOPE
    CLOG_FACTOR
    IMPERVIOUS_FRACTION
    DRAIN_COEFFICIENT
    DRAIN_EXPONENT
    DRAIN_OFFSET
    DRAIN_DELAY
    DRAIN_HEAD_OPEN
    DRAIN_HEAD_CLOSE
    DRAIN_CURVE
    DRAIN_REGEN_DAYS
    DRAIN_REGEN_DEGREE


class LidResult(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~INFLOW`
    :attr:`~EVAPORATION`
    :attr:`~INFILTRATION`
    :attr:`~SURFACE_FLOW`
    :attr:`~DRAIN_FLOW`
    :attr:`~INITIAL_VOLUME`
    :attr:`~FINAL_VOLUME`
    :attr:`~SURFACE_DEPTH`
    :attr:`~PAVEMENT_DEPTH`
    :attr:`~SOIL_MOISTURE`
    :attr:`~STORAGE_DEPTH`
    :attr:`~DRY_TIME`
    :attr:`~OLD_DRAIN_FLOW`
    :attr:`~NEW_DRAIN_FLOW`
    :attr:`~PERVIOUS_AREA`
    :attr:`~FLOW_TO_PERVIOUS_AREA`
    :attr:`~EVAPORATE_RATE`
    :attr:`~NATIVE_INFILTRATION`
    :attr:`~SURFACE_INFLOW`
    :attr:`~SURFACE_INFILTRATION`
    :attr:`~SURFACE_EVAPORATION`
    :attr:`~SURFACE_OUTFLOW`
    :attr:`~PAVEMENT_EVAPORATION`
    :attr:`~PAVEMENT_PERCOLATION`
    :attr:`~SOIL_EVAPORATION`
    :attr:`~SOIL_PERCOLATION`
    :attr:`~STORAGE_INFLOW`
    :attr:`~STORAGE_EXFILTRATION`
    :attr:`~STORAGE_EVAPORATION`
    :attr:`~STORAGE_DRAIN`
    ================ =================
    """
    INFLOW
    EVAPORATION
    INFILTRATION
    SURFACE_FLOW
    DRAIN_FLOW
    INITIAL_VOLUME
    FINAL_VOLUME
    SURFACE_DEPTH
    PAVEMENT_DEPTH
    SOIL_MOISTURE
    STORAGE_DEPTH
    DRY_TIME
    OLD_DRAIN_FLOW
    NEW_DRAIN_FLOW
    PERVIOUS_AREA
    FLOW_TO_PERVIOUS_AREA
    EVAPORATE_RATE
    NATIVE_INFILTRATION
    SURFACE_INFLOW
    SURFACE_INFILTRATION
    SURFACE_EVAPORATION
    SURFACE_OUTFLOW
    PAVEMENT_EVAPORATION
    PAVEMENT_PERCOLATION
    SOIL_EVAPORATION
    SOIL_PERCOLATION
    STORAGE_INFLOW
    STORAGE_EXFILTRATION
    STORAGE_EVAPORATION
    STORAGE_DRAIN

    
class RainResult(Enum, start=0):
    """
    .. ruberic:: Enum Members

    ================ =================
    :attr:`~TOTAL`
    :attr:`~RAINFALL`
    :attr:`~SNOWFALL`
    ================ =================
    """
    TOTAL
    RAINFALL
    SNOWFALL
