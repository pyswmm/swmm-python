#
#  shared_enum.py -
#
#  Created:   February 21, 2020
#  Updated:
#
#  Author:    See AUTHORS
#

from aenum import Enum, IntEnum


class UnitSystem(Enum, start=0):
    """SWMM Unit System enum class. 

    .. rubric:: Enum Members

    ================ ====================
    :attr:`~US`      US Traditional units
    :attr:`~SI`      SI (metric) units
    ================ ====================
    """
    US
    SI


class FlowUnits(Enum, start=0):
    """SWMM Flow Units enum class.

    .. rubric:: Enum Members

    ================ =======================
    :attr:`~CFS`     cubic feet per second
    :attr:`~GPM`     gallons per minute
    :attr:`~MGD`     million gallons per day
    :attr:`~CMS`     cubic meters per second
    :attr:`~LPS`     liters per second
    :attr:`~MLD`     million liters per day
    ================ =======================
    """
    CFS
    GPM
    MGD
    CMS
    LPS
    MLD


class ConcUnits(Enum, start=0):
    """SWMM Concentration Units enum class.

    .. rubric:: Enum Members

    ================ ====================
    :attr:`~MG`      Milligrams per liter
    :attr:`~UG`      Micrograms per liter
    :attr:`~COUNT`   Counts per liter
    :attr:`~NONE`    None
    ================ ====================
    """
    MG,
    UG,
    COUNT
    NONE


class BaseUnits(Enum, start = 1):
    """Base Units enum class

    .. rubric:: Enum Members

    =================== ==================
    :attr:`~RAIN_INT`   rainfall intensity
    :attr:`~SNOW_DEPTH` rainfall depth  
    :attr:`~EVAP_RATE`  evaporation rate
    :attr:`~INFIL_RATE` infiltration rate
    :attr:`~FLOW_RATE`  flow rate
    :attr:`~ELEV`       elevation
    :attr:`~PERCENT`    percent
    :attr:`~CONCEN`     concentration
    :attr:`~HEAD`       head
    :attr:`~VOLUME`     volume
    :attr:`~VELOCITY`   velocity
    :attr:`~TEMP`       temperature
    :attr:`~UNITLESS`   unitless quantity
    :attr:`~NONE`       none
    =================== ==================
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


class ObjectType(Enum, start=0):
    """SWMM Object Types enum class.

    .. rubric:: Enum Members

    ==================== ===============================
    :attr:`~GAGE`        rain gage 
    :attr:`~SUBCATCH`    subcatchment
    :attr:`~NODE`        conveyance system node
    :attr:`~LINK`        conveyance system link
    :attr:`~POLLUT`      pollutant
    :attr:`~LANDUSE`     land use category
    :attr:`~TIMEPATTERN` dry weather flow time pattern
    :attr:`~CURVE`       generic table of values
    :attr:`~TSERIES`     generic time series of values
    :attr:`~CONTROL`     conveyance system control rules
    :attr:`~TRANSECT`    irregular channel cross-section
    :attr:`~AQUIFER`     groundwater aquifer
    :attr:`~UNITHYD`     RDII unit hydrograph
    :attr:`~SNOWMELT`    snowmelt parameter set
    :attr:`~SHAPE`       custom conduit shape
    :attr:`~LID`         LID treatment unit
    ==================== ===============================
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
    """Node Sub-Types enum class.

    :attr:`~JUNCTION`
    :attr:`~OUTFALL`
    :attr:`~STORAGE`
    :attr:`~DIVIDER`
    """
    JUNCTION
    OUTFALL
    STORAGE
    DIVIDER


class LinkType(Enum, start=0):
    """Link Sub-Types enum class.

    :attr:`~CONDUIT`
    :attr:`~PUMP`
    :attr:`~ORIFICE`
    :attr:`~WEIR`
    :attr:`~OUTLET`
    """
    CONDUIT
    PUMP
    ORIFICE
    WEIR
    OUTLET


class LinkDirection(Enum):
    """Link Direction enum class.

    :attr:`~UPSTREAM_TO_DOWNSTREAM`
    :attr:`~DOWNSTREAM_TO_UPSTREAM`
    """
    UPSTREAM_TO_DOWNSTREAM = 1
    DOWNSTREAM_TO_UPSTREAM = -1
    

class ElementType(IntEnum, start = 0):
    """SWMM Element Types enum class.

    :attr:`~SUBCATCH`
    :attr:`~NODE`
    :attr:`~LINK`
    :attr:`~SYSTEM`
    :attr:`~POLLUT`
    """
    SUBCATCH
    NODE
    LINK
    SYSTEM
    POLLUT


class Time(Enum, start = 0):
    """Time enum class.

    :attr:`~REPORT_STEP`
    :attr:`~NUM_PERIODS`
    """
    REPORT_STEP
    NUM_PERIODS


class SubcatchAttribute(Enum, start = 0):
    """Subcatchment Attributes enum class.

    .. rubric:: Enum Members

    ========================= ===============================
    :attr:`~RAINFALL`         rainfall intensity
    :attr:`~SNOW_DEPTH`       snow depth
    :attr:`~EVAP_LOSS`        evaporation loss 
    :attr:`~INFIL_LOSS`       infiltration loss
    :attr:`~RUNOFF_RATE`      runoff flow rate
    :attr:`~GW_OUTFLOW_RATE`  groundwater flow rate to node
    :attr:`~GW_TABLE_ELEV`    elevation of saturated gw table
    :attr:`~SOIL_MOISTURE`    soil moisture
    :attr:`~POLLUT_CONC_0`    pollutant washoff concentration
    ========================= ===============================
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
    """Node Attribute enum class.

    .. rubric:: Enum Members

    ========================= ===============================
    :attr:`~INVERT_DEPTH`     water depth above invert
    :attr:`~HYDRAULIC_HEAD`   hydraulic head
    :attr:`~PONDED_VOLUME`    volume stored and ponded
    :attr:`~LATERAL_INFLOW`   lateral inflow rate
    :attr:`~TOTAL_INFLOW`     total inflow rate
    :attr:`~FLOODING_LOSSES`  overflow rate
    :attr:`~POLLUT_CONC_0`    concentration of each pollutant
    ========================= ===============================
    """
    INVERT_DEPTH
    HYDRAULIC_HEAD
    PONDED_VOLUME
    LATERAL_INFLOW
    TOTAL_INFLOW
    FLOODING_LOSSES
    POLLUT_CONC_0


class LinkAttribute(Enum, start = 0):
    """Link Attribute enum class.

    .. rubric:: Enum Members

    ====================== ===============================
    :attr:`~FLOW_RATE`     flow rate
    :attr:`~FLOW_DEPTH`    flow depth
    :attr:`~FLOW_VELOCITY` flow velocity
    :attr:`~FLOW_VOLUME`   link volume
    :attr:`~CAPACITY`      ratio of area to full area
    :attr:`~POLLUT_CONC_0` concentration of each pollutant
    ====================== ===============================
    """
    FLOW_RATE
    FLOW_DEPTH
    FLOW_VELOCITY
    FLOW_VOLUME
    CAPACITY
    POLLUT_CONC_0


class SystemAttribute(Enum, start = 0):
    """System Attribute enum class.

    .. rubric:: Enum Members

    ============================= ====================
    :attr:`~AIR_TEMP`             air temperature
    :attr:`~RAINFALL`             rainfall intensity
    :attr:`~SNOW_DEPTH`           snow depth
    :attr:`~EVAP_INFIL_LOSS`      infiltration
    :attr:`~RUNOFF_FLOW`          runoff
    :attr:`~DRY_WEATHER_INFLOW`   dry weather inflow
    :attr:`~GW_INFLOW`            ground water inflow
    :attr:`~RDII_INFLOW`          RDII inflow
    :attr:`~DIRECT_INFLOW`        external inflow
    :attr:`~TOTAL_LATERAL_INFLOW` total lateral inflow
    :attr:`~FLOOD_LOSSES`         flooding outflow
    :attr:`~OUTFALL_FLOWS`        outfall outflow
    :attr:`~VOLUME_STORED`        storage volume
    :attr:`~EVAP_RATE`            evaporation
    ============================= ====================
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


#
# Solver Toolkit API Enums
#    
class TimeProperty(Enum, start=0):
    """Time Property enum class.

    :attr:`~START_DATE`
    :attr:`~END_DATE`
    :attr:`~REPORT_DATE`
    """
    START_DATE
    END_DATE
    REPORT_DATE


class UnitProperty(Enum, start=0):
    """Unit Property enum class.

    :attr:`~SYSTEM_UNIT`
    :attr:`~FLOW_UNIT`
    """
    SYSTEM_UNIT
    FLOW_UNIT


class SimOption(Enum, start=0):
    """Simulation Option enum class.

    :attr:`~ALLOW_POND`
    :attr:`~SKIP_STEADY`
    :attr:`~IGNORE_RAIN`
    :attr:`~IGNORE_RDII`
    :attr:`~IGNORE_SNOW`
    :attr:`~IGNORE_GW`
    :attr:`~IGNORE_ROUTE`
    :attr:`~IGNORE_ROUTE_QUALITY`
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
    """Simulation Settings enum class.

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
    """Node Property enum class.

    :attr:`~INVERT_ELEVATION`
    :attr:`~FULL_DEPTH`
    :attr:`~SURCHARGE_DEPTH`
    :attr:`~POND_AREA`
    :attr:`~INITIAL_DEPTH`
    """
    INVERT_ELEVATION
    FULL_DEPTH
    SURCHARGE_DEPTH
    POND_AREA
    INITIAL_DEPTH


class NodeResult(Enum, start=0):
    """Node Result enum class.

    :attr:`~TOTAL_INFLOW`
    :attr:`~TOTAL_OUTFLOW`
    :attr:`~LOSSES`
    :attr:`~VOLUME`
    :attr:`~FLOOD`
    :attr:`~DEPTH`
    :attr:`~HEAD`
    :attr:`~LATERAL_INFLOW`
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
    """Node Pollutant enum class.

    :attr:`~QUALITY`
    """
    QUALITY


class LinkProperty(Enum, start=0):
    """Link Property enum class.

    :attr:`~OFFSET_1`
    :attr:`~OFFSET_2`
    :attr:`~INITIAL_FLOW`
    :attr:`~FLOW_LIMIT`
    :attr:`~INLET_LOSS`
    :attr:`~OUTLET_LOSS`
    :attr:`~AVERAGE_LOSS`
    """
    OFFSET_1
    OFFSET_2
    INITIAL_FLOW
    FLOW_LIMIT
    INLET_LOSS
    OUTLET_LOSS
    AVERAGE_LOSS


class LinkResult(Enum, start=0):
    """Link Result enum class.

    :attr:`~FLOW`
    :attr:`~DEPTH`
    :attr:`~VOLUME`
    :attr:`~US_SURFACE_AREA`
    :attr:`~DS_SURFACE_AREA`
    :attr:`~SETTING`
    :attr:`~TARGET_SETTING`
    :attr:`~FROUDE`
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
    """Link Pollutant enum class.

    :attr:`~QUALITY`
    :attr:`~TOTAL_LOAD`
    """
    QUALITY
    TOTAL_LOAD

    
class SubcatchProperty(Enum, start=0):
    """Subcatchment Property enum class.

    :attr:`~WIDTH`
    :attr:`~AREA`
    :attr:`~IMPERVIOUS_FRACTION`
    :attr:`~SLOPE`
    :attr:`~CURB_LENGTH`
    """
    WIDTH
    AREA
    IMPERVIOUS_FRACTION
    SLOPE
    CURB_LENGTH


class SubcatchResult(Enum, start=0):
    """Subcatchment Result enum class.

    :attr:`~RAIN`
    :attr:`~EVAPORATION`
    :attr:`~INFILTRATION`
    :attr:`~RUNON`
    :attr:`~RUNOFF`
    :attr:`~SNOW`
    """
    RAIN
    EVAPORATION
    INFILTRATION
    RUNON
    RUNOFF
    SNOW


class SubcatchPollutant(Enum, start=0):
    """Subcatchment Pollutant enum class.

    :attr:`~BUILD_UP`
    :attr:`~CONCENTRATION`
    :attr:`~QUALITY`
    :attr:`~TOTAL_LOAD`
    """
    BUILD_UP
    CONCENTRATION
    QUALITY
    TOTAL_LOAD

    
class LidUsageProperty(Enum, start=0):
    """LID Usage Property enum class.

    :attr:`~UNIT_AREA`
    :attr:`~TOP_WIDTH`
    :attr:`~BOTTOM_WIDTH`
    :attr:`~INITIAL_SATURATION`
    :attr:`~FROM_IMPERVIOUS`
    :attr:`~FROM_PERVIOUS`
    """
    UNIT_AREA
    TOP_WIDTH
    BOTTOM_WIDTH
    INITIAL_SATURATION
    FROM_IMPERVIOUS
    FROM_PERVIOUS


class LidUsageOption(Enum, start=0):
    """LID Usage Option enum class.

    :attr:`~INDEX`
    :attr:`~NUMBER`
    :attr:`~TO_PERV`
    :attr:`~DRAIN_SUBCATCH`
    :attr:`~DRAIN_NODE`
    """
    INDEX
    NUMBER
    TO_PERV
    DRAIN_SUBCATCH
    DRAIN_NODE


class LidLayer(Enum, start=0):
    """LID Layer enum class.

    :attr:`~SURFACE`
    :attr:`~SOIL`
    :attr:`~STORAGE`
    :attr:`~PAVEMENT`
    :attr:`~DRAIN`
    :attr:`~DRAIN_MAT`
    """
    SURFACE
    SOIL
    STORAGE
    PAVEMENT
    DRAIN
    DRAIN_MAT

    
class LidLayerProperty(Enum, start=0):
    """LID Layer Property enum class.

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
    """LID Result enum class.

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
    """Rain Result enum class.

    :attr:`~TOTAL`
    :attr:`~RAINFALL`
    :attr:`~SNOWFALL`
    """
    TOTAL
    RAINFALL
    SNOWFALL
