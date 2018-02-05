#!/usr/bin/env python3
'''
Demonstrates unit tests using a contrived example of non-sense linear algebra
functions.
'''


def rotate_operator(matrix):
    '''Prepends 90 degree rotation to linear transformation `matrix`.'''
    return matrix.dot([[0, -1], [1, 0]])


def return_matrixesque():
    '''Returns a nested list that looks like a matrix.'''
    return [[0, 1], [2, 3]]


def fail_catastrophically():
    '''This will not end well.'''
    matrix = return_matrixesque()
    return rotate_operator(matrix)
