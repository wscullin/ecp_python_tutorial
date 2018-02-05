from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules=[
    Extension("calcpi",
              sources=["calcpi.pyx"],
              libraries=["m"] # Unix-like specific
    )
]

ext_modules_omp=[
    Extension("calcpi_omp",
              extra_compile_args=['-fopenmp'],
              extra_link_args=['-fopenmp'],
              sources=["calcpi_omp.pyx"],
              libraries=["m"] # Unix-like specific
    )
]

setup(
  name = "calcpi",
  ext_modules = cythonize(ext_modules)
)

setup(
  name = "calcpi_omp",
  ext_modules = cythonize(ext_modules_omp)
)


