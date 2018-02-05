#!/usr/bin/env python2.7

# File: builtins_pi.py
# Author: William Scullin
# Date: 2015-11-28
#
# Sample program that does a serial monte carlo calculation of pi using only
# functions from the standard library.

import random
import time
import util
import calcpipy
import calcpi
import calcpi_omp


def bench_function(f):
    samples = util.get_sample_count()

    start_time = time.time()

    pi = f(samples)

    end_time = time.time()

    util.output(samples, pi, start_time, end_time)

if __name__ == '__main__':
    bench_function(calcpipy.calcpi_py)
    bench_function(calcpi.calcpi)
    bench_function(calcpi_omp.calcpi_omp)
