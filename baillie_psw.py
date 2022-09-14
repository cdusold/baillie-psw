from jacobi_symbol import jacobi_symbol
from lucas_pp import lucas_pp
from miller_rabin import miller_rabin_base_2


def D_chooser(candidate):
    """Choose a D value suitable for the Baillie-PSW test"""
    D = 5

    while jacobi_symbol(D, candidate) != -1:
        D += 2 if D > 0 else -2
        D *= -1

    return D


def baillie_psw(candidate):
    """Perform the Baillie-PSW probabilistic primality test on candidate"""

    for known_prime in [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
    ]:
        if candidate == known_prime:
            return True
        elif candidate % known_prime == 0:
            return False

    if not miller_rabin_base_2(candidate):
        return False

    if int(candidate**0.5 + 0.5)**2 == candidate:
        return False

    D = D_chooser(candidate)
    if not lucas_pp(candidate, D, 1, (1 - D) // 4):
        return False

    return True
