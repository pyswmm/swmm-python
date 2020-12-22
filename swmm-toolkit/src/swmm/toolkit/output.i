/*
 *  output.i - SWIG interface description file for swmm-output
 *
 *  Created:    November 3, 2017
 *  Updated:    February 21, 2020
 *
 *  Author:     See AUTHORS
 *
*/


%include "typemaps.i"
%include "cstring.i"


/* Docstrings for module */
%include "output_docs.i"

%module(package="swmm.toolkit", docstring=OUTPUT_MODULE_DOCS) output
%{
#define SWIG_FILE_WITH_INIT

#include "swmm_output_enums.h"
#include "swmm_output.h"
%}

/* RENAME FUNCTIONS PYTHON STYLE */
//%rename("%(regex:/^\w+_([a-zA-Z]+)/\L\\1/)s") "";
%include "output_rename.i"


/* MARK FUNCTIONS FOR ALLOCATING AND DEALLOCATING HANDLES */
%newobject SMO_init;
%delobject SMO_close;


/* TYPEMAPS FOR HANDLE POINTER */
/* Used for functions that output a new opaque pointer */
%typemap(in,numinputs=0) SMO_Handle *p_handle (SMO_Handle temp) {
    $1 = &temp;
}
/* used for functions that take in an opaque pointer (or NULL)
and return a (possibly) different pointer */
%typemap(argout) SMO_Handle *p_handle {
    %append_output(SWIG_NewPointerObj(*$1, SWIGTYPE_p_Handle, SWIG_POINTER_NEW));
}


/* TYPEMAP FOR IGNORING INT ERROR CODE RETURN VALUE */
%typemap(out) int {
    $result = Py_None;
    Py_INCREF($result);
}


/* APPLY MACROS FOR OUTPUT VARIABLES */
%apply double *OUTPUT {
    double *date
}

%apply int *OUTPUT {
    int *version,
    int *time
}

%cstring_output_allocate_size(char **elementName, int *size, SMO_freeMemory(*$1));


/* TYPEMAPS FOR MEMORY MANAGEMNET OF FLOAT ARRAYS */
%typemap(in, numinputs=0)float **float_out (float *temp), int *int_dim (int temp){
   $1 = &temp;
}
%typemap(argout) (float **float_out, int *int_dim) {
    if (*$1) {
      PyObject *o = PyList_New(*$2);
      float* temp = *$1;
      for(int i=0; i<*$2; i++) {
        PyList_SetItem(o, i, PyFloat_FromDouble((double)temp[i]));
      }
      $result = SWIG_Python_AppendOutput($result, o);
      SMO_freeMemory(*$1);
    }
}


/* TYPEMAPS FOR MEMORY MANAGEMENT OF INT ARRAYS */
%typemap(in, numinputs=0)int **int_out (int *temp), int *int_dim (int temp){
    $1 = &temp;
}
%typemap(argout) (int **int_out, int *int_dim) {
    if (*$1) {
        int *temp = *$1;
        PyObject *o = PyList_New(*$2);
        for(int i=0; i<*$2; i++) {
            PyList_SetItem(o, i, PyInt_FromLong((long)temp[i]));
        }
        $result = SWIG_Python_AppendOutput($result, o);
        SMO_freeMemory(*$1);
    }
}


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
    SMO_unit,
    SMO_elementType,
    SMO_time,
    SMO_subcatchAttribute,
    SMO_nodeAttribute,
    SMO_linkAttribute,
    SMO_systemAttribute
}


/* INSERTS CUSTOM EXCEPTION HANDLING IN WRAPPER */
%exception SMO_init
{
    $function
}

%exception SMO_close
{
    $function
}

%exception
{
    char *err_msg;
    SMO_clearError(arg1);
    $function
    if (SMO_checkError(arg1, &err_msg))
    {
        PyErr_SetString(PyExc_Exception, err_msg);
        SMO_freeMemory((void *)err_msg);
        SWIG_fail;
    }
}

/* INSERT EXCEPTION HANDLING FOR THESE FUNCTIONS */

%ignore SMO_freeMemory;
%ignore SMO_clearError;
%ignore SMO_checkError;

%include "swmm_output.h"

%exception;
