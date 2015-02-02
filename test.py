"""A collection of unittests for the various bits of code"""

from nose import *
from jacobi_symbol import jacobi_symbol

def testJacobiSymbolWithAEqualToZero():
    vals = list(map(lambda x: jacobi_symbol(0, x), [1, 3, 5, 7, 9, 11]))
    assert vals == [1, 0, 0, 0, 0, 0]

def testJacobiSymbolWithAEqualToOne():
    vals = list(map(lambda x: jacobi_symbol(1, x), [3, 5, 7, 9, 11]))
    assert vals == [1, 1, 1, 1, 1]

def testJacobiSymbolWithAEqualToTwo():
    vals = list(map(lambda x: jacobi_symbol(2, x), [3, 5, 7, 9, 11]))
    assert vals == [-1, -1, 1, 1, -1]

def testJacobiSymbolWithAGreaterThanM():
    vals = list(map(lambda x: jacobi_symbol(12, x), [1, 3, 5, 7, 9, 11]))
    assert vals == [1, 0, -1, -1, 0, 1]

def testJacobiSymbolWithANegative():
    vals = list(map(lambda x: jacobi_symbol(x, 3), [-1, -2, -3, -4, -5]))
    assert vals == [-1, 1, 0, -1, 1]
