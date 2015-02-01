"""A collection of unittests for the various bits of code"""

from nose import *
from jacobi_symbol import jacobi_symbol

def testJacobiSymbolWithALessThanN():
    vals = list(map(lambda x: jacobi_symbol(0, x), [1, 3, 5, 7, 9, 11]))
    assert vals == [1, 0, 0, 0, 0, 0]

    
