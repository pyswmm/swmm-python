/*
 *  solver.i - SWIG interface description file for swmm-solver
 *
 *  Created:    7/2/2018
 *  Updated:    2/4/2020
 *
 *  Author:     Michael E. Tryby
 *              US EPA - ORD/NRMRL
 *
 *  Build command:
 *    $ python setup.py build
 *
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


/* RENAME REMAINING FUNCTIONS PYTHON STYLE */
//%rename("%(regex:/^\w+_([a-zA-Z]+)_\w+$/\L\\1/)s") "";
%include "solver_rename.i"


/* INSERTS CUSTOM EXCEPTION HANDLING IN WRAPPER */
//%exception
//{
//    char* err_msg;
//    swmm_clearError_project(arg1);
//    $function
//    if (swmm_checkError_project(arg1, &err_msg))
//    {
//        PyErr_SetString(PyExc_Exception, err_msg);
//        free(err_msg);
//        SWIG_fail;
//    }
//}

// CANONICAL API
int  swmm_run(char *f1, char *f2, char *f3);
int  swmm_open(char *f1, char *f2, char *f3);
int  swmm_start(int saveFlag);
int  swmm_step(double *OUTPUT);
int  swmm_end(void);
int  swmm_report(void);
int  swmm_getMassBalErr(float *runoffErr, float *flowErr, float *qualErr);
int  swmm_close(void);
int  swmm_getVersion(void);


//%exception;

/* NO EXCEPTION HANDLING FOR THESE FUNCTIONS */
int  swmm_getError(char *errMsg, int msgLen);
int  swmm_getWarnings(void);
