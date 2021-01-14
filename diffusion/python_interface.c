// CPython module interface for diffusion.c

#include <Python.h>
#include <numpy/arrayobject.h>
#include "diffusion.h"

// Documentation
static char module_docstring[] = "Provides optimized method to solve the diffusion equation";
static char cdiffusion_evolve_docstring[] = "Evolve a 2D grid using the diffusion equation";

PyArrayObject *py_evolve(PyObject *, PyObject *);

// Module specification
static PyMethodDef module_methods[] =
{
    // { method name, C function, argument types, docstring }
    { "evolve", (PyCFunction) py_evolve, METH_VARARGS, cdiffusion_evolve_docstring },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef cdiffusionmodule =
{
    PyModuleDef_HEAD_INIT,
    "cdiffusion",
    module_docstring,
    -1,
    module_methods
};

PyArrayObject *py_evolve(PyObject *self, PyObject *args)
{
    PyArrayObject *data;
    PyArrayObject *next_grid;
    double dt, D = 1.0;

    // Function "evolve" will have signature:
    //     evolve(data, next_grid, dt, D=1)
    if (!PyArg_ParseTuple(args, "OOd|d", &data, &next_grid, &dt, &D))
    {
        PyErr_SetString(PyExc_RuntimeError, "Invalid arguments");
        return(NULL);
    }

    // Make sure Numpy arrays are contiguous in memory.
    if (!PyArray_Check(data) || !PyArray_ISCONTIGUOUS(data))
    {
        PyErr_SetString(PyExc_RuntimeError, "data is not in a contiguous array.");
        return(NULL);
    }
    if (!PyArray_Check(next_grid) || !PyArray_ISCONTIGUOUS(next_grid))
    {
        PyErr_SetString(PyExc_RuntimeError, "next_grid is not in a contiguous array.");
        return(NULL);
    }

    // Make sure that grid and next_grid are of the same type and have the same dimensions.
    if (PyArray_TYPE(data) != PyArray_TYPE(next_grid))
    {
        PyErr_SetString(PyExc_RuntimeError, "next_grid and data should have same type.");
        return(NULL);
    }
    if (PyArray_NDIM(data) != 2)
    {
        PyErr_SetString(PyExc_RuntimeError, "data should be two dimensional");
        return(NULL);
    }
    if (PyArray_NDIM(next_grid) != 2)
    {
        PyErr_SetString(PyExc_RuntimeError, "next_grid should be two dimensional");
        return(NULL);
    }
    if ((PyArray_DIM(data, 0) != PyArray_DIM(next_grid, 0)) || (PyArray_DIM(data, 1) != PyArray_DIM(next_grid, 1)))
    {
        PyErr_SetString(PyExc_RuntimeError, "data and next_grid must have the same dimensions");
        return(NULL);
    }

    evolve(PyArray_DATA(data), PyArray_DATA(next_grid), D, dt);

    Py_XINCREF(next_grid);
    return (next_grid);
}

// Initialize the module
PyMODINIT_FUNC PyInit_cdiffusion(void)
{
    PyObject *m;

    m = PyModule_Create(&cdiffusionmodule);
    if (m == NULL)
    {
        return(NULL);
    }

    // Load numpy functionality
    import_array();

    return(m);
}
