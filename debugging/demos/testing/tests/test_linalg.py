'''
Unit tests for the linear algebra functions.
'''

import pytest
import numpy as np
from linalg import rotate_operator, fail_catastrophically


# pylint: disable=redefined-outer-name

@pytest.fixture
def fixture_matrix():
    '''A fixture matrix that can be re-used in multiple tests.'''
    return np.mat([[0, 1], [2, 3]])


def test_rotate_operator(fixture_matrix):
    '''Tests the `rotate_operator` function.'''
    output = rotate_operator(fixture_matrix)
    assert isinstance(output, np.matrix)
    assert (output == np.mat([[1, 0], [3, -2]])).all()


@pytest.mark.xfail(strict=True, reason="This will always fail.")
def test_fail_catastrophically():
    '''Tests a failing function.'''
    output = fail_catastrophically()
    assert (output == np.mat([[1, 0], [3, -2]])).all()
