from miller_rabin import miller_rabin_base_2
from jacobi_symbol import jacobi_symbol
from lucas_pp import lucas_pp

def D_chooser(candidate):
    """Choose a D value suitable for the Baillie-PSW test"""
    D = 5
    while jacobi_symbol(D, candidate) != -1:
        D += 2 if D > 0 else -2
        D *= -1
    return D

def baillie_psw(candidate):
    """Perform the Baillie-PSW probabilistic primality test on candidate"""

    # Check divisibility by a short list of primes less than 50
    for known_prime in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 33, 37, 41, 43, 47]:
        if candidate == known_prime:
            return True
        elif candidate % known_prime == 0:
            return False

    # Now perform the Miller-Rabin primality test base 2
    if not miller_rabin_base_2(candidate):
        return False

    # Finally perform the Lucas primality test
    D = D_chooser(candidate)
    if not lucas_pp(candidate, D, 1, (1-D)/4):
        return False

    # You've probably got a prime!
    return True