#!/usr/bin/env python3
'''
A standard mpi4py 'hello world' application.
'''

from mpi4py import MPI


def main():
    '''Print the MPI parameters for this rank.'''
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    name = MPI.Get_processor_name()

    padding = len(str(size))
    print("Greetings from rank '{1:0{0}d}' of '{2}' on '{3}'.".format(
        padding, rank, size, name))


if __name__ == '__main__':
    main()
