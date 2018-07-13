/*
 *  swmm_toolkit.i - SWIG interface description file for SWMM toolkit
 * 
 *  Created:    7/2/2018
 *  Author:     Michael E. Tryby
 *              US EPA - ORD/NRMRL
 *  
 *  Build command: 
 *    $ swig -I../../../include -python swmm_toolkit.i
 *
*/ 

%module swmm_toolkit
%{
#include "swmm5.h"

#define SWIG_FILE_WITH_INIT
%}

%include "typemaps.i"

/* DEFINE AND TYPEDEF MUST BE INCLUDED */
typedef void* SWMM_ProjectHandle;


#ifdef WINDOWS
  #ifdef __cplusplus
  #define DLLEXPORT __declspec(dllexport) __cdecl
  #else
  #define DLLEXPORT __declspec(dllexport) __stdcall
  #endif
#else
  #define DLLEXPORT
#endif


/* TYPEMAPS FOR OPAQUE POINTER */
/* Used for functions that output a new opaque pointer */
%typemap(in, numinputs=0) SWMM_ProjectHandle* ph_out (SWMM_ProjectHandle retval)
{
 /* OUTPUT in */
    retval = NULL;
    $1 = &retval;
}
/* used for functions that take in an opaque pointer (or NULL)
and return a (possibly) different pointer */
%typemap(argout) SWMM_ProjectHandle* ph_out, SWMM_ProjectHandle* ph_inout 
{
 /* OUTPUT argout */
    %append_output(SWIG_NewPointerObj(SWIG_as_voidptr(retval$argnum), $1_descriptor, 0));
} 
%typemap(in) SWMM_ProjectHandle* ph_inout (SWMM_ProjectHandle retval)
{
   /* INOUT in */
   SWIG_ConvertPtr(obj0,SWIG_as_voidptrptr(&retval), 0, 0);
    $1 = &retval;
}
/* No need for special IN typemap for opaque pointers, it works anyway */

/* TYPEMAP FOR IGNORING INT ERROR CODE RETURN VALUE */
%typemap(out) int {
    $result = Py_None;
    Py_INCREF($result);
}


/* INSERTS CUSTOM EXCEPTION HANDLING IN WRAPPER */
%exception
{
    char* err_msg;
    swmm_clearError_project(arg1);
    $function
    if (swmm_checkError_project(arg1, &err_msg))
    {
        PyErr_SetString(PyExc_Exception, err_msg);
        free(err_msg);
        SWIG_fail;
    }
}

int  DLLEXPORT  swmm_run_project(SWMM_ProjectHandle ph, const char* f1, const char* f2, const char* f3);
int  DLLEXPORT  swmm_open_project(SWMM_ProjectHandle ph, const char* f1, const char* f2, const char* f3);
int  DLLEXPORT  swmm_start_project(SWMM_ProjectHandle ph, int saveFlag);
int  DLLEXPORT  swmm_step_project(SWMM_ProjectHandle ph, double* elapsedTime);
int  DLLEXPORT  swmm_end_project(SWMM_ProjectHandle ph);
int  DLLEXPORT  swmm_report_project(SWMM_ProjectHandle ph);
int  DLLEXPORT  swmm_getMassBalErr_project(SWMM_ProjectHandle ph, float* runoffErr, float* flowErr, float* qualErr);
int  DLLEXPORT  swmm_close_project(SWMM_ProjectHandle ph);
int  DLLEXPORT  swmm_getError_project(SWMM_ProjectHandle ph, char* errMsg, int msgLen);
int  DLLEXPORT  swmm_getWarnings_project(SWMM_ProjectHandle ph);

%exception;

/* NO EXCEPTION HANDLING FOR THESE FUNCTIONS */
int  DLLEXPORT  swmm_alloc_project(SWMM_ProjectHandle *ph_out);
int  DLLEXPORT  swmm_free_project(SWMM_ProjectHandle *ph_out);

void DLLEXPORT  swmm_clearError_project(SWMM_ProjectHandle ph);
int  DLLEXPORT  swmm_checkError_project(SWMM_ProjectHandle ph, char** msg_buffer);
