# Diffusion

Various ways of doing 1D, 2D and 3D diffusion within Python and C.

Explored several ways of calling a foreign function using ctypes, cffi and through a CPython module.

Results of running `evolve` for 10.000 iterations for each method:

| Implementation |  Duration   |
|-----|----|
| ctypes | 0.027s |
| cffi | 0.023s |
| CPython | **0.018s** |

### Compiling the shared library

You can compile the shared library as follows:

```
$ gcc -O3 -c diffusion.c
$ gcc -shared -o diffusion.so diffusion.o
```

### Building the Python module

To build the Python module run:

```
$ python setup.py build_ext --inplace
```
