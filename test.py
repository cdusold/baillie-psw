"""A collection of unittests for the various bits of code"""

from nose import *
from jacobi_symbol import jacobi_symbol

def testJacobiSymbolWithAEqualToZero():
    for x, expected in zip(range(1, 12, 2), [1, 0, 0, 0, 0, 0]):
        assert jacobi_symbol(0, x) == expected

def testJacobiSymbolWithAEqualToOne():
    for x, expected in zip(range(3, 12, 2), [1, 1, 1, 1, 1]):
        assert jacobi_symbol(1, x) == expected

def testJacobiSymbolWithAEqualToTwo():
    for x, expected in zip(range(3, 12, 2), [-1, -1, 1, 1, -1]):
        assert jacobi_symbol(2, x) == expected

def testJacobiSymbolWithAGreaterThanM():
    for x, expected in zip(range(1, 12, 2), [1, 0, -1, -1, 0, 1]):
        assert jacobi_symbol(12, x) == expected

def testJacobiSymbolWithANegative():
    for x, expected in zip(range(-1, -5, -1), [-1, 1, 0, -1, 1]):
        assert jacobi_symbol(x, 3) == expected
