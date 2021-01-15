# Diffusion

Various ways of doing 1D, 2D and 3D diffusion within Python and C.

Explored several ways of calling a foreign function using ctypes, cffi and through a CPython module.

Results of running `evolve` for 10.000 iterations for each method:

| Implementation |  Duration   |
|-----|----|
| numpy | 23.09s |
| cffi | 1.38s |
| ctypes | 1.41s |
| CPython | 1.49s |
| GPU | **0.70s** |

Note on GPU: moving from system memory to GPU memory is comparatively slow as the data has to travel through the PCIe bus. 
If we were to include this time into the experiment it takes 2.54s instead of 0.70s! This shows how important it is to make the time spent on GPU as long as possible 
before returning the data back to system memory.

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
