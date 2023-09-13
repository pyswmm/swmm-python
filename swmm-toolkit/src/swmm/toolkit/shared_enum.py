#
#  shared_enum.py -
#
#  Created:   February 21, 2020
#  Updated:
#
#  Author:    See AUTHORS
#

from aenum import Enum, IntEnum


class UnitSystem(Enum):
    """SWMM Unit System enum class. 

    .. rubric:: Enum Members

    ================ ====================
    :attr:`~US`      US Traditional units
    :attr:`~SI`      SI (metric) units
    ================ ====================
    """
    US = 0
    SI = 1


class FlowUnits(Enum):
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
    CFS = 0
    GPM = 1
    MGD = 2
    CMS = 3
    LPS = 4
    MLD = 5


class ConcUnits(Enum):
    """SWMM Concentration Units enum class.

    .. rubric:: Enum Members

    ================ ====================
    :attr:`~MG`      Milligrams per liter
    :attr:`~UG`      Micrograms per liter
    :attr:`~COUNT`   Counts per liter
    :attr:`~NONE`    None
    ================ ====================
    """
    MG = 0
    UG = 1
    COUNT = 2
    NONE = 3


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
    RAIN_INT = 1
    SNOW_DEPTH = 2
    EVAP_RATE = 3
    INFIL_RATE = 4
    FLOW_RATE = 5
    ELEV = 6
    PERCENT = 7
    CONCEN = 8
    HEAD = 9
    VOLUME = 10
    VELOCITY = 11
    TEMP = 12
    UNITLESS = 13
    NONE = 14


class ObjectType(Enum):
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
    GAGE = 0
    SUBCATCH = 1
    NODE = 2
    LINK = 3
    POLLUT = 4
    LANDUSE = 5
    TIMEPATTERN = 6
    CURVE = 7
    TSERIES = 8
    CONTROL = 9
    TRANSECT = 10
    AQUIFER = 11
    UNITHYD = 12
    SNOWMELT = 13
    SHAPE = 14
    LID = 15


class NodeType(Enum):
    """Node Sub-Types enum class.

    :attr:`~JUNCTION`
    :attr:`~OUTFALL`
    :attr:`~STORAGE`
    :attr:`~DIVIDER`
    """
    JUNCTION = 0
    OUTFALL = 1
    STORAGE = 2
    DIVIDER = 3


class LinkType(Enum):
    """Link Sub-Types enum class.

    :attr:`~CONDUIT`
    :attr:`~PUMP`
    :attr:`~ORIFICE`
    :attr:`~WEIR`
    :attr:`~OUTLET`
    """
    CONDUIT = 0
    PUMP = 1
    ORIFICE = 2
    WEIR = 3
    OUTLET = 4


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
    SUBCATCH = 0
    NODE = 1
    LINK = 2
    SYSTEM = 3
    POLLUT = 4


class Time(Enum, start = 0):
    """Time enum class.

    :attr:`~REPORT_STEP`
    :attr:`~NUM_PERIODS`
    """
    REPORT_STEP = 0
    NUM_PERIODS = 1


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
    RAINFALL = 0
    SNOW_DEPTH = 1
    EVAP_LOSS = 2
    INFIL_LOSS = 3
    RUNOFF_RATE = 4
    GW_OUTFLOW_RATE = 5
    GW_TABLE_ELEV = 6
    SOIL_MOISTURE = 7
    POLLUT_CONC_0 = 8


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
    INVERT_DEPTH = 0
    HYDRAULIC_HEAD = 1
    PONDED_VOLUME = 2
    LATERAL_INFLOW = 3
    TOTAL_INFLOW = 4
    FLOODING_LOSSES = 5
    POLLUT_CONC_0 = 6


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
    FLOW_RATE = 0
    FLOW_DEPTH = 1
    FLOW_VELOCITY = 2
    FLOW_VOLUME = 3
    CAPACITY = 4
    POLLUT_CONC_0 = 5


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
    :attr:`~PTNL_EVAP_RATE`       potential evapotranspiration
    ============================= ====================
    """
    AIR_TEMP = 0
    RAINFALL = 1
    SNOW_DEPTH = 2
    EVAP_INFIL_LOSS = 3
    RUNOFF_FLOW = 4
    DRY_WEATHER_INFLOW = 5
    GW_INFLOW = 6
    RDII_INFLOW = 7
    DIRECT_INFLOW = 8
    TOTAL_LATERAL_INFLOW = 9
    FLOOD_LOSSES = 10
    OUTFALL_FLOWS = 11
    VOLUME_STORED = 12
    EVAP_RATE = 13
    PTNL_EVAP_RATE = 14


#
# Solver Toolkit API Enums
#    
class TimeProperty(Enum):
    """Time Property enum class.

    :attr:`~START_DATE`
    :attr:`~END_DATE`
    :attr:`~REPORT_DATE`
    """
    START_DATE = 0
    END_DATE = 1
    REPORT_DATE = 2


class UnitProperty(Enum):
    """Unit Property enum class.

    :attr:`~SYSTEM_UNIT`
    :attr:`~FLOW_UNIT`
    """
    SYSTEM_UNIT = 0
    FLOW_UNIT = 1


class SimOption(Enum):
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
    ALLOW_POND = 0
    SKIP_STEADY = 1
    IGNORE_RAIN = 2
    IGNORE_RDII = 3
    IGNORE_SNOW = 4
    IGNORE_GW = 5
    IGNORE_ROUTE = 6
    IGNORE_ROUTE_QUALITY = 7


class SimSetting(Enum):
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
    ROUTE_STEP = 0
    MIN_ROUTE_STEP = 1
    LENGTH_STEP = 2
    START_DRY_DAYS = 3
    COURANT_FACTOR = 4
    MIN_SURFACE_AREA = 5
    MIN_SLOPE = 6
    RUNOFF_ERROR = 7
    GW_ERROR = 8
    FLOW_ERROR = 9
    QUALITY_ERROR = 10
    HEAD_TOLERANCE = 11
    SYSTEM_FLOW_TOLERANCE = 12
    LATERAL_FLOW_TOLERANCE = 13
    THREADS = 14


class NodeProperty(Enum):
    """Node Property enum class.

    :attr:`~INVERT_ELEVATION`
    :attr:`~FULL_DEPTH`
    :attr:`~SURCHARGE_DEPTH`
    :attr:`~POND_AREA`
    :attr:`~INITIAL_DEPTH`
    """
    INVERT_ELEVATION = 0
    FULL_DEPTH = 1
    SURCHARGE_DEPTH = 2
    POND_AREA = 3
    INITIAL_DEPTH = 4


class NodeResult(Enum):
    """Node Result enum class.

    :attr:`~TOTAL_INFLOW`
    :attr:`~TOTAL_OUTFLOW`
    :attr:`~LOSSES`
    :attr:`~VOLUME`
    :attr:`~FLOOD`
    :attr:`~DEPTH`
    :attr:`~HEAD`
    :attr:`~LATERAL_INFLOW`
    :attr:`~HYD_RES_TIME`
    """
    TOTAL_INFLOW = 0
    TOTAL_OUTFLOW = 1
    LOSSES = 2
    VOLUME = 3
    FLOOD = 4
    DEPTH = 5
    HEAD = 6
    LATERAL_INFLOW = 7
    HYD_RES_TIME = 8


class NodePollutant(Enum):
    """Node Pollutant enum class.

    :attr:`~QUALITY`
    :attr:`~INFLOW_CONC`
    :attr:`~REACTOR_CONC`
    """
    QUALITY = 0
    INFLOW_CONC = 1
    REACTOR_CONC = 2


class LinkProperty(Enum):
    """Link Property enum class.

    :attr:`~OFFSET_1`
    :attr:`~OFFSET_2`
    :attr:`~INITIAL_FLOW`
    :attr:`~FLOW_LIMIT`
    :attr:`~INLET_LOSS`
    :attr:`~OUTLET_LOSS`
    :attr:`~AVERAGE_LOSS`
    """
    OFFSET_1 = 0
    OFFSET_2 = 1
    INITIAL_FLOW = 2
    FLOW_LIMIT = 3
    INLET_LOSS = 4
    OUTLET_LOSS = 5
    AVERAGE_LOSS = 6


class LinkResult(Enum):
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
    FLOW = 0
    DEPTH = 1
    VOLUME = 2
    US_SURFACE_AREA = 3
    DS_SURFACE_AREA = 4
    SETTING = 5
    TARGET_SETTING = 6
    FROUDE = 7


class LinkPollutant(Enum):
    """Link Pollutant enum class.

    :attr:`~QUALITY`
    :attr:`~TOTAL_LOAD`
    :attr:`~REACTOR_CONC`
    """
    QUALITY = 0
    TOTAL_LOAD = 1
    REACTOR_CONC = 2

    
class SubcatchProperty(Enum):
    """Subcatchment Property enum class.

    :attr:`~WIDTH`
    :attr:`~AREA`
    :attr:`~IMPERVIOUS_FRACTION`
    :attr:`~SLOPE`
    :attr:`~CURB_LENGTH`
    """
    WIDTH = 0
    AREA = 1
    IMPERVIOUS_FRACTION = 2
    SLOPE = 3
    CURB_LENGTH = 4


class SubcatchResult(Enum):
    """Subcatchment Result enum class.

    :attr:`~RAIN`
    :attr:`~EVAPORATION`
    :attr:`~INFILTRATION`
    :attr:`~RUNON`
    :attr:`~RUNOFF`
    :attr:`~SNOW`
    """
    RAIN = 0
    EVAPORATION = 1
    INFILTRATION = 2
    RUNON = 3
    RUNOFF = 4
    SNOW = 5


class SubcatchPollutant(Enum):
    """Subcatchment Pollutant enum class.

    :attr:`~BUILD_UP`
    :attr:`~CONCENTRATION`
    :attr:`~QUALITY`
    :attr:`~TOTAL_LOAD`
    """
    BUILD_UP = 0
    CONCENTRATION = 1
    QUALITY = 2
    TOTAL_LOAD = 3

    
class LidUsageProperty(Enum):
    """LID Usage Property enum class.

    :attr:`~UNIT_AREA`
    :attr:`~TOP_WIDTH`
    :attr:`~BOTTOM_WIDTH`
    :attr:`~INITIAL_SATURATION`
    :attr:`~FROM_IMPERVIOUS`
    :attr:`~FROM_PERVIOUS`
    """
    UNIT_AREA = 0
    TOP_WIDTH = 1
    BOTTOM_WIDTH = 2
    INITIAL_SATURATION = 3
    FROM_IMPERVIOUS = 4
    FROM_PERVIOUS = 5


class LidUsageOption(Enum):
    """LID Usage Option enum class.

    :attr:`~INDEX`
    :attr:`~NUMBER`
    :attr:`~TO_PERV`
    :attr:`~DRAIN_SUBCATCH`
    :attr:`~DRAIN_NODE`
    """
    INDEX = 0
    NUMBER = 1
    TO_PERV = 2
    DRAIN_SUBCATCH = 3
    DRAIN_NODE = 4


class LidLayer(Enum):
    """LID Layer enum class.

    :attr:`~SURFACE`
    :attr:`~SOIL`
    :attr:`~STORAGE`
    :attr:`~PAVEMENT`
    :attr:`~DRAIN`
    :attr:`~DRAIN_MAT`
    """
    SURFACE = 0
    SOIL = 1
    STORAGE = 2
    PAVEMENT = 3
    DRAIN = 4
    DRAIN_MAT = 5

    
class LidLayerProperty(Enum):
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
    THICKNESS = 0
    VOID_FRACTION = 1
    ROUGHNESS = 2
    SURFACE_SLOPE = 3
    SIDE_SLOP = 4
    ALPHA = 5
    POROSITY = 6
    FIELD_CAPACITY = 7
    WILTING_POINT = 8
    SUCTION_HEAD = 9
    K_SATURATION = 10
    K_SLOPE = 11
    CLOG_FACTOR = 12
    IMPERVIOUS_FRACTION = 13
    DRAIN_COEFFICIENT = 14
    DRAIN_EXPONENT = 15
    DRAIN_OFFSET = 16
    DRAIN_DELAY = 17
    DRAIN_HEAD_OPEN = 18
    DRAIN_HEAD_CLOSE = 19
    DRAIN_CURVE = 20
    DRAIN_REGEN_DAYS = 21
    DRAIN_REGEN_DEGREE = 22


class LidResult(Enum):
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
    INFLOW = 0
    EVAPORATION = 1
    INFILTRATION = 2
    SURFACE_FLOW = 3
    DRAIN_FLOW = 4
    INITIAL_VOLUME = 5
    FINAL_VOLUME = 6
    SURFACE_DEPTH = 7
    PAVEMENT_DEPTH = 8
    SOIL_MOISTURE = 9
    STORAGE_DEPTH = 10
    DRY_TIME = 11
    OLD_DRAIN_FLOW = 12
    NEW_DRAIN_FLOW = 13
    PERVIOUS_AREA = 14
    FLOW_TO_PERVIOUS_AREA = 15
    EVAPORATE_RATE = 16
    NATIVE_INFILTRATION = 17
    SURFACE_INFLOW = 18
    SURFACE_INFILTRATION = 19
    SURFACE_EVAPORATION = 20
    SURFACE_OUTFLOW = 21
    PAVEMENT_EVAPORATION = 22
    PAVEMENT_PERCOLATION = 23
    SOIL_EVAPORATION = 24
    SOIL_PERCOLATION = 25
    STORAGE_INFLOW = 26
    STORAGE_EXFILTRATION = 27
    STORAGE_EVAPORATION = 28
    STORAGE_DRAIN = 29

    
class RainResult(Enum):
    """Rain Result enum class.

    :attr:`~TOTAL`
    :attr:`~RAINFALL`
    :attr:`~SNOWFALL`
    """
    TOTAL = 0
    RAINFALL = 1
    SNOWFALL = 2

class InletProperty(Enum):
    """Inlet Property enum class.
    
    :attr:`~NUM_INLETS`
    :attr:`~CLOG_FACTOR`
    :attr:`~FLOW_LIMIT`
    :attr:`~DEPRESSION_HEIGHT`
    :attr:`~DEPRESSION_WIDTH`"""
    NUM_INLETS = 0
    CLOG_FACTOR = 1
    FLOW_LIMIT = 2
    DEPRESSION_HEIGHT = 3
    DEPRESSION_WIDTH = 4
    

class InletResult(Enum):
    """Inlet Result enum class.

    :attr:`~FLOW_FACTOR`
    :attr:`~FLOW CAPTURE`
    :attr:`~BACK_FLOW`
    :attr:`~BLACK_FLOW_RATIO`
    """
    FLOW_FACTOR = 0
    FLOW_CAPTURE = 1
    BACK_FLOW = 2
    BLACK_FLOW_RATIO = 3

class HotstartFile(Enum):
    """Hotstart File enum class.

    :attr:`~USE`
    :attr:`~SAVE`
    """
    USE = 0
    SAVE = 1