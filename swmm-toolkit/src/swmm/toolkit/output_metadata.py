#
#  output_metadata.py -
#
#  Created: February 20, 2020
#  Updated:
#
#  Author:     Michael E. Tryby
#              US EPA - ORD/CESER
#


from itertools import islice

from aenum import extend_enum

from swmm.toolkit import output, output_enum, solver_enum


class OutputMetadata:
    '''
    Simple attribute name and unit lookup.
    '''
    _unit_labels_us_ = {
        output_enum.BaseUnits.RAIN_INT:   "in/hr",
        output_enum.BaseUnits.SNOW_DEPTH: "in",
        output_enum.BaseUnits.EVAP_RATE:  "in/day",
        output_enum.BaseUnits.INFIL_RATE: "in/hr",
        output_enum.BaseUnits.ELEV:       "ft",
        output_enum.BaseUnits.PERCENT:    "%",
        output_enum.BaseUnits.HEAD:       "ft",
        output_enum.BaseUnits.VOLUME:     "cu ft",
        output_enum.BaseUnits.VELOCITY:   "ft/sec",
        output_enum.BaseUnits.TEMP:       "deg F",
        output_enum.BaseUnits.UNITLESS:   "unitless",
        output_enum.BaseUnits.NONE:       "",

        solver_enum.FlowUnits.CFS:          "cu ft/sec",
        solver_enum.FlowUnits.GPM:          "gal/min",
        solver_enum.FlowUnits.MGD:          "M gal/day",
    }

    _unit_labels_si_ = {
        output_enum.BaseUnits.RAIN_INT:   "mm/hr",
        output_enum.BaseUnits.SNOW_DEPTH: "mm",
        output_enum.BaseUnits.EVAP_RATE:  "mm/day",
        output_enum.BaseUnits.INFIL_RATE: "mm/hr",
        output_enum.BaseUnits.ELEV:       "m",
        output_enum.BaseUnits.PERCENT:    "%",
        output_enum.BaseUnits.HEAD:       "m",
        output_enum.BaseUnits.VOLUME:     "cu m",
        output_enum.BaseUnits.VELOCITY:   "m/sec",
        output_enum.BaseUnits.TEMP:       "deg C",
        output_enum.BaseUnits.UNITLESS:   "unitless",
        output_enum.BaseUnits.NONE:       "",

        solver_enum.FlowUnits.CMS:          "cu m/sec",
        solver_enum.FlowUnits.LPS:          "L/sec",
        solver_enum.FlowUnits.MLD:          "M L/day",
    }

    _unit_labels_quality_ = {
        solver_enum.ConcUnits.MG:           "mg/L",
        solver_enum.ConcUnits.UG:           "ug/L",
        solver_enum.ConcUnits.COUNT:        "Count/L",
        solver_enum.ConcUnits.NONE:         ""
    }


    def _build_pollut_metadata(self, output_handle):
        '''
        Builds metadata for pollutant attributes at runtime.
        '''
        # Get number of pollutants
        n = output.get_proj_size(output_handle)[output_enum.ElementType.POLLUT]

        if n > 0:

            pollut_name = []
            pollut_units = []

            # Get pollutant names
            for i in range(0, n):
                pollut_name.append(output.get_elem_name(
                    output_handle, output_enum.ElementType.POLLUT, i))
            # Get pollutant units
            for u in output.get_units(output_handle)[2:]:
                pollut_units.append(solver_enum.ConcUnits(u))

            # Create dictionary keys
            for i in range(1, n):
                symbolic_name = 'POLLUT_CONC_' + str(i)
                extend_enum(output_enum.SubcatchAttribute, symbolic_name, 8 + i)
                extend_enum(output_enum.NodeAttribute, symbolic_name, 6 + i)
                extend_enum(output_enum.LinkAttribute, symbolic_name, 5 + i)

            # Update metadata dictionary with pollutant metadata
            for i, attr in enumerate(islice(output_enum.SubcatchAttribute, 8, None)):
                self._metadata[attr] = (pollut_name[i], self._unit_labels[pollut_units[i]])

            for i, attr in enumerate(islice(output_enum.NodeAttribute, 6, None)):
                self._metadata[attr] = (pollut_name[i], self._unit_labels[pollut_units[i]])

            for i, attr in enumerate(islice(output_enum.LinkAttribute, 5, None)):
                self._metadata[attr] = (pollut_name[i], self._unit_labels[pollut_units[i]])


    def __init__(self, output_handle):
        # Get units from binary output file
        self.units = output.get_units(output_handle)

        # Determine prevailing unit system
        self._unit_system = solver_enum.UnitSystem(self.units[0])
        if self._unit_system == solver_enum.UnitSystem.US:
            self._unit_labels = type(self)._unit_labels_us_
        else:
            self._unit_labels = type(self)._unit_labels_si_

        self._unit_labels.update(type(self)._unit_labels_quality_)

        # Set user flow units
        self._flow = solver_enum.FlowUnits(self.units[1])

        self._metadata = {
            output_enum.SubcatchAttribute.RAINFALL:
                ("Rainfall", self._unit_labels[output_enum.BaseUnits.RAIN_INT]),
            output_enum.SubcatchAttribute.SNOW_DEPTH:
                ("Snow Depth", self._unit_labels[output_enum.BaseUnits.SNOW_DEPTH]),
            output_enum.SubcatchAttribute.EVAP_LOSS:
                ("Evaporation Loss", self._unit_labels[output_enum.BaseUnits.EVAP_RATE]),
            output_enum.SubcatchAttribute.INFIL_LOSS:
                ("Infiltration Loss", self._unit_labels[output_enum.BaseUnits.INFIL_RATE]),
            output_enum.SubcatchAttribute.RUNOFF_RATE:
                ("Runoff Rate", self._unit_labels[self._flow]),
            output_enum.SubcatchAttribute.GW_OUTFLOW_RATE:
                ("Groundwater Flow Rate", self._unit_labels[self._flow]),
            output_enum.SubcatchAttribute.GW_TABLE_ELEV:
                ("Groundwater Elevation", self._unit_labels[output_enum.BaseUnits.ELEV]),
            output_enum.SubcatchAttribute.SOIL_MOISTURE:
                ("Soil Moisture", self._unit_labels[output_enum.BaseUnits.PERCENT]),
            output_enum.SubcatchAttribute.POLLUT_CONC_0:
                ("Pollutant Concentration", self._unit_labels[output_enum.BaseUnits.NONE]),

            output_enum.NodeAttribute.INVERT_DEPTH:
                ("Invert Depth", self._unit_labels[output_enum.BaseUnits.ELEV]),
            output_enum.NodeAttribute.HYDRAULIC_HEAD:
                ("Hydraulic Head", self._unit_labels[output_enum.BaseUnits.HEAD]),
            output_enum.NodeAttribute.PONDED_VOLUME:
                ("Ponded Volume", self._unit_labels[output_enum.BaseUnits.VOLUME]),
            output_enum.NodeAttribute.LATERAL_INFLOW:
                ("Lateral Inflow", self._unit_labels[self._flow]),
            output_enum.NodeAttribute.TOTAL_INFLOW:
                ("Total Inflow", self._unit_labels[self._flow]),
            output_enum.NodeAttribute.FLOODING_LOSSES:
                ("Flooding Loss", self._unit_labels[self._flow]),
            output_enum.NodeAttribute.POLLUT_CONC_0:
                ("Pollutant Concentration", self._unit_labels[output_enum.BaseUnits.NONE]),

            output_enum.LinkAttribute.FLOW_RATE:
                ("Flow Rate", self._unit_labels[self._flow]),
            output_enum.LinkAttribute.FLOW_DEPTH:
                ("Flow Depth", self._unit_labels[output_enum.BaseUnits.ELEV]),
            output_enum.LinkAttribute.FLOW_VELOCITY:
                ("Flow Velocity", self._unit_labels[output_enum.BaseUnits.VELOCITY]),
            output_enum.LinkAttribute.FLOW_VOLUME:
                ("Flow Volume", self._unit_labels[output_enum.BaseUnits.VOLUME]),
            output_enum.LinkAttribute.CAPACITY:
                ("Capacity", self._unit_labels[output_enum.BaseUnits.PERCENT]),
            output_enum.LinkAttribute.POLLUT_CONC_0:
                ("Pollutant Concentration", self._unit_labels[output_enum.BaseUnits.NONE]),

            output_enum.SystemAttribute.AIR_TEMP:
                ("Temperature", self._unit_labels[output_enum.BaseUnits.TEMP]),
            output_enum.SystemAttribute.RAINFALL:
                ("Rainfall", self._unit_labels[output_enum.BaseUnits.RAIN_INT]),
            output_enum.SystemAttribute.SNOW_DEPTH:
                ("Snow Depth", self._unit_labels[output_enum.BaseUnits.SNOW_DEPTH]),
            output_enum.SystemAttribute.EVAP_INFIL_LOSS:
                ("Evap and Infil Losses", self._unit_labels[output_enum.BaseUnits.INFIL_RATE]),
            output_enum.SystemAttribute.RUNOFF_FLOW:
                ("Runoff Flow Rate", self._unit_labels[self._flow]),
            output_enum.SystemAttribute.DRY_WEATHER_INFLOW:
                ("Dry Weather Inflow", self._unit_labels[self._flow]),
            output_enum.SystemAttribute.GW_INFLOW:
                ("Groundwater Inflow", self._unit_labels[self._flow]),
            output_enum.SystemAttribute.RDII_INFLOW:
                ("RDII Inflow", self._unit_labels[self._flow]),
            output_enum.SystemAttribute.DIRECT_INFLOW:
                ("Direct Inflow", self._unit_labels[self._flow]),
            output_enum.SystemAttribute.TOTAL_LATERAL_INFLOW:
                ("Total Lateral Inflow", self._unit_labels[self._flow]),
            output_enum.SystemAttribute.FLOOD_LOSSES:
                ("Flood Losses", self._unit_labels[self._flow]),
            output_enum.SystemAttribute.OUTFALL_FLOWS:
                ("Outfall Flow", self._unit_labels[self._flow]),
            output_enum.SystemAttribute.VOLUME_STORED:
                ("Volume Stored", self._unit_labels[output_enum.BaseUnits.VOLUME]),
            output_enum.SystemAttribute.EVAP_RATE:
                ("Evaporation Rate", self._unit_labels[output_enum.BaseUnits.EVAP_RATE])
        }

        self._build_pollut_metadata(output_handle)


    def get_attribute_metadata(self, attribute):
        '''
        Takes an attribute enum and returns the name and units in a tuple.
        '''
        return self._metadata[attribute]


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
