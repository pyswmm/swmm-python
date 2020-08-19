#
#  toolkit_enum.py -
#
#  Created: August 20, 2020
#  Updated:
#
#  Author:     Michael E. Tryby
#              US EPA - ORD/CESER
#              Jennifer Wu
#              Xylem Inc


from aenum import Enum, IntEnum


class ObjectProperty(Enum, start=0):
    GAGE,
    SUBCATCH,  
    NODE,
    LINK,    
    POLLUT,
    LANDUSE,  
    TIMEPATTERN, 
    CURVE,
    TSERIES,    
    CONTROL, 
    TRANSECT,  
    AQUIFER,
    UNITHYD,  
    SNOWMELT,
    SHAPE,
    LID

    
class TimeProperty(Enum, start = 0):
    START_DATE,
    END_DATE,
    REPORT_DATE

