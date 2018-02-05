cdef extern from "stdlib.h":
    cpdef long random() nogil
    cpdef void srandom(unsigned int) nogil
    cpdef const long RAND_MAX

cdef double randdbl() nogil:
      cdef double r
      r = random()
      r = r/RAND_MAX
      return r

cpdef double calcpi(const int samples):
    """serially calculate Pi using Cython library functions"""
    cdef int inside, i
    cdef double x, y
    
    inside = 0
    
    srandom(0)
    for i in range(samples):
        x = randdbl()
        y = randdbl()
        if (x*x)+(y*y) < 1:
            inside += 1
    return (4.0 * inside)/samples

