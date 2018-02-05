from cython.parallel import prange
from libc.stdlib cimport abort, malloc, free
cimport openmp

cdef extern from "stdlib.h":
    cpdef long random() nogil
    cpdef void srandom(unsigned int) nogil
    cpdef const long RAND_MAX

cpdef double randdbl() nogil:
      cdef double r
      r = random()
      return r/RAND_MAX

cpdef double calcpi_omp(const int samples):
    """serially calculate Pi using Cython library functions"""
    cdef int inside, i, num_threads
    cdef double * x
    cdef double * y
    cdef double pi 
    
    inside = 0
    
    srandom(0)

    with nogil:
        x = <double *> malloc(sizeof(double) * samples)  
        y = <double *> malloc(sizeof(double) * samples)
        if x == NULL or y == NULL:
            abort()

    for i in prange(samples, nogil=True,schedule=guided):
        x[i] = randdbl()
        y[i] = randdbl()

    for i in prange(samples, nogil=True,schedule=guided):
        if (x[i]**2+y[i]**2) < 1:
            inside += 1
    pi = (4.0 * inside)/samples
    return pi
