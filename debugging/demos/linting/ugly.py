#!/usr/bin/env python

from mpi4py import MPI


def HelloWorld():
    COM = MPI.COMM_WORLD
    size = COM.Get_size()
    rank = COM.Get_rank( )
    name = MPI.Get_processor_name()

    padding=len(
      str(size))
    print("Greetings from rank '{1:0{0}d}' of '{2}' on '{3}'.".format(padding, rank, size, name))


if __name__ == '__main__':
    HelloWorld()
