


%typemap(in, numinputs=0) SM_NodeStats **in_out_dict (SM_NodeStats *temp){
    $1 = &temp;
}
%typemap(argout) SM_NodeStats **in_out_dict {
    PyObject *o = PyDict_New();
    PyMapping_SetItemString(o, "avgDepth", PyFloat_FromDouble((*$1)->avgDepth));
    PyMapping_SetItemString(o, "maxDepth", PyFloat_FromDouble((*$1)->maxDepth));
    PyMapping_SetItemString(o, "maxDepthDate", PyFloat_FromDouble((*$1)->maxDepthDate));
    PyMapping_SetItemString(o, "maxRptDepth", PyFloat_FromDouble((*$1)->maxRptDepth));
    PyMapping_SetItemString(o, "volFlooded", PyFloat_FromDouble((*$1)->volFlooded));
    PyMapping_SetItemString(o, "timeFlooded", PyFloat_FromDouble((*$1)->timeFlooded));
    PyMapping_SetItemString(o, "timeSurcharged", PyFloat_FromDouble((*$1)->timeSurcharged));
    PyMapping_SetItemString(o, "timeCourantCritical", PyFloat_FromDouble((*$1)->timeCourantCritical));
    PyMapping_SetItemString(o, "totLatFlow", PyFloat_FromDouble((*$1)->totLatFlow));
    PyMapping_SetItemString(o, "maxLatFlow", PyFloat_FromDouble((*$1)->maxLatFlow));
    PyMapping_SetItemString(o, "maxInflow", PyFloat_FromDouble((*$1)->maxInflow));
    PyMapping_SetItemString(o, "maxOverflow", PyFloat_FromDouble((*$1)->maxOverflow));
    PyMapping_SetItemString(o, "maxPondedVol", PyFloat_FromDouble((*$1)->maxPondedVol));
    PyMapping_SetItemString(o, "maxInflowDate", PyFloat_FromDouble((*$1)->maxInflowDate));
    PyMapping_SetItemString(o, "maxOverflowDate", PyFloat_FromDouble((*$1)->maxOverflowDate));
    $result = SWIG_Python_AppendOutput($result, o);
    swmm_freeMemory(*$1);
}

%typemap(in, numinputs=0) SM_StorageStats **in_out_dict (SM_StorageStats *temp){
    $1 = &temp;
}
%typemap(argout) SM_StorageStats **in_out_dict {
    PyObject *o = PyDict_New();
    PyMapping_SetItemString(o, "initVol", PyFloat_FromDouble((*$1)->initVol));
    PyMapping_SetItemString(o, "avgVol", PyFloat_FromDouble((*$1)->avgVol));
    PyMapping_SetItemString(o, "maxVol", PyFloat_FromDouble((*$1)->maxVol));
    PyMapping_SetItemString(o, "maxFlow", PyFloat_FromDouble((*$1)->maxFlow));
    PyMapping_SetItemString(o, "evapLosses", PyFloat_FromDouble((*$1)->evapLosses));
    PyMapping_SetItemString(o, "exfilLosses", PyFloat_FromDouble((*$1)->exfilLosses));
    PyMapping_SetItemString(o, "maxVolDate", PyFloat_FromDouble((*$1)->maxVolDate));
    $result = SWIG_Python_AppendOutput($result, o);
    swmm_freeMemory(*$1);
}

%typemap(in, numinputs=0) SM_OutfallStats **in_out_dict (SM_OutfallStats *temp){
    $1 = &temp;
}
%typemap(argout) SM_OutfallStats **in_out_dict {
    int length = sizeof((*$1)->totalLoad)/sizeof(double) + 1;
    PyObject *loads = PyList_New(length);
    PyObject *o = PyDict_New();
    for(int i=0; i<length; i++) {
      PyList_SetItem(loads, i, PyFloat_FromDouble(((*$1)->totalLoad)[i]));
    }
    PyMapping_SetItemString(o, "avgFlow", PyFloat_FromDouble((*$1)->avgFlow));
    PyMapping_SetItemString(o, "maxFlow", PyFloat_FromDouble((*$1)->maxFlow));
    PyMapping_SetItemString(o, "loads", loads);
    PyMapping_SetItemString(o, "totalPeriods", PyLong_FromLong((*$1)->totalPeriods));
    $result = SWIG_Python_AppendOutput($result, o);
    swmm_freeOutfallStats(*$1);
    swmm_freeMemory(*$1);
}

%typemap(in, numinputs=0) SM_LinkStats **in_out_dict (SM_LinkStats *temp){
    $1 = &temp;
}
%typemap(argout) SM_LinkStats **in_out_dict {
    PyObject *o = PyDict_New();
    PyObject *flowTime = PyDict_New();

    PyMapping_SetItemString(flowTime, "DRY", PyFloat_FromDouble(((*$1)->timeInFlowClass)[0]));
    PyMapping_SetItemString(flowTime, "UP_DRY", PyFloat_FromDouble(((*$1)->timeInFlowClass)[1]));
    PyMapping_SetItemString(flowTime, "DN_DRY", PyFloat_FromDouble(((*$1)->timeInFlowClass)[2]));
    PyMapping_SetItemString(flowTime, "SUBCRITICAL", PyFloat_FromDouble(((*$1)->timeInFlowClass)[3]));
    PyMapping_SetItemString(flowTime, "SUPCRITICAL", PyFloat_FromDouble(((*$1)->timeInFlowClass)[4]));
    PyMapping_SetItemString(flowTime, "UP_CRITICAL", PyFloat_FromDouble(((*$1)->timeInFlowClass)[5]));
    PyMapping_SetItemString(flowTime, "DN_CRITICAL", PyFloat_FromDouble(((*$1)->timeInFlowClass)[6]));
    PyMapping_SetItemString(o, "maxFlow", PyFloat_FromDouble((*$1)->maxFlow));
    PyMapping_SetItemString(o, "maxFlowDate", PyFloat_FromDouble((*$1)->maxFlowDate));
    PyMapping_SetItemString(o, "maxVeloc", PyFloat_FromDouble((*$1)->maxVeloc));
    PyMapping_SetItemString(o, "maxDepth", PyFloat_FromDouble((*$1)->maxDepth));
    PyMapping_SetItemString(o, "timeNormalFlow", PyFloat_FromDouble((*$1)->timeNormalFlow));
    PyMapping_SetItemString(o, "timeInletControl", PyFloat_FromDouble((*$1)->timeInletControl));
    PyMapping_SetItemString(o, "timeSurcharged", PyFloat_FromDouble((*$1)->timeSurcharged));
    PyMapping_SetItemString(o, "timeFullUpstream", PyFloat_FromDouble((*$1)->timeFullUpstream));
    PyMapping_SetItemString(o, "timeFullDnstream", PyFloat_FromDouble((*$1)->timeFullDnstream));
    PyMapping_SetItemString(o, "timeFullFlow", PyFloat_FromDouble((*$1)->timeFullFlow));
    PyMapping_SetItemString(o, "timeCapacityLimited", PyFloat_FromDouble((*$1)->timeCapacityLimited));
    PyMapping_SetItemString(o, "timeCourantCritical", PyFloat_FromDouble((*$1)->timeCourantCritical));
    PyMapping_SetItemString(o, "timeInFlowClass", flowTime);
    PyMapping_SetItemString(o, "flowTurns", PyLong_FromLong((*$1)->flowTurns));
    PyMapping_SetItemString(o, "flowTurnSign", PyLong_FromLong((*$1)->flowTurnSign));
    $result = SWIG_Python_AppendOutput($result, o);
    swmm_freeMemory(*$1);
}

%typemap(in, numinputs=0) SM_PumpStats **in_out_dict (SM_PumpStats *temp){
    $1 = &temp;
}
%typemap(argout) SM_PumpStats **in_out_dict {
    PyObject *o = PyDict_New();
    PyMapping_SetItemString(o, "utilized", PyFloat_FromDouble((*$1)->utilized));
    PyMapping_SetItemString(o, "minFlow", PyFloat_FromDouble((*$1)->minFlow));
    PyMapping_SetItemString(o, "avgFlow", PyFloat_FromDouble((*$1)->avgFlow));
    PyMapping_SetItemString(o, "maxFlow", PyFloat_FromDouble((*$1)->maxFlow));
    PyMapping_SetItemString(o, "volume", PyFloat_FromDouble((*$1)->volume));
    PyMapping_SetItemString(o, "energy", PyFloat_FromDouble((*$1)->energy));
    PyMapping_SetItemString(o, "offCurveLow", PyFloat_FromDouble((*$1)->offCurveLow));
    PyMapping_SetItemString(o, "offCurveHigh", PyFloat_FromDouble((*$1)->offCurveHigh));
    PyMapping_SetItemString(o, "startUps", PyLong_FromLong((*$1)->startUps));
    PyMapping_SetItemString(o, "totalPeriods", PyLong_FromLong((*$1)->totalPeriods));
    $result = SWIG_Python_AppendOutput($result, o);
    swmm_freeMemory(*$1);
}

%typemap(in, numinputs=0) SM_SubcatchStats **in_out_dict (SM_SubcatchStats *temp){
    $1 = &temp;
}
%typemap(argout) SM_SubcatchStats **in_out_dict {
    PyObject *o = PyDict_New();
    PyMapping_SetItemString(o, "precip", PyFloat_FromDouble((*$1)->precip));
    PyMapping_SetItemString(o, "runon", PyFloat_FromDouble((*$1)->runon));
    PyMapping_SetItemString(o, "evap", PyFloat_FromDouble((*$1)->evap));
    PyMapping_SetItemString(o, "infil", PyFloat_FromDouble((*$1)->infil));
    PyMapping_SetItemString(o, "runoff", PyFloat_FromDouble((*$1)->runoff));
    PyMapping_SetItemString(o, "maxFlow", PyFloat_FromDouble((*$1)->maxFlow));
    $result = SWIG_Python_AppendOutput($result, o);
    swmm_freeMemory(*$1);
}

%typemap(in, numinputs=0) SM_RoutingTotals **in_out_dict (SM_RoutingTotals *temp){
    $1 = &temp;
}
%typemap(argout) SM_RoutingTotals **in_out_dict {
    PyObject *o = PyDict_New();
    PyMapping_SetItemString(o, "dwInflow", PyFloat_FromDouble((*$1)->dwInflow));
    PyMapping_SetItemString(o, "wwInflow", PyFloat_FromDouble((*$1)->wwInflow));
    PyMapping_SetItemString(o, "gwInflow", PyFloat_FromDouble((*$1)->gwInflow));
    PyMapping_SetItemString(o, "iiInflow", PyFloat_FromDouble((*$1)->iiInflow));
    PyMapping_SetItemString(o, "exInflow", PyFloat_FromDouble((*$1)->exInflow));
    PyMapping_SetItemString(o, "flooding", PyFloat_FromDouble((*$1)->flooding));
    PyMapping_SetItemString(o, "outflow", PyFloat_FromDouble((*$1)->outflow));
    PyMapping_SetItemString(o, "evapLoss", PyFloat_FromDouble((*$1)->evapLoss));
    PyMapping_SetItemString(o, "seepLoss", PyFloat_FromDouble((*$1)->seepLoss));
    PyMapping_SetItemString(o, "reacted", PyFloat_FromDouble((*$1)->reacted));
    PyMapping_SetItemString(o, "initStorage", PyFloat_FromDouble((*$1)->initStorage));
    PyMapping_SetItemString(o, "finalStorage", PyFloat_FromDouble((*$1)->finalStorage));
    PyMapping_SetItemString(o, "pctError", PyFloat_FromDouble((*$1)->pctError));
    $result = SWIG_Python_AppendOutput($result, o);
    swmm_freeMemory(*$1);
}

%typemap(in, numinputs=0) SM_RunoffTotals **in_out_dict (SM_RunoffTotals *temp){
    $1 = &temp;
}
%typemap(argout) SM_RunoffTotals **in_out_dict {
    PyObject *o = PyDict_New();
    PyMapping_SetItemString(o, "rainfall", PyFloat_FromDouble((*$1)->rainfall));
    PyMapping_SetItemString(o, "evap", PyFloat_FromDouble((*$1)->evap));
    PyMapping_SetItemString(o, "infil", PyFloat_FromDouble((*$1)->infil));
    PyMapping_SetItemString(o, "runoff", PyFloat_FromDouble((*$1)->runoff));
    PyMapping_SetItemString(o, "drains", PyFloat_FromDouble((*$1)->drains));
    PyMapping_SetItemString(o, "runon", PyFloat_FromDouble((*$1)->runon));
    PyMapping_SetItemString(o, "initStorage", PyFloat_FromDouble((*$1)->initStorage));
    PyMapping_SetItemString(o, "finalStorage", PyFloat_FromDouble((*$1)->finalStorage));
    PyMapping_SetItemString(o, "initSnowCover", PyFloat_FromDouble((*$1)->initSnowCover));
    PyMapping_SetItemString(o, "finalSnowCover", PyFloat_FromDouble((*$1)->finalSnowCover));
    PyMapping_SetItemString(o, "snowRemoved", PyFloat_FromDouble((*$1)->snowRemoved));
    PyMapping_SetItemString(o, "Continuity Error", PyFloat_FromDouble((*$1)->pctError));
    $result = SWIG_Python_AppendOutput($result, o);
    swmm_freeMemory(*$1);
}
