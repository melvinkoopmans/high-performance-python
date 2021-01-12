from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

ext_modules = [
    Extension("juliac", ["juliac.pyx"], extra_compile_args=['-fopenmp'], extra_link_args=['-fopenmp'])
]


setup(
    name="Cython test",
    ext_modules=cythonize(ext_modules, compiler_directives={"language_level": "3"}),
    include_dirs=np.get_include()
)
