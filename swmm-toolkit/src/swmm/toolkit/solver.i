/*
 *  solver.i - SWIG interface description file for swmm-solver
 *
 *  Created:    7/2/2018
 *  Updated:    8/17/2020
 *
 *  Author:     Michael E. Tryby
 *              US EPA - ORD/NRMRL
 *
 *              Jennifer Wu
 *              Xylem Inc.
 *
 *              Caleb Buahin
 *              Xylem Inc. 
*/


%include "typemaps.i"
%include "cstring.i"


%module(package="swmm.toolkit") solver
%{
#define SWIG_FILE_WITH_INIT

#include "swmm5.h"
#include "toolkitAPI.h"
#include "toolkitAPI_enums.h"
%}


/* TYPEMAP FOR IGNORING INT ERROR CODE RETURN VALUE */
%typemap(out) int {
    $result = Py_None;
    Py_INCREF($result);
}


/* GENERATES DOCUMENTATION */
%feature("autodoc", "2");


/* RENAME FUNCTIONS PYTHON STYLE */
%include "solver_rename.i"
%include "solver_toolkitapi_rename.i"

/* INSERTS CUSTOM EXCEPTION HANDLING IN WRAPPER */
%exception
{
    $function
    if (result > 0) {
        char errmsg[90];
        swmm_getError(errmsg, 90);
        PyErr_SetString(PyExc_Exception, errmsg);
        SWIG_fail;
    }
}

%apply int *OUTPUT {
    int *year,
    int *month,
    int *day,
    int *hour,
    int *minute,
    int *second
};

%apply double *OUTPUT {
    double *value
};

%cstring_bounded_output(char *OUTCHAR, 256);

/* TYPEMAP FOR ENUMERATED TYPE INPUT ARGUMENTS */
%typemap(in) EnumTypeIn {
    int value = 0;
    if (PyObject_HasAttrString($input, "value")) {
        PyObject *o = PyObject_GetAttrString($input, "value");
        SWIG_AsVal_int(o, &value);
    }
    $1 = ($1_basetype)(value);
}
%apply EnumTypeIn {
    SM_ObjectType,
    SM_NodeType,
    SM_LinkType,
    SM_TimePropety,
    SM_Units,
    SM_SimOption,
    SM_SimSetting,
    SM_NodeProperty,
    SM_LinkProperty,
    SM_SubcProperty,
    SM_NodeResult,
    SM_NodePollut,
    SM_LinkResult,
    SM_LinkPollut,
    SM_SubcResult,
    SM_SubcPollut,
    SM_GagePrecip,
    SM_LidLayer,
    SM_LidLayerProperty,
    SM_LidUProperty,
    SM_LidUOptions,
    SM_LidResult
}

// CANONICAL API
int  swmm_run(char *f1, char *f2, char *f3);
int  swmm_open(char *f1, char *f2, char *f3);
int  swmm_start(int saveFlag);
int  swmm_step(double *OUTPUT);
int  swmm_end(void);
int  swmm_report(void);
int  swmm_getMassBalErr(float *OUTPUT, float *OUTPUT, float *OUTPUT);
int  swmm_close(void);
int  swmm_getVersion(void);


// TOOLKIT API 
int  swmm_getSimulationUnit(int type, int *OUTPUT);
int  swmm_project_findObject(int type, char *id, int *OUTPUT);
int  swmm_countObjects(int type, int *OUTPUT);
int  swmm_getSimulationDateTime(int timetype, int *year, int *month, int *day, int *hour, int *minute, int *second);
int  swmm_setSimulationDateTime(int timetype, int year, int month, int day, int hour, int minute, int second);
int  swmm_getSimulationAnalysisSetting(int type, int *OUTPUT);
int  swmm_getSimulationParam(int type, double *OUTPUT);
%exception;
