
from swmm.output import output


# Units of Measurement
#
# Units                  US Customary                           SI Metric    
#    AREA_SUBCATCH          acres                 ac               hectares            ha
#    AREA_STOR              square feet           sq ft            square meters       sq m
#    AREA_POND              square feet           sq ft            square meters       sq m
#    CAP_SUC                inches                in               millimeters         mm
#    CONC                   milligrams/liter      mg/L             milligrams/liter    mg/L             
#                           micrograms/liter      ug/L             micrograms/liter    ug/L
#                           counts/liter          Count/L          counts/liter        Count/L
#    INFIL_DECAY            1/hours               1/hrs            1/hours             1/hrs
#    POLLUT_DECAY           1/days                1/days           1/days              1/days 
#    DEPRES_STOR            inches                in               millimeters         mm
#    DEPTH                  feet                  ft               meters              m
#    DIAM                   feet                  ft               meters              m
#    DISC_COEFF_ORIF        dimensionless         dimless          dimensionless       dimless
#    DISC_COEFF_WEIR        CFS/foot^n            CFS/ft^n         CMS/meter^n         CMS/m^n
#    ELEV                   feet                  ft               meters              m
#    EVAP_RATE              inches/day            in/day           millimeters/day     mm/day
#    FLOW_RATE              cubic feet/sec        CFS              cubic meter/sec     CMS
#                           gallons/minute        GPM              liter/sec           LPS
#                           million gallons/day   MGD              million liter/day   MLD
#    HEAD                   feet                  ft               meters              m
#    HYD_CONDUCT            inches/hour           in/hr            millimeters/hour    mm/hr
#    INFIL_RATE             inches/hour           in/hr            millimeters/hour    mm/hr
#    LEN                    feet                  ft               meters              m
#    MANN_N                 seconds/meter^1/3     sec/m^1/3        seconds/meter^1/3   sec/m^1/3
#    POLLUT_BUILDUP         mass/length           mass/len         mass/length         mass/len
#                           mass/acre             mass/ac          mass/hectare        mass/ha
#    RAIN_INTENSITY         inches/hour           in/hr            millimeters/hour    mm/hr
#    RAIN_VOLUME            inches                in               millimeters         mm
#    SLOPE_SUBCATCH         percent               percent          percent             percent
#    SLOPE_XSEC             rise/run              rise/run         rise/run            rise/run
#    STREET_CLEAN_INT       days                  days             days                days
#    VOLUME                 cubic feet            cu ft            cubic meters        cu m
#    WIDTH                  feet                  ft               meters              m


# Output Metadata
#
# Subcatch Attributes    Long Name                    Units
#    RAINFALL               Rainfall                     RAIN_INTENSITY
#    SNOW_DEPTH             Snow Depth                   DEPTH
#    EVAP_LOSS              Evaporation Loss             LOSS_RATE
#    INFIL_LOSS             Infiltration Loss            LOSS_RATE
#    RUNOFF_RATE            Runoff Rate                  FLOW_RATE
#    GW_OUTFLOW_RATE        Groundwater Flow Rate        FLOW_RATE
#    GW_TABLE_ELEV          Groundwater Elevation        ELEV
#    SOIL_MOISTURE          Soil Moisture                PERCENT
#    POLLUT_CONC            Pollutant Concentration      CONC

# Node Attributes   
#    INVERT_DEPTH           Invert Depth                 DEPTH   
#    HYDRAULIC_HEAD         Hydraulic Head               HEAD
#    PONDED_VOLUME          Ponded Volume                VOLUME
#    LATERAL_INFLOW         Lateral Inflow               FLOW_RATE
#    TOTAL_INFLOW           Total Inflow                 FLOW_RATE
#    FLOODING_LOSSES        Flooding Loss                FLOW_RATE
#    POLLUT_CONC            Pollutant Concentration      CONC
    
# Link Attributes
#    FLOW_RATE              Flow Rate                    FLOW_RATE
#    FLOW_DEPTH             Flow Depth                   DEPTH
#    FLOW_VELOCITY          Flow Velocity                VELOCITY
#    FLOW_VOLUME            Flow Volume                  VOLUME
#    CAPACITY               Capacity                     PERCENT 
#    POLLUT_CONC            Pollutant Concentration      CONC

# System Attributes
#    AIR_TEMP               Temperature                  TEMP
#    RAINFALL               Rainfall                     RAIN_INTENSITY
#    SNOW_DEPTH             Snow Depth                   DEPTH
#    EVAP_INFIL_LOSS        Evap and Infil Losses        LOSS_RATE
#    RUNOFF_FLOW            Runoff Flow Rate             FLOW_RATE
#    DRY_WEATHER_INFLOW     Dry Weather Inflow           FLOW_RATE
#    GW_INFLOW              Groundwater Inflow           FLOW_RATE
#    RDII_INFLOW            RDII Inflow                  FLOW_RATE
#    DIRECT_INFLOW          Direct Inflow                FLOW_RATE
#    TOTAL_LATERAL_INFLOW   Total Lateral Inflow         FLOW_RATE
#    FLOOD_LOSSES           Flood Losses                 FLOW_RATE
#    OUTFALL_FLOWS          Outfall Flow                 FLOW_RATE
#    VOLUME_STORED          Volume Stored                VOLUME
#    EVAP_RATE              Evaporation Rate             LOSS_RATE
