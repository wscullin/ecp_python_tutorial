#!/usr/bin/env python3
'''
Command-line entry point for running demo MPI app and starting `pdb` session on
a specific rank.

Incantations for the forms:
    mpiexec -n 2 python launch_pdb.py
    mpiexec -stdin 0 -n 2 python launch_pdb.py 0
    mpiexec -stdin 1 -n 2 python launch_pdb.py 1

may work on some resources. HPC resources tend to interfere with the necessary
IO redirection to reliably attach pdb to ranks other than `0`.
'''
import sys
from testing.ipc import MPI, demo_scatter_gather


def launch_debugger_on_rank():
    '''Starts a pdb session on a specific MPI rank.

    Target rank is obtained from the command line (default 0).
    '''
    comm = MPI.COMM_WORLD
    pdb_rank = int(sys.argv[1]) if sys.argv[1:] else 0

    if comm.rank == pdb_rank:
        import pdb; pdb.set_trace()  # noqa pylint: disable=multiple-statements

    demo_scatter_gather()


if __name__ == '__main__':
    launch_debugger_on_rank()
