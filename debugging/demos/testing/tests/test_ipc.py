'''
Unit tests for mpi4py functions.
'''

import pytest
from mpi4py import MPI
from mock import Mock
import ipc

# pylint: disable=redefined-outer-name

@pytest.fixture
def mock_mpi():
    '''A mocked MPI module.'''
    mpi = Mock(spec=MPI)
    # mpi.COMM_WORLD = Mock(spec=MPI.COMM_WORLD)
    return mpi


def test_mock_mpi(mock_mpi):
    '''Tests the interface to mocked MPI.'''
    print(dir(mock_mpi.COMM_WORLD))
    assert hasattr(mock_mpi.COMM_WORLD, 'rank')
    assert hasattr(mock_mpi.COMM_WORLD, 'Allgather')


def test_demo_scatter_gather(monkeypatch, mock_mpi):
    '''Tests the ipc.demo_scatter_gather function.'''
    monkeypatch.setattr('ipc.MPI', mock_mpi)
    mock_mpi.COMM_WORLD.size = 2
    mock_mpi.COMM_WORLD.rank = 0
    ipc.demo_scatter_gather()
    mock_mpi.COMM_WORLD.Scatter.assert_called()
    mock_mpi.COMM_WORLD.Allgather.assert_called()
