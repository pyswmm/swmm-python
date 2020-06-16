/*
 *  solver.i - SWIG interface description file for swmm-solver
 *
 *  Created:    7/2/2018
 *  Updated:    2/4/2020
 *
 *  Author:     Michael E. Tryby
 *              US EPA - ORD/NRMRL
*/


%include "typemaps.i"


%module(package="swmm.toolkit") solver
%{
#define SWIG_FILE_WITH_INIT

#include "swmm5.h"
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

%exception;
