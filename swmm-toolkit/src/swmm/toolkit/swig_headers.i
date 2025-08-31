
/* 
in version 4.3, swig had a breaking change. Python functions that return None 
no longer implicitly return void. see https://github.com/swig/swig/pull/2907
and https://github.com/swig/swig/issues/2905

This header block reverts the change from that commit, since I cannot find a 
more concise way to implicitly make functions that return None just be void.

I think the "correct" way is to define typemap(outs) that match every function
signature we have and drop the error code accordingly.
*/
%header %{
SWIGINTERN PyObject*
Custom_SWIG_Python_AppendOutput(PyObject* result, PyObject* obj, int is_void) {
    if (!result) {
    result = obj;
    } else if (result == Py_None) {
    SWIG_Py_DECREF(result);
    result = obj;
    } else {
    if (!PyList_Check(result)) {
        PyObject *o2 = result;
        result = PyList_New(1);
        if (result) {
        PyList_SET_ITEM(result, 0, o2);
        } else {
        SWIG_Py_DECREF(obj);
        return o2;
        }
    }
    PyList_Append(result,obj);
    SWIG_Py_DECREF(obj);
    }
    return result;
}
#define SWIG_Python_AppendOutput Custom_SWIG_Python_AppendOutput
%}