/*
 *  solver.i - SWIG interface description file for swmm-solver
 *
 *  Created:    7/2/2018
 *  Updated:    8/17/2020
 *
 *  Author:     See AUTHORS
 * 
*/


%include "typemaps.i"
%include "cstring.i"


/* Docstrings for module */
%include "solver_docs.i"

%module(package="swmm.toolkit", docstring=SOLVER_MODULE_DOCS) solver
%{
#define SWIG_FILE_WITH_INIT

#include "swmm5.h"
#include "toolkit.h"
#include "toolkit_enums.h"
#include "toolkit_structs.h"
%}

/* RENAME FUNCTIONS PYTHON STYLE */
%include "solver_rename.i"

%include "stats_typemaps.i";



/* TYPEMAP FOR IGNORING INT ERROR CODE RETURN VALUE */
%typemap(out) int {
    $result = Py_None;
    Py_INCREF($result);
}


%apply int *OUTPUT {
    int *index,
    int *value,
    int *count, 
    int *node1, 
    int *node2,
    int *out_index,
    int *condition,
    int *year,
    int *month,
    int *day,
    int *hour,
    int *minute,
    int *second
}


%apply double *OUTPUT {
    double *elapsedTime,
    double *value,
    double *result
}


%apply float *OUTPUT {
    float *runoffErr,
    float *flowErr, 
    float *qualErr
}


%apply signed char *OUTPUT {
    signed char *value
}


%apply char *OUTPUT {
    char *condition
}


%cstring_output_allocate(char **OUTCHAR, swmm_freeMemory(*$1));

%apply char **OUTCHAR {
    char **id,
    char **major, 
    char **minor, 
    char **patch
}


/* TYPEMAPS FOR MEMORY MANAGEMNET OF DOUBLE ARRAYS */
%typemap(in, numinputs=0) double **double_out (double *temp) {
    $1=&temp;
}
%typemap(in, numinputs=0) int *int_dim (int temp) {
    $1=&temp;
}
%typemap(argout) (double **double_out, int *int_dim) {
    if (*$1) {
      PyObject *o = PyList_New(*$2);
      for(int i=0; i<*$2; i++) {
        PyList_SetItem(o, i, PyFloat_FromDouble(temp$argnum[i]));
      }
      $result = SWIG_Python_AppendOutput($result, o);
      swmm_freeMemory(*$1);
    }
}

%apply double **double_out {
    double **pollutArray
}
%apply int *int_dim {
    int *length
}
%apply (double **double_out, int *int_dim) {
    (double **pollutArray, int *length)
}


/* TYPEMAP FOR ENUMERATED TYPE INPUT ARGUMENTS */
%typemap(in) EnumTypeIn {
    int value = 0;
    if (PyObject_HasAttrString($input, "value")) {
        PyObject *o = PyObject_GetAttrString($input, "value");
        SWIG_AsVal_int(o, &value);
    }
    else if (PyLong_Check($input)) {
        SWIG_AsVal_int($input, &value);
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


/* TYPEMAPS FOR ENUMERATED TYPE OUTPUT ARGUMENTS */
%typemap(in, numinputs=0) EnumTypeOut * (int temp) {
    $1 = ($1_type)&temp;
}
%typemap(argout) EnumTypeOut * {
    char *temp = "$1_basetype";
    PyObject *module = PyImport_ImportModule("swmm.toolkit.shared_enum");
    PyObject *function = PyDict_GetItemString(PyModule_GetDict(module), (temp + 3));
    if (PyCallable_Check(function)) {
        PyObject *enum_out = PyObject_CallFunction(function, "i", *$1);
        %append_output(enum_out);
    }
}
%apply EnumTypeOut * {
    SM_ObjectType *,
    SM_NodeType *,
    SM_LinkType *
}


/* INSERTS CUSTOM EXCEPTION HANDLING IN WRAPPER */
%exception
{
    $function
    if (result > 0) {
        char* errorMsg = NULL;
        int errorCode = 0;
        errorCode = swmm_getAPIError(result, &errorMsg);
        if (errorCode == 0) {
            PyErr_SetString(PyExc_Exception, errorMsg);
        }
        swmm_freeMemory(errorMsg);
        SWIG_fail;
    }
}

// CANONICAL API
%ignore swmm_getError;
%ignore swmm_getWarnings;
%ignore swmm_IsOpenFlag;
%ignore swmm_IsStartedFlag;

%include "swmm5.h"


// TOOLKIT API
%ignore swmm_run_cb;
%ignore swmm_getAPIError;
%ignore swmm_getObjectIndex;
%ignore swmm_freeMemory;

%include "toolkit.h"


%exception;
