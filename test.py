"""A collection of unittests for the various bits of code"""

from jacobi_symbol import jacobi_symbol
from miller_rabin import miller_rabin_base_2


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


def testMillerRabinPassesForSmallPrimes():
    for x in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        assert miller_rabin_base_2(x)


def testMillerRabinPassesForLargerPrimes():
    """Largest primes for which the base-2 MR test definitely pass"""
    for x in [2003, 2011, 2017, 2029, 2039]:
        assert miller_rabin_base_2(x)


def testMillerRabinFailsForNonPrimes():
    for x in [
            4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28,
            30
    ]:
        assert not miller_rabin_base_2(x)


def testMillerRabinFailsForStrongPseudoprimes():
    for x in [2047, 3277, 4033, 4681, 8321, 15841, 29341, 42799, 49141]:
        assert miller_rabin_base_2(x)


def testMillerRabinOnEvens():
    for x in range(30, 10000000, 2):
        assert not miller_rabin_base_2(x)
