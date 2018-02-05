#!/usr/bin/env python3
'''
Example mpi4py scatter-gather operations.
'''


import numpy as np
from mpi4py import MPI


def hello_world():
    '''Print the MPI parameters for this rank.'''
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    name = MPI.Get_processor_name()

    padding = len(str(size))
    print("Greetings from rank '{1:0{0}d}' of '{2}' on '{3}'.".format(
        padding, rank, size, name))


def rank_print(message='', comm=MPI.COMM_WORLD, rank=0):
    '''Print for MPI parallel programs: Only rank 0 prints message.'''
    if comm.rank == rank:
        print(message, sep='', end='\n')


def show_data_state(title, local_data, data, comm=MPI.COMM_WORLD):
    '''Print the contents of each rank's data state.'''
    rank_print('%s:' % title)
    for rank in range(comm.size):
        rank_print('  local_data [%d]: %s' % (comm.rank, local_data),
                   rank=rank)
        comm.Barrier()
    rank_print('        data [%d]: %s' % (comm.rank, data))


def demo_scatter_gather():
    '''A function to demonstrate scatter-gather operations.'''
    comm = MPI.COMM_WORLD

    rank_print('Running on %d cores.' % comm.size)

    scale = 4
    total_data_count = scale * comm.size

    if comm.rank == 0:
        data = np.arange(total_data_count, dtype=np.float64)
    else:
        data = np.zeros(total_data_count, dtype=np.float64)
    local_data = np.zeros(scale, dtype=np.float64)
    show_data_state('Initial state', local_data, data)

    # Scatter data into local_data arrays
    comm.Scatter([data, MPI.DOUBLE], [local_data, MPI.DOUBLE])
    show_data_state('After Scatter', local_data, data)

    # Alter the local data.
    local_data *= 2
    show_data_state('After alteration', local_data, data)

    # Allgather local_data into data again
    comm.Allgather([local_data, MPI.DOUBLE], [data, MPI.DOUBLE])
    show_data_state('After Allgather', local_data, data)


if __name__ == '__main__':
    demo_scatter_gather()
